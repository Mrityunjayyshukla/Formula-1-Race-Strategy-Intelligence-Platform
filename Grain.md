# Grain
Grain means what does one row represent.\
The important thing with Grain is that Rows with the same grain should never exist.

### **Dimension Tables**
| Table | Grain | Primary Key |
|----------|----------|----------|
| dim_driver | 1 row per driver | driver_id |
| dim_constructor | 1 row per constructor | constructor_id |
| dim_circuit | 1 row per circuit | circuit_id |
| dim_event | 1 row per race weekend | event_id |
| dim_session | 1 row per session | session_id |
---
### **Fact Tables**
| Table | Grain | Primary Key |
|----------|----------|----------|
| fact_lap | 1 row per driver lap | session_id + driver_id + lap_number |
| fact_telemetry | 1 row per telemetry sample | session_id + driver_id + timestamp |
| fact_weather | 1 row per weather observation | session_id + observation_time |
| face_result | 1 row per driver result | session_id + driver_id |
| fact_stint | 1 row per tyre stint | session_id + driver_id + stint_number |
----
### **Relationships**

```
dim_circuit (1) → (many) dim_event
dim_event (1) → (many) dim_session
```
```
dim_session (1) → (many) fact_lap
dim_session (1) → (many) fact_result
dim_session (1) → (many) fact_weather
dim_session (1) → (many) fact_telemetry
dim_session (1) → (many) fact_stint
```

```
dim_driver (1) → (many) fact_lap
dim_driver (1) → (many) fact_result
dim_driver (1) → (many) fact_telemetry
dim_driver (1) → (many) fact_stint

```
```
dim_constructor (1) → (many) fact_lap
dim_constructor (1) → (many) fact_result
dim_constructor (1) → (many) fact_stint
```
```
fact_lap (1) → (many) fact_telemetry
```
---

### Why is Grain useful?
1. **Prevent duplicates:** Immediately see which columns should uniquely identify a record.
2. **Makes joins correct:** Avoids accidentally creating millions of duplicate rows when joining telemetry to laps.
3. **Helps data quality checks:** Easily detect duplicate records by checking the primary key.
4. **Essential for feature engineering:** At what level every feature is being calculated *(lap-level, stint-level, race-level)* is known.
