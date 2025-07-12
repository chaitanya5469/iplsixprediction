Here’s a clean, professional `README.md` tailored to your **Streamlit-based IPL Six Predictor** project using the new code:

---

````markdown
# 🏏 IPL Six Predictor – Streamlit App

This Streamlit web app predicts the **probability of a six being hit in the first two overs** of an IPL match based on the selected teams. It uses a Logistic Regression model trained on a real IPL 2024 match dataset.

---

## 📊 Features

- Select **Home Team** and **Opponent Team** from dropdowns
- Get predicted **probability of a six** in the early overs
- Lightweight UI powered by Streamlit
- Instant feedback and interactive design

---


## 🧠 How It Works

- Loads match data from `IPL24_All_Matches_Dataset.xlsx`
- Encodes teams using `LabelEncoder`
- Trains a `LogisticRegression` model to classify six vs non-six
- Predicts based on selected team pair

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- scikit-learn
- NumPy

---

## 🧪 Local Setup

### 🔧 1. Clone the Repository
```bash
git clone https://github.com/chaitanya5469/iplsixprediction.git
cd iplsixprediction
````

### 🐍 2. Create Virtual Environment (Recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ 4. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🌐 Deploy Online

You can deploy this project easily using:

### ✅ [Streamlit Cloud](https://streamlit.io/cloud)

* Push your code to GitHub
* Sign in to Streamlit Cloud
* Deploy your repo in a few clicks

or

### ✅ [Hugging Face Spaces](https://huggingface.co/spaces)

* Create a new “Streamlit” space
* Upload `app.py`, `requirements.txt`, and your dataset
* Done!

---

## 📁 Project Structure

```
📦 iplsixprediction/
├── app.py                        # Streamlit app code
├── IPL24_All_Matches_Dataset.xlsx # Dataset used for model training
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 🤝 Contributing

Pull requests and feedback are welcome!
If you find bugs or want to suggest improvements, feel free to open an issue.

---

## 📜 License

This project is for educational purposes and may use publicly available IPL data.

---

### 👨‍💻 Created by [Chaitanya Krishna](https://github.com/chaitanya5469)

```

---

Let me know if you'd like this customized with:
- A deploy badge
- Instructions to upload pre-trained `.pkl` instead of training live
- A `label_encoder.pkl` to avoid re-encoding

I can also add a `requirements.txt` auto-generated from your environment if needed.
```
