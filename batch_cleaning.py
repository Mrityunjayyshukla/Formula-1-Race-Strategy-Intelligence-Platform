import numpy as np
import pandas as pd

# Generalised data functions
# Getting the necessary information
def fetch_details(df):
    print("Number of rows: ", df.shape[0])
    print("Number of columns: ", df.shape[1])
    print("Columns: ", df.columns.to_list)
    print("Duplicated: ", df.duplicated().sum())
    print("Null: ", df.isna().sum().to_dict())

# Dropping unnecessary columns
def drop_columns(df, drop_list):
    df = df.drop(drop_list, axis=1)
    return df

# Driver Name standardization
def driver_name_standard(df, result_df):
    driver_map = dict(zip(result_df['Abbreviation'], result_df['FirstName']+" " + result_df['LastName']))
    df['Driver'] = df['Driver'].map(driver_map).fillna(df['Driver'])
    return df

# Drop duplicates
def drop_duplicates(df):
    df = df.drop_duplicates()
    return df

# Convert times into numeric seconds for multiple columns
# If there is only one column, use that one column in a list
def time_to_numeric(df, column_list):
    for i in column_list:
        df[i] = df[i].dt.total_seconds()
        return df

# creating flag columns
def flag_columns(df, exist_columns, new_columns):
    if len(exist_columns) != len(new_columns):
        return "Error: Length of lists is not same"
    for i in range(len(exist_columns)):
        df[new_columns[i]] = df[exist_columns[i]].isna()

    return df

# Create mappings
def create_mapping(df, column_name, map_dict):
    df[column_name] = df[column_name].map(map_dict).fillna(df[column_name])
    print(df[column_name].unique)
    return df

# Change datatypes

# Creating timestamp Format
def timestamp_format(df, column_list):
    for i in column_list:
        td = pd.to_timedelta(df[i])
        h = td.dt.components.hours
        m = td.dt.components.minutes
        s = td.dt.components.seconds
        ms = td.dt.components.milliseconds / 1000

        df[i] = (
            h.astype(str).str.zfill(2) + ":"+
            m.astype(str).str.zfill(2) + ":"+
            s.astype(str).str.zfill(2) + "." +
            ms.astype(str).str.zfill(3)
        )

    return df

# Timestamp format if NaT values are also there
