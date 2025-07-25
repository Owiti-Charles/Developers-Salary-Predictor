# 💼 Developer Salary Prediction: Stack Overflow Survey 2023–2024

# 👥 Authors
  - Makena Odongo
  - Paul Otuoro
  - Viola Kimitei
  - Charles Owiti
  - Austine Otieno


## 📖 Project Overview
This project builds a machine learning model to predict annual developer salaries using data from the Stack Overflow Developer Surveys (2023 and 2024). By leveraging demographic, professional, and technical features, the model provides data-driven salary benchmarks for developers, employers, and HR platforms, with a special focus on Kenya’s growing tech ecosystem.

---

## 🎯 Objectives

- **Empower Developers:** Help developers benchmark salaries for better negotiation.
- **Support Employers:** Enable competitive, fair salary offerings.
- **Enhance HR Platforms:** Integrate salary predictions into job boards like Fuzu or BrighterMonday.
- **Inform Policy:** Provide insights into tech labor market trends, especially in Kenya.

---

## 🌍 Why It Matters
Salary transparency is limited, particularly in regions like Africa. This model addresses this gap by offering reliable salary predictions, supporting career decisions, and fostering fair compensation practices in Nairobi’s tech hub and beyond.

---

## 📊 Data

The dataset comprises responses from the Stack Overflow Developer Surveys:

- **2023:** ~89,000 responses, 244 from Kenya  
- **2024:** ~65,000 responses, 180 from Kenya  
- **Total:** Over 100,000 responses across 188 countries  
- **Source:** [Stack Overflow Developer Survey](https://insights.stackoverflow.com/survey)

### Key Features

- **Demographics:** Country, age, gender  
- **Professional:** Years of coding experience, job type, organization size  
- **Technical:** Programming languages, platforms, tools  
- **Target:** Annual salary in USD (`ConvertedCompYearly`, log-transformed)

### Data Limitations

- Schema differences between years (mitigated by aligning common columns)
- Sparse data Sub-Saharan regions like Kenyan (addressed with global model and feature engineering)
- Salary outliers (handled via log transformation and IQR filtering)

---

## 🛠️ Installation

To reproduce this project, follow these steps:

### Prerequisites

- Python 3.10.18  
- Git  
- Jupyter Notebook  

## 📦 Requirements

Key packages include:

- `pandas`, `numpy` — data manipulation  
- `scikit-learn`, `xgboost`, `lightgbm`, 'TensorFlow` — modeling  
- `shap` — model interpretability  
- `matplotlib`, `seaborn` — visualizations

---

# 📈 Results

## 💡 Model Performance

The optimized **LightGBM** model achieved:

- **RMSE**: `0.46` (predictions within ±50% of actual salary)
- **R² Score**: `0.62` (explains 62% of salary variation)
- **Validation**: 20% holdout set + 5-fold cross-validation

| Model               | RMSE   | R² Score | Use Case               |
|--------------------|--------|----------|------------------------|
| Linear Regression   | 0.4766 | 0.5945   | Baseline               |
| Random Forest       | 0.4752 | 0.5969   | Balanced Performance   |
| XGBoost             | 0.4717 | 0.6027   | Strong Single Model    |
| **LightGBM (Opt.)** | **0.4619** | **0.6192** | **Production Choice**   |
| Stacking Ensemble   | 0.4620 | 0.6189   | Marginal Gains         |
|Neural Network   | 0.4715   | 0.603043   | Needs tuning          |
---

## 🧠 Key Insights

### 🔝 Top Salary Drivers:
- `YearsCodePro`: Professional coding experience.
- `NumLanguages`: Number of programming languages known.
- `EdLevel_Encoded`: Education level.
- `Region`: High-income regions boost salaries.

### 📊 Visualizations:
- **SHAP Summary Plot**: Shows how each feature influences predictions.
- **Feature Importance Plot**: Highlights the most predictive variables.
- **Actual vs. Predicted Plot**: Demonstrates model accuracy.

---

# 💼 Business Applications

### 👩‍💻 Developers
- Negotiate salaries with **data-backed benchmarks**.

### 🏢 Employers
- Offer **competitive pay** to attract and retain talent.

### 📊 HR Platforms
- Integrate predictive models into **job board features**.

### 🏛️ Policy Makers
- Inform **tech labor policies** in Kenya and Sub-Saharan Africa.

---

# 🔮 Future Improvements

- Incorporate **cost-of-living indices** for regionally adjusted predictions.
- Explore further with **neural networks** for deeper pattern detection.
- Enrich Kenya-specific data using **local job board APIs**.
- Test **additional ensemble models** for marginal performance gains.

---

# 🙏 Acknowledgments

Stack Overflow for open-access developer survey data.
Open-source libraries used:
- pandas
- scikit-learn
- xgboost
- lightgbm
- shap

Inspired by global developer insights from:
- GitHub Octoverse
- HackerRank Developer Reports
