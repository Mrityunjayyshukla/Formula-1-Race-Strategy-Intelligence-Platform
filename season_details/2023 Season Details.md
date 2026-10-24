## 2023 - Round 10 British Grand Prix (Race)
### Laps - Before
- **Number of rows:** 971
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 5, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 947, 'PitInTime': 945, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 23, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 27, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 971, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 971
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 5, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 947, 'PitInTime': 945, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 971, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 730641
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 37545, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 15307
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 3, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2023 - Round 11 Hungarian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1252
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1216, 'PitInTime': 1213, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 21, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 39, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1252, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1252
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1216, 'PitInTime': 1213, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1252, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 811082
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 43179, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 21485
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 164
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 164
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

## 2023 - Round 12 Belgian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 816
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 778, 'PitInTime': 778, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 20, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 39, 'SpeedST': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 816, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 816
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 778, 'PitInTime': 778, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 816, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 705818
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 34043, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 13640
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 2, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2023 - Round 13 Dutch Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1343
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 33, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1241, 'PitInTime': 1241, 'Sector1Time': 39, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 42, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 104, 'SpeedST': 17, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1343, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1343
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 33, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1241, 'PitInTime': 1241, 'Sector1Time': 39, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1343, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 1126733
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 38220, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 49760
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 209
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 209
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

## 2023 - Round 14 Italian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 957
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 9, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 932, 'PitInTime': 931, 'Sector1Time': 28, 'Sector2Time': 9, 'Sector3Time': 9, 'Sector1SessionTime': 29, 'Sector2SessionTime': 9, 'Sector3SessionTime': 9, 'SpeedI1': 9, 'SpeedI2': 9, 'SpeedFL': 35, 'SpeedST': 9, 'IsPersonalBest': 9, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 9, 'Deleted': 957, 'DeletedReason': 9, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 957
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 9, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 932, 'PitInTime': 931, 'Sector1Time': 28, 'Sector2Time': 9, 'Sector3Time': 9, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 9, 'Deleted': 957, 'DeletedReason': 9, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 637716
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 30019, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 9876
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 156
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 156
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

## 2023 - Round 15 Singapore Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1088
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 26, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1062, 'PitInTime': 1063, 'Sector1Time': 23, 'Sector2Time': 4, 'Sector3Time': 4, 'Sector1SessionTime': 23, 'Sector2SessionTime': 4, 'Sector3SessionTime': 4, 'SpeedI1': 4, 'SpeedI2': 4, 'SpeedFL': 29, 'SpeedST': 5, 'IsPersonalBest': 3, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 4, 'Deleted': 1088, 'DeletedReason': 3, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1088
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 26, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1062, 'PitInTime': 1063, 'Sector1Time': 23, 'Sector2Time': 4, 'Sector3Time': 4, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 4, 'Deleted': 1088, 'DeletedReason': 3, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 855630
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 47509, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 29442
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 176
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 176
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 1, 'GridPosition': 1, 'Time': 5, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2023 - Round 16 Japanese Grand Prix (Race)
### Laps - Before
- **Number of rows:** 880
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 61, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 836, 'PitInTime': 832, 'Sector1Time': 22, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 25, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 48, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 880, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 880
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 61, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 836, 'PitInTime': 832, 'Sector1Time': 22, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 880, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 718035
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 35556, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 17743
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 158
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 158
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

## 2023 - Round 17 Qatar Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1006
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 6, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 951, 'PitInTime': 951, 'Sector1Time': 19, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 21, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 56, 'SpeedST': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1006, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1006
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 6, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 951, 'PitInTime': 951, 'Sector1Time': 19, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1006, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 716325
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 34544, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 14264
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

## 2023 - Round 18 United States Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1014
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 974, 'PitInTime': 975, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 24, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 39, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1014, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1014
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 974, 'PitInTime': 975, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1014, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 795493
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 38627, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 21258
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 168
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 168
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

## 2023 - Round 19 Mexico City Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1282
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 30, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1243, 'PitInTime': 1240, 'Sector1Time': 41, 'Sector2Time': 1, 'Sector3Time': 2, 'Sector1SessionTime': 43, 'Sector2SessionTime': 1, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 1, 'SpeedFL': 43, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1282, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1282
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 30, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1243, 'PitInTime': 1240, 'Sector1Time': 41, 'Sector2Time': 1, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1282, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 856330
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 44778, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 40244
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 190
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 190
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

## 2023 - Round 1 Bahrain Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1056
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1006, 'PitInTime': 1004, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 25, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 53, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1056, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1056
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1006, 'PitInTime': 1004, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1056, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 800120
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 39211, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 19225
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 161
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 161
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

## 2023 - Round 20 São Paulo Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1108
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 19, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1041, 'PitInTime': 1038, 'Sector1Time': 36, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 38, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 72, 'SpeedST': 17, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1108, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1108
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 19, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1041, 'PitInTime': 1038, 'Sector1Time': 36, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1108, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 678854
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 38869, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 34683
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 183
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 183
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 6, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2023 - Round 21 Las Vegas Grand Prix (Race)
### Laps - Before
- **Number of rows:** 946
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 85, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 915, 'PitInTime': 915, 'Sector1Time': 23, 'Sector2Time': 3, 'Sector3Time': 3, 'Sector1SessionTime': 24, 'Sector2SessionTime': 3, 'Sector3SessionTime': 3, 'SpeedI1': 3, 'SpeedI2': 3, 'SpeedFL': 34, 'SpeedST': 3, 'IsPersonalBest': 3, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 946, 'DeletedReason': 3, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 946
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 85, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 915, 'PitInTime': 915, 'Sector1Time': 23, 'Sector2Time': 3, 'Sector3Time': 3, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 946, 'DeletedReason': 3, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 773585
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 29937, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 19058
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 108
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 108
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

## 2023 - Round 22 Abu Dhabi Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1157
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1120, 'PitInTime': 1119, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 23, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 38, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1157, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1157
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1120, 'PitInTime': 1119, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1157, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 802189
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 37497, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 15865
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 156
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 156
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

## 2023 - Round 2 Saudi Arabian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 943
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 19, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 919, 'PitInTime': 918, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 22, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 26, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 943, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 943
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 19, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 919, 'PitInTime': 918, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 943, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 705586
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 34754, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 11857
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 2, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2023 - Round 3 Australian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1003
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 102, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 936, 'PitInTime': 938, 'Sector1Time': 35, 'Sector2Time': 8, 'Sector3Time': 71, 'Sector1SessionTime': 37, 'Sector2SessionTime': 8, 'Sector3SessionTime': 71, 'SpeedI1': 8, 'SpeedI2': 8, 'SpeedFL': 73, 'SpeedST': 8, 'IsPersonalBest': 7, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 8, 'Deleted': 1003, 'DeletedReason': 7, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1003
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 102, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 936, 'PitInTime': 938, 'Sector1Time': 35, 'Sector2Time': 8, 'Sector3Time': 71, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 8, 'Deleted': 1003, 'DeletedReason': 7, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 1100058
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 37344, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 55728
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 222
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 222
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 8, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2023 - Round 4 Azerbaijan Grand Prix (Race)
### Laps - Before
- **Number of rows:** 962
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 32, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 937, 'PitInTime': 938, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 23, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 25, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 962, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 962
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 32, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 937, 'PitInTime': 938, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 962, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 807832
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 39326, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 21292
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

## 2023 - Round 5 Miami Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1138
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1118, 'PitInTime': 1118, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 21, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 20, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1138, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1138
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1118, 'PitInTime': 1118, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1138, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 816234
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 36737, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 17683
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2023 - Round 6 Monaco Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1515
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1478, 'PitInTime': 1477, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 2, 'Sector1SessionTime': 23, 'Sector2SessionTime': 1, 'Sector3SessionTime': 2, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 39, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1515, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1515
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1478, 'PitInTime': 1477, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1515, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 986225
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 48283, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 37643
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 176
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 176
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

## 2023 - Round 7 Spanish Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1312
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1267, 'PitInTime': 1269, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 25, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 43, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1312, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1312
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1267, 'PitInTime': 1269, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1312, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 815048
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 37672, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 15032
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

## 2023 - Round 8 Canadian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1317
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1284, 'PitInTime': 1283, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 3, 'Sector1SessionTime': 24, 'Sector2SessionTime': 1, 'Sector3SessionTime': 3, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 35, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 35, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1317, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1317
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1284, 'PitInTime': 1283, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 3, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1317, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 824411
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 42654, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 20299
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 162
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 162
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

## 2023 - Round 9 Austrian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1354
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1289, 'PitInTime': 1291, 'Sector1Time': 21, 'Sector2Time': 2, 'Sector3Time': 1, 'Sector1SessionTime': 24, 'Sector2SessionTime': 2, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 64, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1354, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1354
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1289, 'PitInTime': 1291, 'Sector1Time': 21, 'Sector2Time': 2, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1354, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 755019
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 35465, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 13862
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 1, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

