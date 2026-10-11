import numpy as np
import pandas as pd
import os


def load_session_data(folder_path):
    paths = {
            'laps': os.path.join(folder_path, "laps.parquet"),
            'telemetry': os.path.join(folder_path, "telemetry.parquet"),
            'weather': os.path.join(folder_path, "weather.parquet"),
            'results': os.path.join(folder_path, "results.parquet")
        }
    laps_df = pd.read_parquet(paths['laps'])
    weather_df = pd.read_parquet(paths['weather'])
    tele_df = pd.read_parquet(paths['telemetry'])
    results_df = pd.read_parquet(paths['results'])
    return paths, laps_df, weather_df, tele_df, results_df
class F1:
    def __init__(self, df, results, file_path: None):
        self.df = df.copy()
        self.results_df = results
        self.file_path = file_path or {}

    # Getting the necessary information
    def fetch_details(self, name="DataFrame"):
        print("Number of rows: ", self.df.shape[0])
        print("Number of columns: ", self.df.shape[1])
        print("Columns: ", self.df.columns.tolist())
        print("Duplicated: ", self.df.duplicated().sum())
        print("Null: ", self.df.isna().sum().to_dict())

    # Dropping unnecessary columns
    def drop_columns(self, drop_list):
        self.df = self.df.drop(columns = [
            col for col in drop_list if col in self.df.columns
        ], axis = 1)
        return self.df

    # Driver Name standardization
    def driver_name_standard(self):
        if ("Abbreviation" in self.results_df.columns and "Driver" in self.df.columns):
            driver_map = dict(zip(
                self.results_df['Abbreviation'], self.results_df['FirstName'] + " " + self.results_df['LastName']
            ))
            self.df['Driver'] = self.df['Driver'].map(driver_map).fillna(self.df['Driver'])
        return self.df

    # Drop Duplicates
    def drop_duplicates(self):
        self.df = self.df.drop_duplicates()
        return self.df

    # Convert times into numeric seconds for multiple columns
    # If there is only one column, use that one column in a list
    def time_to_numeric(self, columns):
        for i in columns:
            if i in self.df.columns:
                if self.df[i].dtype == bool:
                    print(f"Skipping boolean column: {i}")
                    continue
                self.df[i] = pd.to_timedelta(self.df[i], errors='coerce').dt.total_seconds()
            else:
                print(f"Warning: Column '{i}' not found in DataFrame.")
        return self.df

    # Creating Flag columns
    def flag_columns(self, exist_columns, new_columns):
        if len(exist_columns) != len(new_columns):
            return "Error: Length of lists is not same"
        else:
            for i in range(len(exist_columns)):
                self.df[new_columns[i]] = self.df[exist_columns[i]].isna()
        return self.df

    # create mappings
    def create_mapping(self, column_name, map_dict):
        if column_name in self.df.columns:
            self.df[column_name] = (
            self.df[column_name].map(map_dict).fillna(self.df[column_name])
      )
        return self.df

    # Change Datatypes
    def change_dtypes(self, columns, dtypes):
        if not isinstance(dtypes, list):
            dtypes = [dtypes] * len(columns)
        for col, dtype in zip(columns, dtypes):
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(dtype)
        return self.df

    # Creating Timestamp format
    def timestamp_format(self, column_list):
        for i in column_list:
            if i in self.df.columns:
                td = pd.to_timedelta(self.df[i])
                h = td.dt.components.hours
                m = td.dt.components.minutes
                s = td.dt.components.seconds
                ms = td.dt.components.milliseconds / 1000
                self.df[i] = (
                    h.astype(str).str.zfill(2)
                    + ":"
                    + m.astype(str).str.zfill(2)
                    + ":"
                    + s.astype(str).str.zfill(2)
                    + "."
                    + ms.astype(str).str.zfill(3)
                )
        return self.df

    # Get unique values in a column
    def unique_values(self, column):
        return self.df[column].unique().tolist()

    # Save the cleaned dataframe in seperate parquet files
    def save_cleaned_data(self, output_dir=None):
        datasets = {
            'laps': (self.lap_df, 'laps_cleaned.parquet'),
            'weather': (self.weather_df, 'weather_cleaned.parquet'),
            'telemetry': (self.tele_df, 'telemetry_cleaned.parquet'),
            'results': (self.results_df, 'results_cleaned.parquet'),
        }
        for key, (df, default_name) in datasets.items():
            if df is not None:
                out_path = default_name

                if output_dir:
                    out_path = os.path.join(output_dir, default_name)
                elif key in self.file_path:
                    orig_path = self.file_path[key]
                    orig_dir = os.path.dirname(orig_path)

                    # If orig_dir is not empty, use it; otherwise fall back to default
                    if orig_dir:
                        out_path = os.path.join(orig_dir, default_name)
                    else:
                        print(f"Warning: No directory found in path for '{key}' ({orig_path}). Saving to base folder.")
                else:
                    print(f"Warning: Key '{key}' not found in file_paths. Saving to base folder.")

                # Save to parquet
                df.to_parquet(out_path, index=False)
                print(f"Successfully saved: {out_path}")

class Laps(F1):
    def __init__(self, lap_df, results_df):
        super().__init__(df=lap_df, results=results_df, file_path=None)

    # Remove Formation lap
    def remove_formation_lap(self):
        if "LapNumber" in self.df.columns:
            self.df = self.df[self.df["LapNumber"] != 0]
        return self.df

    # Handling in-laps and out-laps
    def in_out_laps(self):
        if "PitInTime" in self.df.columns:
            self.df["IsInLap"] = self.df["PitInTime"].notna()
        if "PitOutTime" in self.df.columns:
            self.df["IsOutLap"] = self.df["PitOutTime"].notna()
        return self.df

    # Track Status Handling
    def track_status(self):
        trackStatus_map = {
            "1": "Track Clear",
            "2": "Yellow Flag",
            "4": "Safety Car deployed",
            "5": "Red Flag (Session Suspended)",
            "6": "Virtual Safety Car deployed",
            "7": "Virtual Safety Car ending",
        }
        statusList = []
        for val in self.df["TrackStatus"].astype(str):
            status = ""
            for j in val:
                if j in trackStatus_map:
                    status += trackStatus_map[j] + "-"
            statusList.append(status)
        self.df["TrackData"] = statusList
        self.df["TrackData"] = self.df["TrackData"].str.rstrip("-")
        return self.df

class Telemetry(F1):
    def __init__(self, tele_df, results_df=None):
        super().__init__(df=tele_df, results=results_df, file_path=None)

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
    def __init__(self, weather_df, results_df=None):
        super().__init__(df=weather_df, results=results_df, file_path=None)

    def weather_impossible_values(self):
        self.weather_df = self.weather_df[(self.weather_df['AirTemp'] >= 10) | (self.weather_df['AirTemp'] <= 45)]
        self.weather_df = self.weather_df[(self.weather_df['TrackTemp'] >= 15) | (self.weather_df['TrackTemp'] <= 60)]
        self.weather_df = self.weather_df[(self.weather_df['Humidity'] >= 10) | (self.weather_df['Humidity'] <= 100)]
        self.weather_df = self.weather_df[(self.weather_df['WindSpeed'] >= 0) | (self.weather_df['WindSpeed'] <= 15)]
        self.weather_df = self.weather_df[(self.weather_df['WindDirection'] >= 0) | (self.weather_df['WindDirection'] <= 360)]
        return self.weather_df

class Result(F1):
    def __init__(self, results_df):
        super().__init__(df=None, results=results_df, file_path=None)

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
        self.results_df['FormattedTime'] = self.results_df.apply(self.race_comp_times, axis=1)
        return self.results_df

    # DNF, DNS and DSQ flag
    def retire_flag(self, column_name="RaceOutcome"):
        dnfs = ['Retired', 'Accident', 'Collision', 'Engine', 'Gearbox', 'Power Unit', 'Suspension', 'Brakes', 'Overheating']
        conditions = [self.results_df['Status'].isin(dnfs), self.results_df['Status'] == 'DNS', self.results_df['Status'] == 'Disqualified']
        choices = ['DNF', 'DNS', 'DSQ']
        self.results_df[column_name] = np.select(conditions, choices, default='Finished')
        return self.results_df

# We have f1_parquet_data
# In that there will be a list of years: 2022 - 2025
# In that we have round numbers. Creating a list of number of rounds each year
# There we add a condition that check only the "R" folder.
# # Save cleaned files to the exact same folders as the originals


folder_path = "f1_parquet_data/2025/Round_1_Australian_Grand_Prix/R"
paths, lap_df, tele_df, weather_df, results_df = load_session_data(folder_path)
f1_laps = Laps(lap_df=lap_df, results_df=results_df)

f1_laps.fetch_details()  # Working

lap_drop = ["Time", "DriverNumber", "Sector1SessionTime", "Sector2SessionTime", "Sector3SessionTime", "SpeedI1", "SpeedI2", "SpeedFL", "SpeedST", "LapStartTime", "LapStartDate", "FastF1Generated"]
f1_laps.drop_columns(lap_drop)
f1_laps.drop_duplicates()
f1_laps.driver_name_standard()

columnToNumeric = ["LapTime", "Sector1Time", "Sector2Time", "Sector3Time", 'PitInTime', 'PitOutTime']
f1_laps.time_to_numeric(columnToNumeric)

exist_columns = ["Sector1Time", "Sector2Time", "Sector3Time"]
new_columns = ["MissingSector1", "MissingSector2", "MissingSector3"]
f1_laps.flag_columns(exist_columns=exist_columns, new_columns=new_columns)

f1_laps.remove_formation_lap()
f1_laps.in_out_laps()
f1_laps.track_status()

compound_df = {"SOFT": 1, "MEDIUM": 2, "HARD": 3, "INTERMEDIATE": 4, "WET": 5}
f1_laps.create_mapping("Compound", compound_df)

columns_to_change = ["LapNumber", "Stint", "IsPersonalBest", "TyreLife", "TrackStatus"]
dtypes_to_apply = ['int64', 'int64', bool, bool, 'int64']
f1_laps.change_dtypes(columns_to_change, dtypes_to_apply)

# FIX: Print and save from f1_laps.df (the modified dataframe), not lap_df
print(f1_laps.df)
f1_laps.df.to_parquet("laps_cleaned.parquet", index=False)
print("Successfully saved cleaned laps to laps_cleaned.parquet")
