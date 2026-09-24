import numpy as np
import pandas as pd
import os


def load_session_data(folder_path):
    lap_df = pd.read_parquet(os.path.join(folder_path, "laps.parquet"))
    tele_df = pd.read_parquet(os.path.join(folder_path, "telemetry.parquet"))
    weather_df = pd.read_parquet(os.path.join(folder_path, "weather.parquet"))
    result_df = pd.read_parquet(os.path.join(folder_path, "results.parquet"))
    return lap_df, tele_df, weather_df, result_df
class F1:
    def __init__(self, laps, telemetry, weather, results):
        self.lap_df = laps
        self.weather_df = weather
        self.tele_df = telemetry
        self.result_df = results

    # Getting the necessary information
    def fetch_details(self, df, name="DataFrame"):
        print("Number of rows: ", df.shape[0])
        print("Number of columns: ", df.shape[1])
        print("Columns: ", df.columns.to_list)
        print("Duplicated: ", df.duplicated().sum())
        print("Null: ", df.isna().sum().to_dict())

    # Dropping unnecessary columns
    def drop_columns(self, df, drop_list):
        df = df.drop(drop_list, axis = 1)
        return df

    # Driver Name standardization
    def driver_name_standard(self, df):
        driver_map = dict(zip(
            self.result_df['Abbreviation'], self.result_df['FirstName'] + " " + self.result_df['LastName']
        ))
        df['Driver'] = df['Driver'].map(driver_map).fillna(df['Driver'])
        return df

    # Drop Duplicates
    def drop_duplicates(self, df):
        df = df.drop_duplicates()
        return df

    # Convert times into numeric seconds for multiple columns
    # If there is only one column, use that one column in a list
    def time_to_numeric(self, df, column_list):
        for i in column_list:
            df[i] = df[i].dt.total_seconds()
            return df

    # Creating Flag columns
    def flag_columns(self, df, exist_columns, new_columns):
        if len(exist_columns) != len(new_columns):
            return "Error: Length of lists is not same"
        else:
            for i in range(len(exist_columns)):
                df[new_columns[i]] = df[exist_columns[i]].isna()
        return df

    # create mappings
    def create_mapping(self, df, column_name, map_dict):
        df[column_name] = df[column_name].map(map_dict).fillna(df[column_name])
        return df

    # Change Datatypes
    def change_dtypes(self, df, columns, dtypes):
        if not isinstance(dtypes, list):
            dtypes = [dtypes] * len(columns)
        for col, dtype in zip(columns, dtypes):
            df[col] = df[col].astype(dtype)
        return df

    # Creating Timestamp format
    def timestamp_format(self, df, column_list):
        for i in column_list:
            td = pd.to_timedelta(df[i])
            h = td.dt.components.hours
            m = td.dt.components.minutes
            s = td.dt.components.seconds
            ms = td.dt.components.milliseconds / 1000

            df[i] = (h.astype(str).str.zfill(2) + ":" + m.astype(str).str.zfill(2) + ":" + s.astype(str).str.zfill(2) + "." + ms.astype(str).str.zfill(3))
        return df

    # Get unique values in a column
    def unique_values(self, df, column):
        return df[column].unique().tolist()



# folder = "f1_parquet_data/2025/Round_1_Australian_Grand_Prix/R"
# laps, telemetry, weather, results = load_session_data(folder)
# session: F1 = F1(laps, telemetry, weather, results)
# session.fetch_details(session.lap_df, "Laps")

# Generalised data functions


# Lap Data Functions
# Remove Formation Laps
def remove_formation_laps(df):
    df = df[df['LapNumber'] != 0]
    return df

# Handling in-laps and out-laps
def in_out_laps(df):
    df['IsInLap'] = df['PitInTime'].isna()
    df['IsOutLap'] = df['PitOutTime'].isna()
    return df

# Track Status Handling
trackStatus_map = {
    "1": "Track Clear", "2": "Yellow Flag",
    "4": "Safety Car deployed", "5": "Red Flag (Session Suspended)",
    "6": "Virtual Safety Car deployed","7": "Virtual Safety Car ending"
}
def track_status(df):
    status_list = []
    df['TrackStatus'].to_string()
    for i in df['TrackStatus']:
        status = ""
        for j in i:
            status += trackStatus_map[j] + "-"
        status_list.append(status)
    df['TrackData'] = status_list
    df['TrackData'] = df['TrackData'].str.rstrip("-")
    return df


# Telemetry Data Functions
# Removing impossible values
def tele_impossible_values(df):
    # Speed
    df['Speed'] = df[(df['Speed'] >= 0) | (df['Speed'] < 400)]
    # Throttle
    df['Throttle'] = df[(df['Throttle'] >= 0) | (df['Throttle'] <= 100)]
    # Braking
    df['Brake'] = df[(df['Brake'].isna()) | (df['Brake'].isin([True, False]))]
    return df

# Synchronizing Telemetry Frequency
def synchronize_frequency(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    df = df[~df.index.duplicated(keep='first')]

    # Seperate columns by type to apply interpolation rules
    # - Continous (Speed, throttle, RPM) need linear interpolation
    # - Discrete (nGear, DRS, Brake) need forward fill
    continuous_cols = ['Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z']
    discrete_cols = ['nGear', 'DRS', 'Brake']
    existing_cont = [col for col in continuous_cols if col in df.columns]
    existing_disc = [col for col in discrete_cols if col in df.columns]
    rule = '100ms'
    df = pd.concat([
        df[existing_cont].resample(rule).mean().interpolate(method='linear'),
        df[existing_disc].resample(rule).ffill()
    ], axis=1)

    df = df.reset_index()
    return df

# Remove Corrupted GPS points
def corrupted_GPS(df):
    df = df.dropna(subset=['X','Y'])
    df = df[~((df['X']==0) & (df['Y']==0))]

    # Filter out spatial jumps
    df['DeltaX'] = df['X'].diff()
    df['DeltaY'] = df['Y'].diff()
    df["DistanceStep"] = np.sqrt(df['DeltaX']**2 + df['DeltaY']**2)
    if 'Date' in df.columns:
        parsed_dates = pd.to_datetime(df['Date'], errors='coerce')
        df['TimeStep'] = parsed_dates.diff().dt.total_seconds()
        df['TimeStep'] = df['TimeStep'].fillna(0.1)
    else:
        df['TimeStep'] = 0.1

    max_plausible_speed = 400
    df['ImpliedSpeed'] = np.where(df['TimeStep'] > 0, df['DistanceStep']/df['TimeStep'], 0)
    df = df[df['ImpliedSpeed'] <= max_plausible_speed]
    df = df.drop(columns=['DeltaX', 'DeltaY', 'DistanceStep','TimeStep','ImpliedSpeed'])
    return df

# Weather Data Functions
# Handling impossible values
def weather_impossible_values(df):
    df = df[(df['AirTemp'] >= 10) | (df['AirTemp'] <= 45)]
    df = df[(df['TrackTemp'] >= 15) | (df['TrackTemp'] <= 60)]
    df = df[(df['Humidity'] >= 10) | (df['Humidity'] <= 100)]
    df = df[(df['WindSpeed'] >= 0) | (df['WindSpeed'] <= 15)]
    df = df[(df['WindDirection'] >= 0) | (df['WindDirection'] <= 360)]
    return df

# DNF, DNS and DSQ flag
def retire_flag(df, column_name="RaceOutcome"):
    dnfs = ['Retired', 'Accident', 'Collision', 'Engine', 'Gearbox', 'Power Unit', 'Suspension', 'Brakes', 'Overheating']
    conditions = [
        df['Status'].isin(dnfs),
        df['Status'] == 'DNS',
        df['Status'] == 'Disqualified'
    ]
    choices = ['DNF', 'DNS', 'DSQ']
    df[column_name] = np.select(conditions, choices, default='Finished')
    return df
