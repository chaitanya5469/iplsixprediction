from flask import Flask, request, jsonify, render_template
import pandas as pd
import logging
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the dataset
file_path = "IPL24_All_Matches_Dataset.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")


# Preprocess Data for ML
encoder = LabelEncoder()

df['home_team_encoded'] = encoder.fit_transform(df['match'].str.split(' vs ').str[0])
df['other_team_encoded'] = encoder.fit_transform(df['match'].str.split(' vs ').str[1])
df['hit_six'] = (df['runs'] == 6).astype(int)

# Select relevant features
X = df[['home_team_encoded', 'other_team_encoded']]
y = df['hit_six']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
with open('six_prediction_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Load model
def load_model():
    with open('six_prediction_model.pkl', 'rb') as f:
        return pickle.load(f)

ml_model = load_model()

def predict_six_probability(home_team, other_team):
    try:
        home_encoded = encoder.transform([home_team])[0]
        if other_team:
            other_encoded = encoder.transform([other_team])[0]
        else:
            other_encoded = None
      

        input_data = [[home_encoded, other_encoded if other_encoded is not None else 0]]
        probability = ml_model.predict_proba(input_data)[0][1]
        return probability
    except Exception as e:
        logging.error(f"Error in prediction: {e}")
        return {"error": "Prediction error."}

def get_six_details(home_team, other_team=None):
    try:
        # Filter deliveries where a six was hit in the first two overs
        six_df = df[(df['runs'] == 6) & (df['over'] <= 2)]
        
        if other_team:
            # Matches involving the selected two teams
            match_df = six_df[six_df['match'].str.contains(f"{home_team} vs {other_team}|{other_team} vs {home_team}", na=False)]
        else:
            # Matches where home_team played against any team
            match_df = six_df[six_df['match'].str.contains(home_team, na=False)]
        
        # Extract relevant details
        match_details = match_df[['match', 'batsmanName', 'bowlerName']].drop_duplicates()
        match_count = match_details['match'].nunique()
        
        return {
            "matchCount": match_count,
            "details": match_details.to_dict(orient="records"),
            "probability":predict_six_probability(home_team=home_team,other_team=other_team)
        }
    except Exception as e:
        logging.error(f"Error in get_six_details: {e}")
        return {"error": "An error occurred while processing the request."}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query_sixes", methods=["GET"])
def query_sixes():
    try:
        home_team = request.args.get("homeTeam")
        other_team = request.args.get("otherTeam")
        
        if not home_team:
            return jsonify({"error": "Missing homeTeam parameter"}), 400
        
        result = get_six_details(home_team, other_team)
        return jsonify(result)
    except Exception as e:
        logging.error(f"Error in query_sixes: {e}")
        return jsonify({"error": "An internal error occurred."}), 500

if __name__ == "__main__":
    app.run(debug=True)
