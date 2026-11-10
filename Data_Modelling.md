# Phase 4: Data Modelling

Once the data is cleaned, phase 4 should convert those seperate files into a consistent analytical model.<br>
The objective is:
> Cleaned session files → standardised dimensions and facts → analytics ready Gold layer

## 1. Organize the data into layers
```
data/
├── raw/             # Original API output
├── cleaned/       # Cleaned parquet files
└── gold/            # Analytics ready model
    ├── dimensions/
    ├── facts/
    ├── aggregates/
    └── quality/
```
---
## 2. Decide the grain of every table
The grain describes what one row represents. Define it before choosing columns or keys.
### Recommended grains

| **Table** | **One row represents** |
|---------------|-----------------|
| `dim driver` | One driver |
| `dim_constructor` | One constructor or one team |
| `dim_circuit` | One circuit |
| `dim_event` | One Grand Prix Event |
| `dim_session` | One Session within an event |
| `fact_lap` | One driver's completed lap in one session |
| `fact_result` | One driver's result in one session |
| `fact_weather` | One weather observation in one session |
| `fact_telemetry` | One telemetry sample for one driver |
| `fact_stint` | One continous tyre stint by one driver |

\
Defiing the grains prevents accidental duplicate rows during joins.\
For example:

```
fact_lap grain: one row per session_id + driver_id + lap_number
```
```
fact_telemetry grain: one row per session_id + driver_id + lap_number + timestamp
```
---
## 3. Create stable identifiers
Don't rely on names such as **Austrian Grand Prix** because names can vary between seasons or files.\
Create deterministic identifiers.
### Event ID
```
event_id = season + round_number
2023_09
```
### Session ID
```
session_id = season + round_number + session_type
2023_09_R
2023_10_S
```
### Driver ID
Prefer stable driver identifier of drivers.\
Store driver number and abbreviation as attributes.
```
driver_id = stable driver reference
```
### Lap ID
```
lap_id = session_id + driver_id + lap_number
2023_09_R_VER_36
```
### Telemetry ID
```
telemetry_id = session_id + driver_id + lap_number + timestamp
```
---
## 4. Build the dimension tables
### 4.1. Dim_Driver
Recommended columns:
```
driver_id
driver_number
driver_code
first_name
last_name
full_name
country_code
date_of_birth             # optional
```
Keep driver identity seperate from the team because drivers can change teams between seasons.

### 4.2. Dim Constructor
Recommended columns:
```
constructor_id
constructor_name
constructor_standardised_name
nationality
```
use category mapping table to standardise team names.\
For example:
```
Oracle Red Bull Racing → RED_BULL_RACING
Red Bull Racing → RED_BULL_RACING
```
Do not lose the original value, Keep both
```
constructor_raw
constructor_standardised_name
```

### 4.3. Dim Circuit
Recommended columns:
```
circuit_id
circuit_name
country
city
circuit_length_km
number_of_corners
circuit_type
```
Circuit type is the catgorical value telling the type which the circuit belongs to:

- Street
- Permanent
- Hybrid

Circuit characteristics can later support feature engineering, such as average-speed circuits versus high-downforce circuits.

### 4.4. Dim Event
This represents a specific Grand Prix Weekend.\
Recommended columns:
```
event_id
season
round_number
event_name
official_event_name
event_date
country
circuit_id
event_format
```
Event format can be of two types:

- Conventional
- Sprint

### 4.5. Dim Session
This is particularly important because the source files are seperated by session.
```
session_id
event_id
session_name
session_type
session_date
session_start_time
scheduled_laps
```
-------------

## 5. Build **Fact Lap**
This should be the principal analytical fact table.
### Grain
> One Driver, one lap, one session
### Keys
```
lap_id
session_id
event_id
driver_id
constructor_id
```

The Lap measurements will be
```
lap_number
lap_time_seconds
sector_1_time
sector_2_time
sector_3_time
speed_I1
speed_I2
speed_I3
speed_ST
speed_FL
position
stint_number
compound
tyre_life
fresh_tyre   # True / False
```
Operational Flags will be
```
is_accurate
is_deleted
is_personal_best
is_pit_in_lap
is_pit_out_lap
is_wet_lap
is_SC_lap
is_VSC_lap
is_red_flag_period
```
Keep inaccurate, pit and disrupted laps in primary fact table. Use flags to exclude them in a specific analysis.
### Uniqueness Test
Each combination should be unique with:
> session_id + driver_id + lap_number

Any duplication should fail the transformation or be moved into quarantine table.

---

## 6. Build **Fact Result**
### Grain
> One driver's result in one session

### Recommended Columns:
```
session_id
event_id
driver_id
constructor_id
grid_position
classified_position
position_order
points
laps_completed
result_time_seconds
result_gap_seconds
status
finished_flag    # True / False
dnf_flag           # True / False
dns_flag           # True / False
dsq_flag           # True / False
podium_flag     # True / False
winner_flag      # True / False
```

Do not force `DNF`, `DSQ`, or `DNS` into numerical finishing position field.\
Use:
```
classified_position = nullablenumber position
status = DNF, DNS, DSQ, FINISHED, LAPPED
```
This keeps the outcome suitable for both reporting and machine learning.

---
## 7. Build **Fact Weather**
Weather should normally be a fact table, not `dim_weather`, because temperature, humidity, pressure, and wind change during a session.
### Grain
> One weather observation at one timestamp in one session

### Recommended Columns
```
session_id
observation_time
air_temp
track_temp
humidity_percentage
pressure_mbar
wind_speed
wind_direction
rainfall
rain_flag
```
Create and additional lap-level weather table if required:
### Bridge Lap Weather
Recommended Columns for this optional table are:
```
lap_id
weather_observation_time
time_difference_seconds
air_temp
track_temp
humidity_percentage
rain_flag
```
Assign each lap the nearest available weather observation based on timestamp. Use an as-of or nearest time match, not a normal exact timestamp join.

-----

## 8. Build **Fact Telemetry**
Telemetry is the largest table and needs special treatment.
### Grain
> One telemetry observtion for one driver at one timestamp

### Recommended columns
```
session_id
event_id
driver_id
lap_id
lap_number
timestamp
session_time_seconds
lap_time_elapsed_seconds
distance_metres
relative distance
speed_kmph
rpm
gear
throttle_percentage
brake
drs
x
y
z
```
### Important design decision
Do not join full telemetry into `fact_lap`\
One lap row may correspond to hundreds or thousands of telemetry samples. Joining them would repeat the lap data many times and produce an unnecessarily large table.
Instead:\
```
fact_lap.lap_id → fact_telemetry.lap_id
```
This gives a one-to-many relationships.

### Partitioning
Partition telemetry by:
```
season
event
session
driver
```
Example:
```
gold/facts/fact_telemetry/
└── season=2023/
    └── round=09/
        └── session=R/
            └── Driver = VER
```
Only add lap number as another physical partition if individual partitions remain large enough. Excessive small partitions can make reading slower.

---

## 9. Create **Fact Stint**
This should be derived form the cleaned lap table and will be extremely useful for strategy analysis.
### Grain
> One continous tyre stint for one driver
### Recommended Columns
```
session_id
driver_id
constructor_id
stint_number
compound
fresh_tyre
start_lap
end_lap
stint_laps
starting_tyre_life
ending_tyre_life
average_lap_time_seconds
median_lap_time_seconds
best_lap_time_seconds
lap_time_std_seconds
pit_in_lap
pit_out_lap
average_track_temperature
wet_stint_flag
safety_car_affected_flag
```
This table directly supports:
- Tyre degradation analysis
- Strategy comparisons
- One stop versus two stop strategies
- Undercut and overcut analysis
- Pit window modelling

Seperate consecutive stints even if the driver uses same compound again.
For example:
> **Stint 1:** MEDIUM, laps 1-24\
> **Stint 2:** HARD, laps 25-51\
> **Stint 3:** MEDIUM, laps 52-71

The two medium stints must not be merged.

---

## 10. Create telemetry aggregate tables
Most dashboard queries should not scan every raw telemetry sample.\
Create a lap-level telemetry aggregate:
**agg_lap_telemetry**
### Grain
> One row per lap
### Recommended Metrics:
```
lp_id
max_speed_kmph
average_speed_kmph
median_speed_kmph
average_throttle_percentage
full_throttle_percentage
braking_percentage
brake_event_count
average_rpm
maximum_rpm
gear_change_count
drs_usage_percentage
distance_measured_metres
```
You may also create:
```
agg_driver_session
agg_driver_race
agg_constructor_race
agg_circuit_compound
```

These aggregate tabkes will make feature engineering stage must faster.

---
