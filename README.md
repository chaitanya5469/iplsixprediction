# IPL Six Prediction Web App

## Overview
This web application predicts the probability of hitting a six in the first two overs of an IPL match between two selected teams. It also provides details on the number of past matches where a six was hit in the first two overs. The backend is built using Flask, and the machine learning model is trained using logistic regression.

## Features
- Query the number of matches where a six was hit in the first two overs.
- Predict the probability of a six being hit in the first two overs based on the selected teams, batsman, and bowler.
- Interactive frontend for user input.
- Machine learning model trained on IPL data.

## Technologies Used
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-learn (Logistic Regression)
- **Frontend:** HTML, JavaScript, CSS
- **Data Storage:** Excel dataset

## Installation & Setup
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.7+
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/chaitanya5469/iplsixprediction.git
   cd iplsixprediction
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```sh
   python app.py
   ```
5. Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

## API Endpoints
- `GET /query_sixes?homeTeam=<team>&otherTeam=<team>&batsman=<name>&bowler=<name>`
  - Returns:
    ```json
    {
      "match_count": 5,
      "six_probability": 0.75
    }
    ```

## Hosting the Web App
You can deploy this Flask app on platforms like **Render, Heroku, or Vercel**.
### Deployment on Heroku
1. Install Heroku CLI.
2. Login to Heroku:
   ```sh
   heroku login
   ```
3. Create a Heroku app:
   ```sh
   heroku create
   ```
4. Deploy your app:
   ```sh
   git push heroku main
   ```
5. Open the app in your browser:
   ```sh
   heroku open
   ```

## License
This project is open-source and available under the MIT License.

