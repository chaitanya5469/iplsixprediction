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

# Get six-hit details in first 2 overs
def get_six_details(df, home_team, other_team):
    six_df = df[(df['runs'] == 6) & (df['over'] <= 2)]

    # Filter by both teams
    filtered = six_df[six_df['match'].str.contains(f"{home_team} vs {other_team}|{other_team} vs {home_team}", na=False)]

    return filtered[['match', 'batsmanName', 'bowlerName', 'over']].drop_duplicates()

# Streamlit app
st.set_page_config(page_title="IPL Six Predictor", page_icon="🏏")
st.title("🏏 IPL Six Predictor")
st.caption("Predicts probability of a six in the first two overs based on team matchups")

# Load everything
df = load_data()
model, encoder = train_model(df)

# Team selection
teams = sorted(list(set(df['match'].str.split(' vs ').str[0]) | set(df['match'].str.split(' vs ').str[1])))

home_team = st.selectbox("Select Home Team", teams)
other_team = st.selectbox("Select Opponent Team", teams)

if st.button("Predict"):
    try:
        # Encode
        home_encoded = encoder.transform([home_team])[0]
        other_encoded = encoder.transform([other_team])[0]
        input_data = [[home_encoded, other_encoded]]
        
        # Predict
        probability = model.predict_proba(input_data)[0][1]*10
        st.success(f"💥 Probability of a six in first 2 overs: **{probability:%}**")

        # Show detailed data
        st.markdown("### 🧾 Sixes Hit in First 2 Overs (Historical Matches)")
        details = get_six_details(df, home_team, other_team)

        if not details.empty:
            st.dataframe(details)
        else:
            st.info("No sixes found in the first 2 overs for this matchup.")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
