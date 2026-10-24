## 2022 - Round 10 British Grand Prix (Race)
### Laps - Before
- **Number of rows:** 815
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 42, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 768, 'PitInTime': 766, 'Sector1Time': 38, 'Sector2Time': 11, 'Sector3Time': 10, 'Sector1SessionTime': 40, 'Sector2SessionTime': 11, 'Sector3SessionTime': 10, 'SpeedI1': 4, 'SpeedI2': 4, 'SpeedFL': 53, 'SpeedST': 4, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 4, 'Deleted': 815, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 815
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 42, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 768, 'PitInTime': 766, 'Sector1Time': 38, 'Sector2Time': 11, 'Sector3Time': 10, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 4, 'Deleted': 815, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 631680
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 30445, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 46903
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 203
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 203
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

## 2022 - Round 11 Austrian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1324
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1281, 'PitInTime': 1280, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 30, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 45, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 359, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1324, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1324
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1281, 'PitInTime': 1280, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1324, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 722315
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 32821, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 12723
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 15, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2022 - Round 12 French Grand Prix (Race)
### Laps - Before
- **Number of rows:** 958
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 13, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 933, 'PitInTime': 930, 'Sector1Time': 23, 'Sector2Time': 3, 'Sector3Time': 5, 'Sector1SessionTime': 25, 'Sector2SessionTime': 3, 'Sector3SessionTime': 5, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 30, 'SpeedST': 2, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 958, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 958
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 13, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 933, 'PitInTime': 930, 'Sector1Time': 23, 'Sector2Time': 3, 'Sector3Time': 5, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 958, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 746000
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 36623, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 18152
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 128
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 128
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

## 2022 - Round 13 Hungarian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1383
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1340, 'PitInTime': 1341, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 23, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 43, 'SpeedST': 2, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1383, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1383
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1340, 'PitInTime': 1341, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1383, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 902680
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 38423, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 22667
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 13, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2022 - Round 14 Belgian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 792
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 40, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 752, 'PitInTime': 754, 'Sector1Time': 21, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 23, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 40, 'SpeedST': 2, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 792, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 792
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 40, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 752, 'PitInTime': 754, 'Sector1Time': 21, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 792, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 715967
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 34784, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 16453
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 5, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2022 - Round 15 Dutch Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1392
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 4, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1321, 'PitInTime': 1320, 'Sector1Time': 22, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 26, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 73, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1392, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1392
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 4, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1321, 'PitInTime': 1320, 'Sector1Time': 22, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1392, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 854389
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 37650, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 21045
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 163
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 163
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

## 2022 - Round 16 Italian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 971
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 943, 'PitInTime': 941, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 24, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 32, 'SpeedST': 2, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 971, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 971
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 943, 'PitInTime': 941, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 971, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 672089
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 33306, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 12184
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 8, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2022 - Round 17 Singapore Grand Prix (Race)
### Laps - Before
- **Number of rows:** 945
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 108, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 923, 'PitInTime': 922, 'Sector1Time': 24, 'Sector2Time': 4, 'Sector3Time': 4, 'Sector1SessionTime': 25, 'Sector2SessionTime': 4, 'Sector3SessionTime': 4, 'SpeedI1': 4, 'SpeedI2': 4, 'SpeedFL': 27, 'SpeedST': 5, 'IsPersonalBest': 4, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 4, 'Deleted': 945, 'DeletedReason': 4, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 945
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 108, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 923, 'PitInTime': 922, 'Sector1Time': 24, 'Sector2Time': 4, 'Sector3Time': 4, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 4, 'Deleted': 945, 'DeletedReason': 4, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 903558
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 36189, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 43767
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 255
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 255
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

## 2022 - Round 18 Japanese Grand Prix (Race)
### Laps - Before
- **Number of rows:** 507
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 75, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 464, 'PitInTime': 465, 'Sector1Time': 39, 'Sector2Time': 3, 'Sector3Time': 3, 'Sector1SessionTime': 40, 'Sector2SessionTime': 3, 'Sector3SessionTime': 3, 'SpeedI1': 3, 'SpeedI2': 3, 'SpeedFL': 45, 'SpeedST': 3, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 507, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 507
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 75, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 464, 'PitInTime': 465, 'Sector1Time': 39, 'Sector2Time': 3, 'Sector3Time': 3, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 507, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 467460
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 19809, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 23590, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 90562
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 255
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 255
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

## 2022 - Round 19 United States Grand Prix (Race)
### Laps - Before
- **Number of rows:** 992
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 74, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 955, 'PitInTime': 955, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 22, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 39, 'SpeedST': 2, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 992, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 992
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 74, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 955, 'PitInTime': 955, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 992, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 832615
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 35755, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 26302
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 170
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 170
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

## 2022 - Round 1 Bahrain Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1125
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 7, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1067, 'PitInTime': 1066, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 24, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 61, 'SpeedST': 2, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1125, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1125
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 7, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1067, 'PitInTime': 1066, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1125, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 876280
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 38061, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 22840
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 163
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 163
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

## 2022 - Round 20 Mexico City Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1379
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1356, 'PitInTime': 1355, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 27, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 25, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1379, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1379
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 1, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1356, 'PitInTime': 1355, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1379, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 889726
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 42979, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 24959
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 14, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2022 - Round 21 São Paulo Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1259
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1214, 'PitInTime': 1215, 'Sector1Time': 21, 'Sector2Time': 3, 'Sector3Time': 3, 'Sector1SessionTime': 26, 'Sector2SessionTime': 3, 'Sector3SessionTime': 3, 'SpeedI1': 3, 'SpeedI2': 3, 'SpeedFL': 46, 'SpeedST': 4, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 1259, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1259
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 3, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1214, 'PitInTime': 1215, 'Sector1Time': 21, 'Sector2Time': 3, 'Sector3Time': 3, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 1259, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 798745
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 39765, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 24555
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 4, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2022 - Round 22 Abu Dhabi Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1117
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1086, 'PitInTime': 1083, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 25, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 34, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1117, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1117
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1086, 'PitInTime': 1083, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1117, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 784332
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 37886, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 16255
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 9, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2022 - Round 2 Saudi Arabian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 820
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 48, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 801, 'PitInTime': 799, 'Sector1Time': 21, 'Sector2Time': 3, 'Sector3Time': 4, 'Sector1SessionTime': 21, 'Sector2SessionTime': 3, 'Sector3SessionTime': 4, 'SpeedI1': 3, 'SpeedI2': 3, 'SpeedFL': 24, 'SpeedST': 3, 'IsPersonalBest': 3, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 820, 'DeletedReason': 3, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 820
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 48, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 801, 'PitInTime': 799, 'Sector1Time': 21, 'Sector2Time': 3, 'Sector3Time': 4, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 820, 'DeletedReason': 3, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 643722
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 34957, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 13597
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 1, 'GridPosition': 1, 'Time': 8, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2022 - Round 3 Australian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1045
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 19, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1023, 'PitInTime': 1023, 'Sector1Time': 23, 'Sector2Time': 3, 'Sector3Time': 3, 'Sector1SessionTime': 25, 'Sector2SessionTime': 3, 'Sector3SessionTime': 3, 'SpeedI1': 3, 'SpeedI2': 3, 'SpeedFL': 25, 'SpeedST': 3, 'IsPersonalBest': 3, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 1045, 'DeletedReason': 3, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1045
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 19, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1023, 'PitInTime': 1023, 'Sector1Time': 23, 'Sector2Time': 3, 'Sector3Time': 3, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 3, 'Deleted': 1045, 'DeletedReason': 3, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 731534
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 39270, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 16865
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 8, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2022 - Round 4 Emilia Romagna Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1132
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 6, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1106, 'PitInTime': 1106, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 1, 'Sector1SessionTime': 21, 'Sector2SessionTime': 1, 'Sector3SessionTime': 1, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 27, 'SpeedST': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1132, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1132
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 6, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1106, 'PitInTime': 1106, 'Sector1Time': 20, 'Sector2Time': 1, 'Sector3Time': 1, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1132, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 774770
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 40759, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 18136
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 11, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2022 - Round 5 Miami Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1057
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 35, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1030, 'PitInTime': 1028, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 2, 'Sector1SessionTime': 29, 'Sector2SessionTime': 1, 'Sector3SessionTime': 2, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 30, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1057, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1057
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 35, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1030, 'PitInTime': 1028, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1057, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 795472
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 37903, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 786, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 22511
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 5, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2022 - Round 6 Spanish Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1230
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1177, 'PitInTime': 1175, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'Sector1SessionTime': 20, 'Sector2SessionTime': 0, 'Sector3SessionTime': 0, 'SpeedI1': 0, 'SpeedI2': 0, 'SpeedFL': 55, 'SpeedST': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1230, 'DeletedReason': 0, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1230
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 0, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1177, 'PitInTime': 1175, 'Sector1Time': 20, 'Sector2Time': 0, 'Sector3Time': 0, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 0, 'Deleted': 1230, 'DeletedReason': 0, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 849050
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 40399, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 21697
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 12, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2022 - Round 7 Monaco Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1179
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 26, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1106, 'PitInTime': 1124, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 21, 'Sector1SessionTime': 21, 'Sector2SessionTime': 1, 'Sector3SessionTime': 21, 'SpeedI1': 1, 'SpeedI2': 1, 'SpeedFL': 56, 'SpeedST': 1, 'IsPersonalBest': 1, 'Compound': 0, 'TyreLife': 161, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1179, 'DeletedReason': 1, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1179
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 26, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1106, 'PitInTime': 1124, 'Sector1Time': 21, 'Sector2Time': 1, 'Sector3Time': 21, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 1, 'Deleted': 1179, 'DeletedReason': 1, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 991051
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 36806, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 48744
- **Number of columns:** 18
- **Columns:** ['Date', 'Speed', 'RPM', 'Throttle', 'X', 'Y', 'Z', 'nGear', 'DRS', 'Brake', 'SessionTime', 'DriverAhead', 'Time', 'Source', 'Distance', 'Status', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'Speed': 0, 'RPM': 0, 'Throttle': 0, 'X': 0, 'Y': 0, 'Z': 0, 'nGear': 0, 'DRS': 0, 'Brake': 0, 'SessionTime': 0, 'DriverAhead': 0, 'Time': 0, 'Source': 0, 'Distance': 0, 'Status': 0, 'Driver': 0, 'LapNumber': 0}

### Weather - Before
- **Number of rows:** 245
- **Number of columns:** 8
- **Columns:** ['Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'AirTemp': 0, 'Humidity': 0, 'Pressure': 0, 'Rainfall': 0, 'TrackTemp': 0, 'WindDirection': 0, 'WindSpeed': 0}

### Weather - After
- **Number of rows:** 245
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

## 2022 - Round 8 Azerbaijan Grand Prix (Race)
### Laps - Before
- **Number of rows:** 891
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 19, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 864, 'PitInTime': 861, 'Sector1Time': 23, 'Sector2Time': 3, 'Sector3Time': 3, 'Sector1SessionTime': 25, 'Sector2SessionTime': 3, 'Sector3SessionTime': 3, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 32, 'SpeedST': 2, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 891, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 891
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 19, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 864, 'PitInTime': 861, 'Sector1Time': 23, 'Sector2Time': 3, 'Sector3Time': 3, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 891, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 760406
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 39303, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 22380
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 10, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

## 2022 - Round 9 Canadian Grand Prix (Race)
### Laps - Before
- **Number of rows:** 1264
- **Number of columns:** 31
- **Columns:** ['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime', 'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'FastF1Generated', 'IsAccurate']
- **Duplicated Values:** 0
- **Null Values:** {'Time': 0, 'Driver': 0, 'DriverNumber': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1233, 'PitInTime': 1232, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'Sector1SessionTime': 25, 'Sector2SessionTime': 2, 'Sector3SessionTime': 2, 'SpeedI1': 2, 'SpeedI2': 2, 'SpeedFL': 34, 'SpeedST': 2, 'IsPersonalBest': 2, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'LapStartTime': 0, 'LapStartDate': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1264, 'DeletedReason': 2, 'FastF1Generated': 0, 'IsAccurate': 0}

### Laps - After
- **Number of rows:** 1264
- **Number of columns:** 25
- **Columns:** ['Driver', 'LapTime', 'LapNumber', 'Stint', 'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre', 'Team', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason', 'IsAccurate', 'MissingSector1', 'MissingSector2', 'MissingSector3', 'IsInLap', 'IsOutLap', 'TrackData']
- **Duplicated Values:** 0
- **Null Values:** {'Driver': 0, 'LapTime': 2, 'LapNumber': 0, 'Stint': 0, 'PitOutTime': 1233, 'PitInTime': 1232, 'Sector1Time': 22, 'Sector2Time': 2, 'Sector3Time': 2, 'IsPersonalBest': 0, 'Compound': 0, 'TyreLife': 0, 'FreshTyre': 0, 'Team': 0, 'TrackStatus': 0, 'Position': 2, 'Deleted': 1264, 'DeletedReason': 2, 'IsAccurate': 0, 'MissingSector1': 0, 'MissingSector2': 0, 'MissingSector3': 0, 'IsInLap': 0, 'IsOutLap': 0, 'TrackData': 0}

### Telemetry - Before
- **Number of rows:** 792170
- **Number of columns:** 20
- **Columns:** ['Date', 'SessionTime', 'DriverAhead', 'DistanceToDriverAhead', 'Time', 'RPM', 'Speed', 'nGear', 'Throttle', 'Brake', 'DRS', 'Source', 'Distance', 'RelativeDistance', 'Status', 'X', 'Y', 'Z', 'Driver', 'LapNumber']
- **Duplicated Values:** 0
- **Null Values:** {'Date': 0, 'SessionTime': 0, 'DriverAhead': 0, 'DistanceToDriverAhead': 39059, 'Time': 0, 'RPM': 0, 'Speed': 0, 'nGear': 0, 'Throttle': 0, 'Brake': 0, 'DRS': 0, 'Source': 0, 'Distance': 0, 'RelativeDistance': 0, 'Status': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Driver': 0, 'LapNumber': 0}

### Telemetry - After
- **Number of rows:** 22190
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
- **Null Values:** {'DriverNumber': 0, 'DriverId': 0, 'TeamName': 0, 'TeamColor': 0, 'TeamId': 0, 'FullName': 0, 'Position': 0, 'GridPosition': 0, 'Time': 3, 'Status': 0, 'Points': 0, 'Laps': 0, 'RaceOutcome': 0}

