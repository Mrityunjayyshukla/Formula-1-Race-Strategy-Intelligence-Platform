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

class Laps(F1):
    def __init__(self, lap_df, result_df=None):
        super().__init__(laps=lap_df, telemetry=None, weather=None, results=result_df)

    # Remove Formation lap
    def remove_formation_lap(self):
        self.lap_df = self.lap_df[self.lap_df['LapNumber'] != 0]
        return self.lap_df

    # Handling in-laps and out-laps
    def in_out_laps(self):
        self.lap_df['IsInLap'] = self.lap_df['PitInTime'].isna()
        self.lap_df['IsOutLap'] = self.lap_df['PitOutTime'].isna()
        return self.lap_df

    # Track Status Handling
    def track_status(self):
        trackStatus_map = {
            "1": "Track Clear", "2": "Yellow Flag",
            "4": "Safety Car deployed", "5": "Red Flag (Session Suspended)",
            "6": "Virtual Safety Car deployed","7": "Virtual Safety Car ending"
        }
        statusList = []
        self.lap_df['TrackStatus'].to_string()
        for i in self.lap_df['TrackStatus']:
            status = ""
            for j in i:
                status += trackStatus_map[j] + "-"
            statusList.append(status)
        self.lap_df['TrackData'] = statusList
        self.lap_df['TrackData'] = self.lap_df['TrackData'].str.rstrip("-")
        return self.lap_df

class Telemetry(F1):
    def __init__(self, tele_df, result_df=None):
        super().__init__(laps=None, telemetry=tele_df, weather=None, results=result_df)

    # Removing Impossible values
    def tele_impossible_val(self):
        self.tele_df['Speed'] = self.tele_df[(self.tele_df['Speed'] >= 0) | (self.tele_df['Speed'] < 400)]
        self.tele_df['Throttle'] = self.tele_df[(self.tele_df['Throttle'] >= 0) | (self.tele_df['Throttle'] <= 100)]
        self.tele_df['Brake'] = self.tele_df[(self.tele_df['Brake'].isna()) | (self.tele_df['Brake'].isin([True, False]))]
        return self.tele_df

    # Synchronize Telemetry Frequency
    def synch_frequency(self):
        self.tele_df['Date'] = pd.to_datetime(self.tele_df['Date'])
        self.tele_df = self.tele_df.set_index('Date')
        self.tele_df = self.tele_df[~self.tele_df.index.duplicated(keep='first')]

        # Seperate columns by type to apply interpolation rules
        # - Continous (Speed, throttle, RPM) need linear interpolation
        # - Discrete (nGear, DRS, Brake) need forward fill
        continuous_cols = ['Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z']
        discrete_cols = ['nGear', 'DRS', 'Brake']
        existing_cont = [col for col in continuous_cols if col in self.tele_df.columns]
        existing_disc = [col for col in discrete_cols if col in self.tele_df.columns]
        rule = '100ms'
        self.tele_df = pd.concat([
            self.tele_df[existing_cont].resample(rule).mean().interpolate(method='linear'),
            self.tele_df[existing_disc].resample(rule).ffill()
        ], axis=1)
        self.tele_df = self.tele_df.reset_index()
        return self.tele_df

    # Remove corrupted GPS points
    def corrupted_GPS(self):
        self.tele_df = self.tele_df.dropna(subset = ['X','Y'])
        self.tele_df = self.tele_df[~((self.tele_df['X']==0) & (self.tele_df['Y']==0))]
        # Filter spatial jumps
        self.tele_df['DeltaX'] = self.tele_df['X'].diff()
        self.tele_df['DeltaY'] = self.tele_df['Y'].diff()
        self.tele_df['DistanceStep'] = np.sqrt(self.tele_df['DeltaX']**2 + self.tele_df['DeltaY']**2)
        if 'Date' in self.tele_df.columns:
            parsed_dates = pd.to_datetime(self.tele_df['Date'], errors='coerce')
            self.tele_df['TimeStep'] = parsed_dates.diff().dt.total_seconds()
            self.tele_df['TimeStep'] = self.tele_df['TimeStep'].fillna(0.1)
        else:
            self.tele_df['TimeStep'] = 0.1
        max_plausible_speed = 400
        self.tele_df['ImpliedSpeed'] = np.where(self.tele_df['TimeStep'] > 0, self.tele_df['DistanceStep']/self.tele_df['TimeStep'], 0)
        self.tele_df = self.tele_df[self.tele_df['ImpliedSpeed'] <= max_plausible_speed]
        self.tele_df = self.tele_df.drop(columns=['DeltaX', 'DeltaY', 'DistanceStep','TimeStep','ImpliedSpeed'])
        return self.tele_df

class Weather(F1):
    def __init__(self, weather_df, result_df=None):
        super().__init__(laps=None, telemetry=None, weather=weather_df, results=result_df)

    def weather_impossible_values(self):
        self.weather_df = self.weather_df[(self.weather_df['AirTemp'] >= 10) | (self.weather_df['AirTemp'] <= 45)]
        self.weather_df = self.weather_df[(self.weather_df['TrackTemp'] >= 15) | (self.weather_df['TrackTemp'] <= 60)]
        self.weather_df = self.weather_df[(self.weather_df['Humidity'] >= 10) | (self.weather_df['Humidity'] <= 100)]
        self.weather_df = self.weather_df[(self.weather_df['WindSpeed'] >= 0) | (self.weather_df['WindSpeed'] <= 15)]
        self.weather_df = self.weather_df[(self.weather_df['WindDirection'] >= 0) | (self.weather_df['WindDirection'] <= 360)]
        return self.weather_df

class Result(F1):
    def __init__(self, result_df):
        super().__init__(laps=None, telemetry=None, weather=None, results=result_df)

    # format race completion times
    def race_comp_times(self, row):
        td = pd.to_timedelta(row['FormattedTime'], errors='coerce')
        total_seconds = td.total_seconds()
        if pd.isna(total_seconds):
            return pd.NaT
        h = int(total_seconds//3600)
        m = int((total_seconds%3600) // 60)
        s = int(total_seconds % 60)
        ms = int(round((total_seconds % 1) * 1000))

        if row['Position'] == 1.0:
            return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"
        else:
            total_mins = int(total_seconds // 60)
            return f"+{total_mins:02d}:{s:02d}.{ms:03d}"

    def add_formatted_time(self):
        self.result_df['FormattedTime'] = self.result_df.apply(self.race_comp_times, axis=1)
        return self.result_df

    # DNF, DNS and DSQ flag
    def retire_flag(self, column_name="RaceOutcome"):
        dnfs = ['Retired', 'Accident', 'Collision', 'Engine', 'Gearbox', 'Power Unit', 'Suspension', 'Brakes', 'Overheating']
        conditions = [self.result_df['Status'].isin(dnfs), self.result_df['Status'] == 'DNS', self.result_df['Status'] == 'Disqualified']
        choices = ['DNF', 'DNS', 'DSQ']
        self.result_df[column_name] = np.select(conditions, choices, default='Finished')
        return self.result_df

# folder = "f1_parquet_data/2025/Round_1_Australian_Grand_Prix/R"
# laps, telemetry, weather, results = load_session_data(folder)
# session: F1 = F1(laps, telemetry, weather, results)
# session.fetch_details(session.lap_df, "Laps")
