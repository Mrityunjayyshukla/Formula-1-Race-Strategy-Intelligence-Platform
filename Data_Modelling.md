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
