# 🏏 Cricket Winning Team and Fantasy Team Predictor using Machine Learning

An end-to-end data analytics and machine learning web application built with Python and Streamlit. This project processes historical cricket statistics to forecast match winners and generate optimized, high-scoring fantasy cricket squads.

---

## 🏗️ Project Architecture & Flowchart

The system follows an automated pipeline from raw historical logs to real-time predictive dashboard rendering:

```text
[ Raw Cricket Datasets (CSV) ]
              │
              ▼
[ Data Cleaning & Preprocessing ] 
  ├── Handling Missing Values (NaN)
  ├── Data Type Casting & Standardization (Team/Player names, Dates)
  └── Categorical Encoding (Label / One-Hot Encoding)
              │
              ▼
[ Feature Engineering ]
  ├── Calculating Rolling Averages & Recent Form
  ├── Venue Win-Loss Percentages & Head-to-Head Stats
  └── Player Performance Index (Strike Rate, Economy, Average)
              │
              ▼
[ Machine Learning Engine ]
  ├── Match Outcome Predictor ➔ Random Forest / Logistic Regression (Classification)
  └── Fantasy Team Generator ➔ Weighted Statistical Scoring & Optimization
              │
              ▼
[ Streamlit UI Dashboard ]
  ├── Interactive Sidebar Controls (Select Teams, Venue, Match Format)
  └── Dynamic Visualizations (Plotly / Matplotlib Charts & Metrics)

```

---

## 🔍 Detailed Project Workflow & Explanation

### 1. Data Cleaning & Preprocessing

Raw cricket telemetry and match logs often contain inconsistencies, missing entries, and unformatted strings. The data cleaning pipeline performs:

* **Missing Value Imputation:** Filters out or imputes incomplete records, abandoned matches, or missing ball-by-ball attributes using statistical averages.
* **Nomenclature Standardization:** Resolves discrepancies in team names, venue titles, and player spellings to maintain data integrity across datasets.
* **Categorical Encoding:** Transforms text attributes (such as venues, batting teams, and bowling teams) into numerical arrays so machine learning algorithms can ingest them effectively.

### 2. Feature Engineering

To give the machine learning models strong predictive signals, custom features are extracted:

* **Head-to-Head Metrics:** Historical win ratios between the two competing teams.
* **Venue Dynamics:** Ground-specific win probabilities (e.g., performance metrics batting first vs. chasing).
* **Player Form Indices:** Recent batting averages, strike rates, economy rates, and wicket-taking consistency.

### 3. Machine Learning Models Used

The system leverages supervised learning split into two primary predictive components:

* **Match Outcome Predictor (Classification):**
* *Algorithms:* **Random Forest Classifier** and **Logistic Regression**.
* *Purpose:* Predicts the probability of victory for competing teams based on historical matchups, venue factors, and team compositions. Random Forest is chosen for its robustness against overfitting and its ability to capture complex, non-linear interactions between pitch conditions and player strengths.


* **Fantasy Team Generator (Scoring & Optimization):**
* *Methodology:* Evaluates individual player stats to project fantasy points.
* *Purpose:* Selects an optimal playing XI that satisfies structural constraints (e.g., maximum player caps per team, balance of wicket-keepers, batters, all-rounders, and bowlers).



### 4. Interactive Dashboard Layer

* Built using **Streamlit**, **Plotly**, and **Matplotlib**.
* Translates complex model outputs into intuitive visual insights, including win probability meters, historical head-to-head breakdown charts, and ranked fantasy squad lists.

---

## 🚀 Key Features

* **Match Outcome Predictor:** Forecasts winning probabilities in real time.
* **Fantasy Team Generator:** Automatically recommends high-value players for fantasy leagues.
* **Interactive Visualizations:** Dynamic data plots exploring venue stats and player form.
* **Responsive UI:** Clean, modern web application layout powered by Streamlit.

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn
* **Data Visualization:** Matplotlib, Plotly, Seaborn
* **Web Framework:** Streamlit

---

## 📂 Project Structure

```text
├── app.py                     # Main Streamlit application runner
├── requirements.txt           # Project dependencies and libraries
├── datasets/                  # Historical cricket match and player CSV files
├── models/                    # Serialized machine learning models (.pkl files)
└── README.md                  # Project documentation

```

---

## ⚙️ Installation & Setup Guide

To run this project locally on your machine, follow these steps:

1. **Clone the Repository:**
```bash
git clone https://github.com/om-rajale/Cricket-winning-team-and-fantacy-team-predictor-using-Machine-Learning.git
cd Cricket-winning-team-and-fantacy-team-predictor-using-Machine-Learning

```


2. **Create and Activate a Virtual Environment:**
* *Windows (PowerShell):*
```powershell
python -m venv venv
venv\Scripts\Activate.ps1

```


* *Mac / Linux:*
```bash
python3 -m venv venv
source venv/bin/activate

```




3. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


4. **Run the Streamlit App:**
```bash
streamlit run app.py

```



---

## 💡 Usage Instructions

1. Open the local URL generated by Streamlit in your browser (typically `http://localhost:8501`).
2. Use the sidebar controls to select your match parameters (Teams, Venue, etc.).
3. View the predicted match winner probabilities and explore the recommended fantasy squad layout.

---

## 👤 Author

* **Om Rajale**
* GitHub: [@om-rajale](https://www.google.com/search?q=https://github.com/om-rajale)
