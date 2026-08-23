# **Data Cleaning process**
Data cleaning process involves **six** main steps.
- The first step is to create a Data Profiling for the complete data.
- Second step involves performing cleaning process on each type of data table i.e., **Laps**, **Telemetry**, **Weather**, and **Race Results**.
- Third step is **Cross Dataset Cleaning**. This involves validating the relationships between different data tables.
- Fourth step is to perform Outlier Treatment to eliminate any outliers that exist in the data. This is important as the outliers can affect the overall data.
- Fifth step includes performing Data Quality checks to make sure that the data which is being provided is perfect for Feature Engineering.
- Final step is to generate the clean data and a few data reports which are important to showcase the improvement that has been done in the data due to data cleaning process.

## Step 1: Data Profiling
For each table, identify:
1. Number of Rows and Columns
2. Null percentage
3. Duplicate percentage
4. Data Types
5. Unique values
6. Outlier ranges

Output a profiling report for each dataset to get an idea of what necessary operations are required to be performed for the data cleaning process.

## Step 2: Cleaning each Dataset Type
Different types of dataset i.e., **Laps**, **Telemetry**, **Weather**, and **Race Results** include different type of data. So it is necessary to perform cleaning process for each type of dataset seperately.

### 2.1:  Lap Data Cleaning
1. Check and remove the duplicate laps. Check duplicates on the columns
    - Driver
    - Lap number
    - Session
    - Race
2. Standardize Driver names. For example, **VER**/**Verstappen** will be **Max Verstappen**.
3. Convert lap times for the columns
    - Laptime
    - Sector1Time
    - Sector2Time
    - Sector3Time <br>

    from *days-hours-minutes-seconds* to numeric seconds.
4. Handle the missing sector times. They are usually missing due to **Pit Laps**, **Formation Laps**, or **Retirements**. To handle these, create flags like **missing_sector1**, **missing_sector2**, and **missing_sector3**.
5. Remove the Formation Laps. Remove the laps in which the **Lap Number** is **0**.
6. Handle the **In-Laps** and **Out-Laps**. Don't blindly remove the laps. Instead, to handle this, keep flags like **IsInLap**, and **IsOutLap**.
7. Remove abnormally slow laps
    - Safety Car,
    - Virtual Safety Car,
    - Red flag. <br>

    Use **Trackstatus** column to get the abnormal laps.
8. Check Tyre Data. *Standardize* and *Encode* Tyre compounds.
     - Wet
     - Intermediate
     - Soft
     - Medium
     - Hard
9. Validate Positions. The positions can't be *negative*, *zero* or *unrealistic*.

### 2.2: Telemetry Data Cleaning
1. Remove the duplicate **Time Stamps**. Timestamp should be unique per lap.
2. Standardize Units.
    - Speed - km/h,
    - Distance - meters,
    - RPM - integer
3. Handle missing telemetry like **Brake**, **Throttle**, **RPM**. Use Forward fill, Interpolation, and dropping if entire section is missing.
4. Remove impossible values like:
    - Speed < 0 or Speed > 400kmph
    - Throttle < 0 or > 100%
    - Brake value outside expected range
5. Synchronize the Telemetry Frequency. Different sessions may have different sample counts. Resample to standard intervals.
6. Remove corrupted GPS points. Check for the invalid **X-coordinate** and **Y-coordinate**.
7. Create consistent Timestamp format.

### 2.3: Weather Data cleaning
1. Handle missing readings. Use *Forward Fill* or *interpolation* for the same.
2. Standardize timestamp for consistency.
3. Remove Impossible Weather Values like temperature below -20 C or above 80 C
4. Create a **Rain Indicator** flag. Like Rain = 1 and Dry = 0.
5. Aggregate Weather. Create race level weather summaries like
    - avg_track_temp,
    - max_track_temp,
    - avg_humidity

### 2.4: Race result Data cleaning
1. Standardize Driver IDs. Keep it same as the Lap dataset.
2. Standardize Team Names. For Example, use either **Red Bull Racing** or **Oracle Red Bull Racing**.
3. Convert Finishing positions to numeric (integer). Use separate status for *DNF*, *DSQ*, and *DNS*.
4. Create race outcome flags like **Finished**, **DNF** and **DSQ**.
5. Validate the Points.

## Step 3: Cross Dataset Cleaning
This step includes validating relationships between different tables.
1. Driver in
    - Results
    - Laps
2. Driver in
    - Laps
    - Telemetry
3. Race ID in
    - Results
    - Weather
4. No Orphan records should exist.
5. Create surrogate keys like
    - race_id,
    - session_id,
    - driver_id

## Step 4: Outlier Treatment
Don't just remove the outliers. An Outlier can be **Pit Stop Lap**, **Safety Car Lap**, **Wet Weather Lap**, **Crash Lap**.<br>Do not simply remove them. Instead, create flags like **is_pit**, **is_SC**, **is_red_flag**, **is_wet**

## Step 5: Data quality checks
Run some Quality tests to make sure the data is ready for Feature Engineering.
1. **Completeness** - Null percentages
2. **Uniqueness** - No duplicate lap records
3. **Validity** - Speed within realistic range
4. **Consistency** - Driver names identical across datasets
5. **Referential integrity** - Every driver exists in driver dimension
6. **Accuracy** - Lap time > 0


## Step 6: Final Output
1. Cleaned_laps
2. Cleaned_telemetry
3. Cleaned_weather
4. Cleaned_results<br>

Alongside them, quality report containing **Rows before and after cleaning**, **Null reduction percent**, **Duplicate reduction percent**, **Data quality score** including a formal data quality layer.
