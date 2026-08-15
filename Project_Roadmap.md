# **Formula 1 - Race Strategy Intelligence Platform**

**Project Goal:** Analyse how race strategy, tire management, pit stops, weather, track characteristics, and driver performance impact race outcomes, and build a model that predicts race finishing position and optimal pit strategy.

### **Project Showcase**
* Data Engineering
* ETL Pipelines
* Data Warehousing
* Exploratory Data Analysis
* Feature Engineering
* Advanced Visualizations
* Predictive Modelling
* Dashboard Development
* MLOps Concepts

## **Phase 1: Project Architecture**
1. Fast F1 API (Python): Lap Data, Telemetry, Weather, Pit stops, Sector Times, Race Results.
2. **Architecture**: FastF1 API -> Data Ingestion -> Raw Data Lake -> Data Cleaning -> Feature Engineering -> Analytics Warehouse -> Visualization layer -> Machine learning models -> PowerBI/Streamlit Dashboard
3. **Tech Stack**: Python (FastF1, NumPy, matplotlib, Pandas, Seaborn, Plotly, Sci-kit learn, XGBoost, Streamlit), SQL (MySQL, PostgreSQL), Docker

## **Phase 2: Data Ingestion**
**Extract Data:** Seasons 2022-2025 - All races<br>
**Tables:** Races, Laps, Telemetry, Weather, Pit Stops, Qualifying, Drivers, Constructors<br>
**Skills:** API Ingestion, Data collection automation, Batch processing.

## **Phase 3: Data Cleaning**
**Common Issues:** Missing telemetry; Missing Weather Record, Missing Sector Times<br>
**Methods:** Forward fill, Interpolation, Remove corrupted laps.<br>
**Column Standardization:**
1. Driver Name - "HAM/Hamilton" to "Lewis Hamilton".
2. Lap Times - to seconds
3. Date - Datetime format
4. Speeds - float

**Remove Invalid Records:** Red flagged laps; Incomplete laps; Retired Drivers

## **Phase 4: Data Modelling**
Create Star Schema
**Fact Tables**
1. **Fact laps:** Lap\_ID, Race\_ID, Driver\_ID, Lap\_Time, Tyre, Stints
2. **Fact Telemetry:** Speed, Throttle, Brake, Gear
3. **Fact Results:** Finishing Position, Points
4. **Dimension:** Dim\_Driver, Dim\_Track, Dim\_race, Dim\_weather, Dim\_constructor

## **Phase 5: Feature Engineering**
1. **Driver Features:** Average Race pace, Average lap time, Overtake Rate
2. **Tyre Features:** Tyre Compound, Tyre Age, Tyre Degradation, Pace drop per lap.
3. **Pit Stop Features:** Number of Stops, Average Pit Duration, First and Final Stop lap.
4. **Track Features:** Circuit Length, Number of Corners, Average Speed, Track Temperature
5. **Weather Features:** Air Temperature, Rainfall Indicator, Humidity, Wind Speed
6. **Race Features:** Safety Car Laps, Race Distance, Starting Position, Grid Penalties
7. **Advanced Features:** Undercut Success Score, Overcut Success Score, Driver Aggression Index

## **Phase 6: Exploratory Data Analysis**
### **Visualization 1**
**Name:** Lap Time Distribution<br>
**Purpose:** Understand pace spread<br>
**Chart:** Histogram, KDE

### **Visualization 2**
**Name:** Driver pace comparison<br>
**Compare:** The drivers<br>
**Chart:** Box plot

### **Visualization 3**
**Name:** Tyre Degradation Curves<br>
**Chart:** Line plot (x = tyre age, y = lap time)

### **Visualization 4**
**Name:** Pit Stop Impact<br>
**Chart:** Scatter plot (x = pit stop lap, y = finishing position)

### **Visualization 5**
**Name:** Weather vs Lap Time<br>
**Chart:** Heatmap

### **Visualization 6**
**Name:** Track Speed Map using telemetry<br>
**Chart:** Circuit coloured by speed

### **Visualization 7**
**Name:** Sector Performance<br>
**Chart:** Radar Chart

### **Visualization 8**
**Name:** Overtaking Analysis<br>
**Chart:** Sankey Diagram

### **Visualization 9**
**Name:** Pit Strategy Comparison<br>
**Chart:** Gantt Chart

### **Visualization 10**
**Name:** Race Position Changes<br>
**Chart:** Position Evolution Plot

## **Phase 7: Advanced Analytics**
Answering the questions based on the analysis that has been performed on the data to get the insights.<br>
**Analysis 1:** Which tyre strategy wins most races?<br>
**Analysis 2:** Which circuits favour aggressive strategies?<br>
**Analysis 3:** Which drivers preserve tyres best?<br>
**Analysis 4:** Pit stop timing effectiveness<br>
**Analysis 5:** Weather impact on performance<br>
**Analysis 6:** Undercut effectiveness analysis<br>
**Analysis 7:** Constructor strategy comparison<br>

## **Phase 8: Machine Learning**
### **Model 1: Finishing Position Prediction**
**Target:** Finishing Position<br>
**Features:** Grid Position, Pace, Weather, Tyre Age, Pit Strategy<br>
**Models:** Random Forest, XGBoost<br>
**Metrics:** MAE, RMSE<br>

### **Model 2: Podium Prediction**
**Target:** 1 if podium else 0<br>
**Models:** XGBoost, LightGBM<br>
**Metrics:** F1 Score, ROC-AUC<br>

### **Model 3: Optimal Pit Stop Recommendation**
**Target**: Best lap for pit stop<br>
**Models**: Regression or Optimization Model

## **Phase 9: Dashboard (Streamlit)**
**Building Streamlit Dashboard**
1. **Page 1 (Race Overview):** Winner, Weather, Strategy Summary
2. **Page 2 (Driver Analytics):** Pace, Tyre Degradation, Consistency
3. **Page 3 (Strategy Analysis):** Pit Stops, Stints, Undercuts
4. **Page 4 (Telemetry Explorer):** Speed, Brake, Throttle
5. **Page 5 (ML Predictions):** Predicted finishing order, Podium Probability
