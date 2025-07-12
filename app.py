import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

# Load data
@st.cache_data
def load_data():
    file_path = "IPL24_All_Matches_Dataset.xlsx"
    return pd.read_excel(file_path, sheet_name="Sheet1")

# Train model
@st.cache_resource
def train_model(df):
    encoder = LabelEncoder()
    df['home_team_encoded'] = encoder.fit_transform(df['match'].str.split(' vs ').str[0])
    df['other_team_encoded'] = encoder.fit_transform(df['match'].str.split(' vs ').str[1])
    df['hit_six'] = (df['runs'] == 6).astype(int)

    X = df[['home_team_encoded', 'other_team_encoded']]
    y = df['hit_six']

    model = LogisticRegression()
    model.fit(X, y)

    return model, encoder

# Load and train
df = load_data()
model, encoder = train_model(df)

# --------------------- UI ---------------------
st.set_page_config(page_title="IPL Six Predictor", page_icon="🏏")
st.title("🏏 IPL Six Predictor")
st.caption("Predicts probability of a six in early overs based on team matchup")

teams = list(set(df['match'].str.split(' vs ').str[0]) | set(df['match'].str.split(' vs ').str[1]))
teams.sort()

home_team = st.selectbox("Select Home Team", teams)
other_team = st.selectbox("Select Opponent Team", teams)

if st.button("Predict"):
    try:
        home_encoded = encoder.transform([home_team])[0]
        other_encoded = encoder.transform([other_team])[0]
        input_data = [[home_encoded, other_encoded]]
        probability = model.predict_proba(input_data)[0][1]*10
        st.success(f"💥 Probability of a six in first 2 overs: **{probability:.2%}**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
