## 2024 - Round 10 Spanish Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1310
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1267, 'PitInTime': 1268, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 25, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 42, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1310, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1310
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1267, 'PitInTime': 1268, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1310, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 812337
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 37114, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 15209
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 154
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 154
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 11 Austrian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1405
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1359, 'PitInTime': 1359, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 25, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 45, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1405, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1405
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1359, 'PitInTime': 1359, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1405, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 770812
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 33721, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 13088
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 143
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 143
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 1, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 12 British Grand Prix (Race)
### Laps - Before
- **Number of rows:** 960
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 914, 'PitInTime': 914, 'Sector1Time': 19, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 19, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 46, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 960, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 960
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 914, 'PitInTime': 914, 'Sector1Time': 19, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 960, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 711698
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 33138, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 13665
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 147
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 147
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 2, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 13 Hungarian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1355
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1314, 'PitInTime': 1314, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 21, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 41, 'SpeedST': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1355, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1355
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1314, 'PitInTime': 1314, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1355, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 877727
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 40760, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 21313
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 155
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 155
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 1, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 14 Belgian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 841
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 807, 'PitInTime': 806, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 0, 'Sector1SessionTime': 23, 'Sector2SessionTime': 1, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 35, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 841, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 841
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 807, 'PitInTime': 806, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 841, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 703858
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 32247, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 12039
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 137
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 137
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 2, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 15 Dutch Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1426
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1399, 'PitInTime': 1400, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 27, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 26, 'SpeedST': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1426, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1426
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1399, 'PitInTime': 1400, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1426, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 835875
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 39114, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 17181
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 153
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 153
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 16 Italian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1008
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 978, 'PitInTime': 977, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 23, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 31, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1008, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1008
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 978, 'PitInTime': 977, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1008, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 658254
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 30065, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 9039
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 133
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 133
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 1, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 17 Azerbaijan Grand Prix (Race)
### Laps - Before
- **Number of rows:** 973
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 21, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 949, 'PitInTime': 949, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 24, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 26, 'SpeedST': 2, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 973, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 973
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 21, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 949, 'PitInTime': 949, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 973, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 821738
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 38989, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 22877
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 152
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 152
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 4, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 18 Singapore Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1177
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1154, 'PitInTime': 1152, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 22, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 25, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1177, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1177
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1154, 'PitInTime': 1152, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1177, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 893667
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 44535, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 24453
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 160
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 160
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 2, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 19 United States Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1059
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 28, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1035, 'PitInTime': 1036, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 23, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 24, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1059, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1059
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 28, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1035, 'PitInTime': 1036, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1059, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 839380
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 41413, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 21680
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 155
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 155
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 1, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 1 Bahrain Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1129
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1086, 'PitInTime': 1086, 'Sector1Time': 21, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 22, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 43, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1129, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1129
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1086, 'PitInTime': 1086, 'Sector1Time': 21, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1129, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 840934
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 40162, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 18084
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 157
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 157
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 20 Mexico City Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1215
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1193, 'PitInTime': 1193, 'Sector1Time': 22, 'Sector2Time': 4, 'Sector3Time': 2, 'Sector1SessionTime': 23, 'Sector2SessionTime': 4, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 24, 'SpeedST': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1215, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1215
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1193, 'PitInTime': 1193, 'Sector1Time': 22, 'Sector2Time': 4, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1215, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 802697
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 44092, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 27387
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 159
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 159
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 3, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 21 São Paulo Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1134
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 37, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1099, 'PitInTime': 1098, 'Sector1Time': 36, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 38, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 37, 'SpeedST': 5, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1134, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1134
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 37, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1099, 'PitInTime': 1098, 'Sector1Time': 36, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1134, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 800426
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 41149, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 43460
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 201
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 201
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 5, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 22 Las Vegas Grand Prix (Race)
### Laps - Before
- **Number of rows:** 938
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 898, 'PitInTime': 897, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 23, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 41, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 938, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 938
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 898, 'PitInTime': 897, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 938, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 712419
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 35102, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 14525
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 143
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 143
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 2, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 23 Qatar Grand Prix (Race)
### Laps - Before
- **Number of rows:** 943
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 20, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 883, 'PitInTime': 882, 'Sector1Time': 22, 'Sector2Time': 4, 'Sector3Time': 4, 'Sector1SessionTime': 23, 'Sector2SessionTime': 4, 'Sector3SessionTime': 4, 'SpeedI1': 4, 'SpeedI2': 4, 'SpeedFL': 65, 'SpeedST': 4, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 4, 'Deleted': 943, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 943
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 20, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 883, 'PitInTime': 882, 'Sector1Time': 22, 'Sector2Time': 4, 'Sector3Time': 4, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 4, 'Deleted': 943, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 697398
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 34434, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 17099
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 151
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 151
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 5, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 24 Abu Dhabi Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1035
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1007, 'PitInTime': 1005, 'Sector1Time': 21, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 25, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 32, 'SpeedST': 2, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1035, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1035
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1007, 'PitInTime': 1005, 'Sector1Time': 21, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1035, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 719725
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 38100, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 16160
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 148
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 148
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 4, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 2 Saudi Arabian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 901
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 28, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 882, 'PitInTime': 881, 'Sector1Time': 22, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 25, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 21, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 901, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 901
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 28, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 882, 'PitInTime': 881, 'Sector1Time': 22, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 901, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 682437
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 33123, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 11630
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 146
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 146
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 2, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 3 Australian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 998
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 961, 'PitInTime': 961, 'Sector1Time': 21, 'Sector2Time': 2, 'Sector3Time': 3, 'Sector1SessionTime': 26, 'Sector2SessionTime': 2, 'Sector3SessionTime': 3, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 39, 'SpeedST': 2, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 998, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 998
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 961, 'PitInTime': 961, 'Sector1Time': 21, 'Sector2Time': 2, 'Sector3Time': 3, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 998, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 644120
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 33991, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 12630
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 144
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 144
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 19
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 19
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 3, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 4 Japanese Grand Prix (Race)
### Laps - Before
- **Number of rows:** 907
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 31, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 853, 'PitInTime': 852, 'Sector1Time': 45, 'Sector2Time': 3, 'Sector3Time': 3, 'Sector1SessionTime': 46, 'Sector2SessionTime': 3, 'Sector3SessionTime': 3, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 57, 'SpeedST': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 907, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 907
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 31, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 853, 'PitInTime': 852, 'Sector1Time': 45, 'Sector2Time': 3, 'Sector3Time': 3, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 907, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 705089
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 35003, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 31302
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 181
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 181
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 3, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 5 Chinese Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1032
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 25, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 991, 'PitInTime': 991, 'Sector1Time': 23, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 23, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 43, 'SpeedST': 2, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1032, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1032
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 25, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 991, 'PitInTime': 991, 'Sector1Time': 23, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1032, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 862980
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 44017, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 26399
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 165
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 165
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 3, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 6 Miami Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1111
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 5, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1083, 'PitInTime': 1083, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 22, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 29, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1111, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1111
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 5, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1083, 'PitInTime': 1083, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1111, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 815736
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 39279, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 20261
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 150
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 150
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 1, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 7 Emilia Romagna Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1238
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1210, 'PitInTime': 1210, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 25, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 28, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1238, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1238
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1210, 'PitInTime': 1210, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1238, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 782107
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 37780, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 13760
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 143
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 143
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 1, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 8 Monaco Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1237
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 11, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1214, 'PitInTime': 1214, 'Sector1Time': 20, 'Sector2Time': 4, 'Sector3Time': 24, 'Sector1SessionTime': 21, 'Sector2SessionTime': 4, 'Sector3SessionTime': 24, 'SpeedI1': 4, 'SpeedI2': 4, 'SpeedFL': 27, 'SpeedST': 4, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 4, 'Deleted': 1237, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1237
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 11, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1214, 'PitInTime': 1214, 'Sector1Time': 20, 'Sector2Time': 4, 'Sector3Time': 24, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 4, 'Deleted': 1237, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 1129943
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 45683, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 57852
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 200
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 200
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 4, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2024 - Round 9 Canadian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1272
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 5, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1228, 'PitInTime': 1227, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 5, 'Sector1SessionTime': 22, 'Sector2SessionTime': 2, 'Sector3SessionTime': 5, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 47, 'SpeedST': 2, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1272, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1272
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 5, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1228, 'PitInTime': 1227, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 5, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1272, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 886627
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 43640, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 29014
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 113
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 113
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Results - Before
- **Number of rows:** 20
- **Number of columns:** 22
- **Columns:** ['DriverNumber', 'BroadcastName', 'Abbreviation', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FirstName', 'LastName', 'FullName', 'HeadshotUrl', 'CountryCode', 'Position', 'ClassifiedPosition', 'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points', 'Laps']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'BroadcastName': 0, 'Abbreviation': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FirstName': 0, 'LastName': 0, 'FullName': 0, 'HeadshotUrl': 0, 'CountryCode': 0, 'Position': 0, 'ClassifiedPosition': 0, 'GridPosition': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0}

### Results - After
- **Number of rows:** 20
- **Number of columns:** 13
- **Columns:** ['DriverNumber', 'DriverId', 'TeamName', 'TeamColor', 'TeamId', 'FullName', 'Position', 'GridPosition', 'Time', 'Status', 'Points', 'Laps', 'RaceOutcome']
- **Duplicated Values:** 0
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 5, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

