# 🏏 IPL Six Predictor – Streamlit App

A Streamlit app that predicts the **probability of a six being hit in the first two overs** of an IPL match based on selected teams. It uses a Logistic Regression model trained on IPL 2024 data.

---

## 📊 Features

- Select **Home Team** and **Opponent Team**
- Get **probability of a six** in early overs
- Simple and interactive UI using Streamlit
- Trains model on match data automatically

---

## 🧠 How It Works

- Loads data from `IPL24_All_Matches_Dataset.xlsx`
- Encodes team names with `LabelEncoder`
- Trains a `LogisticRegression` model
- Predicts probability using team matchup

---

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/chaitanya5469/iplsixprediction.git
cd iplsixprediction
```

### 2. Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🌐 Deploy Online

### ✅ [Streamlit Cloud](https://streamlit.io/cloud)

1. Push your code to GitHub
2. Log in to Streamlit Cloud
3. Select your repo → Click “Deploy”

---

## 📁 Folder Structure

```
📦 iplsixprediction/
├── app.py
├── IPL24_All_Matches_Dataset.xlsx
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📦 Recommended .gitignore

```
.venv/
__pycache__/
*.pkl
*.pyc
```

To remove `.venv` from Git:

```bash
git rm -r --cached .venv
echo ".venv/" >> .gitignore
git commit -am "Removed .venv and updated .gitignore"
git push origin main
```

---

## 👤 Author

Made by [Chaitanya Krishna](https://github.com/chaitanya5469)

