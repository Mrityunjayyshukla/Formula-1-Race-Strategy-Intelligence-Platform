## 2025 - Round 10 Canadian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1349
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1265, 'PitInTime': 1266, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 3, 'Sector1SessionTime': 23, 'Sector2SessionTime': 2, 'Sector3SessionTime': 3, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 85, 'SpeedST': 2, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1349, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1349
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1265, 'PitInTime': 1266, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 3, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1349, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 805696
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 33604, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 18676
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 167
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 167
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

## 2025 - Round 11 Austrian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1126
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1094, 'PitInTime': 1093, 'Sector1Time': 19, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 20, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 35, 'SpeedST': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1126, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1126
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1094, 'PitInTime': 1093, 'Sector1Time': 19, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1126, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 623839
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 33548, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 13367
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 4, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2025 - Round 12 British Grand Prix (Race)
### Laps - Before
- **Number of rows:** 825
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 91, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 785, 'PitInTime': 789, 'Sector1Time': 21, 'Sector2Time': 3, 'Sector3Time': 3, 'Sector1SessionTime': 23, 'Sector2SessionTime': 3, 'Sector3SessionTime': 3, 'SpeedI1': 3, 'SpeedI2': 3, 'SpeedFL': 39, 'SpeedST': 3, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 825, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 825
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 91, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 785, 'PitInTime': 789, 'Sector1Time': 21, 'Sector2Time': 3, 'Sector3Time': 3, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 825, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 709412
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 36838, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 24292
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 5, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2025 - Round 13 Belgian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 879
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 60, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 833, 'PitInTime': 853, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 20, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 26, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 75, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 879, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 879
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 60, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 833, 'PitInTime': 853, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 879, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 780371
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 34489, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 16177
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 223
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 223
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

## 2025 - Round 14 Hungarian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1368
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1338, 'PitInTime': 1338, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 20, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 30, 'SpeedST': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1368, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1368
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1338, 'PitInTime': 1338, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1368, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 856901
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 38763, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 19565
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 1, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2025 - Round 15 Dutch Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1364
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1324, 'PitInTime': 1324, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 25, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 42, 'SpeedST': 3, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1364, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1364
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1324, 'PitInTime': 1324, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1364, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 838756
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 41310, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 22538
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

## 2025 - Round 16 Italian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 974
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 953, 'PitInTime': 954, 'Sector1Time': 19, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 21, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 20, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 974, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 974
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 953, 'PitInTime': 954, 'Sector1Time': 19, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 974, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 618625
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 29929, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 6404, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 8136
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

## 2025 - Round 17 Azerbaijan Grand Prix (Race)
### Laps - Before
- **Number of rows:** 968
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 58, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 947, 'PitInTime': 947, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 21, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 22, 'SpeedST': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 968, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 968
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 58, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 947, 'PitInTime': 947, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 968, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 804780
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 41026, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 21429
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

## 2025 - Round 18 Singapore Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1229
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1204, 'PitInTime': 1206, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 25, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 23, 'SpeedST': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1229, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1229
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1204, 'PitInTime': 1206, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1229, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 916489
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 43222, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 24563
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 0, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2025 - Round 19 United States Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1067
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1046, 'PitInTime': 1046, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 22, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 22, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1067, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1067
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1046, 'PitInTime': 1046, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1067, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 818828
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 41730, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 20553
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 1, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2025 - Round 1 Australian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 927
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 69, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 843, 'PitInTime': 845, 'Sector1Time': 23, 'Sector2Time': 6, 'Sector3Time': 7, 'Sector1SessionTime': 24, 'Sector2SessionTime': 6, 'Sector3SessionTime': 7, 'SpeedI1': 6, 'SpeedI2': 6, 'SpeedFL': 88, 'SpeedST': 6, 'IsPersonalBest': 3, 'Compound': 0, 'TyreLife': 5, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 6, 'Deleted': 927, 'DeletedReason': 3, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 927
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 69, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 843, 'PitInTime': 845, 'Sector1Time': 23, 'Sector2Time': 6, 'Sector3Time': 7, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 6, 'Deleted': 927, 'DeletedReason': 3, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 754313
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 38826, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 862, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 27236
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 178
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 178
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

## 2025 - Round 20 Mexico City Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1263
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1236, 'PitInTime': 1233, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 24, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 31, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1263, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1263
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1236, 'PitInTime': 1233, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1263, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 795340
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 43489, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 25278
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 4, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2025 - Round 21 São Paulo Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1251
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1212, 'PitInTime': 1213, 'Sector1Time': 21, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 27, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 40, 'SpeedST': 4, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1251, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1251
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1212, 'PitInTime': 1213, 'Sector1Time': 21, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1251, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 743882
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 37645, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 20823
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 3, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2025 - Round 22 Las Vegas Grand Prix (Race)
### Laps - Before
- **Number of rows:** 886
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 862, 'PitInTime': 861, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 20, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 886, 'SpeedFL': 26, 'SpeedST': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 886, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 886
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 862, 'PitInTime': 861, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 886, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 664519
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 36222, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 13393
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 141
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 141
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

## 2025 - Round 23 Qatar Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1067
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1025, 'PitInTime': 1023, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 24, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 45, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1067, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1067
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1025, 'PitInTime': 1023, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1067, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 721682
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 32891, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 12344
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 149
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 149
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

## 2025 - Round 24 Abu Dhabi Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1156
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1129, 'PitInTime': 1129, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 22, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 27, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1156, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1156
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1129, 'PitInTime': 1129, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1156, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 784424
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 36821, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 15351
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

## 2025 - Round 2 Chinese Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1065
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1039, 'PitInTime': 1039, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 23, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 26, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1065, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1065
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1039, 'PitInTime': 1039, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1065, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 787702
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 37865, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 19345
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 4, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2025 - Round 3 Japanese Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1059
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1038, 'PitInTime': 1038, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 26, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 21, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1059, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1059
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1038, 'PitInTime': 1038, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1059, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 749686
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 34933, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 11763
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 140
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 140
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

## 2025 - Round 4 Bahrain Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1128
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 13, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1086, 'PitInTime': 1085, 'Sector1Time': 40, 'Sector2Time': 20, 'Sector3Time': 20, 'Sector1SessionTime': 44, 'Sector2SessionTime': 20, 'Sector3SessionTime': 20, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 43, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1128, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1128
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 13, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1086, 'PitInTime': 1085, 'Sector1Time': 40, 'Sector2Time': 20, 'Sector3Time': 20, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1128, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 864112
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 40221, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 20547
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 2, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2025 - Round 5 Saudi Arabian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 898
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 37, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 879, 'PitInTime': 878, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 23, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 21, 'SpeedST': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 898, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 898
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 37, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 879, 'PitInTime': 878, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 898, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 669956
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 35072, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 12193
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 142
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 142
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

## 2025 - Round 6 Miami Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1005
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 354, 'PitOutTime': 986, 'PitInTime': 986, 'Sector1Time': 22, 'Sector2Time': 3, 'Sector3Time': 3, 'Sector1SessionTime': 27, 'Sector2SessionTime': 3, 'Sector3SessionTime': 3, 'SpeedI1': 3, 'SpeedI2': 3, 'SpeedFL': 22, 'SpeedST': 3, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 354, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 1005, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1005
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 986, 'PitInTime': 986, 'Sector1Time': 22, 'Sector2Time': 3, 'Sector3Time': 3, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 1005, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 720945
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 36741, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 19229
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 149
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 149
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

## 2025 - Round 7 Emilia Romagna Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1207
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1169, 'PitInTime': 1170, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 26, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 39, 'SpeedST': 2, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1207, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1207
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1169, 'PitInTime': 1170, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1207, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 794153
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 37055, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 17790
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

## 2025 - Round 8 Monaco Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1425
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1385, 'PitInTime': 1384, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 2, 'Sector1SessionTime': 23, 'Sector2SessionTime': 1, 'Sector3SessionTime': 2, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 42, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1425, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1425
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1385, 'PitInTime': 1384, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1425, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 850320
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 41615, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 31274
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

## 2025 - Round 9 Spanish Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1203
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1148, 'PitInTime': 1148, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 21, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 56, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1203, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1203
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1148, 'PitInTime': 1148, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1203, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 770282
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 37290, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 18981
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 2, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

