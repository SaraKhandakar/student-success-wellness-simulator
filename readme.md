# Student Success & Wellness Simulator 

**Live Demo:**  
https://sarakhandakar-ueaanoz7ptxgjqhxwromrc.streamlit.app/

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![Status](https://img.shields.io/badge/Deployment-Active-brightgreen)
[![Open App](https://img.shields.io/badge/Launch_App-Streamlit-blue?logo=streamlit)](https://sarakhandakar-ueaanoz7ptxgjqhxwromrc.streamlit.app/)

### App Preview

<img src="https://github.com/SaraKhandakar/student-success-wellness-simulator/blob/main/Student%20simulator.png?raw=true" width="700"/>

A Python + Streamlit app that simulates how daily student habits  
(study hours, sleep, stress, screen time, and attendance) affect  
academic performance and gamified XP levels.

The project includes:
- A **Streamlit web app** for interactive simulation :contentReference[oaicite:1]{index=1}  
- A **Jupyter notebook** with experiments, visualizations, and linear regression modeling
- A **PDF report** documenting methodology, literature support, and insights :contentReference[oaicite:2]{index=2}  

##  Features

- Weighted performance scoring based on:
  - Study hours
  - Sleep duration
  - Attendance
  - Stress levels (negative weight)
  - Screen time (negative weight, with break bonus)
- XP & Level system to gamify good habits
- Multi-session history stored in-memory
- Performance trend chart
- XP progression chart
- Simple feedback messages based on habits
- Notebook version with:
  - Correlation heatmaps
  - Performance trends
  - Linear Regression model to predict performance from habits

##  Tech Stack

- **Language:** Python
- **Frontend / UI:** Streamlit
- **Data / Analysis:** pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **ML Model (in notebook):** Scikit-learn LinearRegression

##  How to Run the Streamlit App Locally

### 1. Clone or download the project

```bash
git clone https://github.com/YOUR_USERNAME/student-success-wellness-simulator.git

cd student-success-wellness-simulator




