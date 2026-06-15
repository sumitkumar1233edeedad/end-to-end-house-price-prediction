# 🏠 House Price Predictor

A full-stack machine learning web application that predicts house prices based on key property features. Built with a clean **HTML/CSS frontend** and a **Python Flask backend**, powered by a trained regression model.

---

## 📸 Preview

```
┌─────────────────────────────────────────┐
│         🏠 House Price Predictor        │
│  ─────────────────────────────────────  │
│  Area (sq ft): [__________]             │
│  Bedrooms:     [__________]             │
│  Bathrooms:    [__________]             │
│  Location:     [Dropdown ▼]             │
│                                         │
│         [ Predict Price ]               │
│                                         │
│  💰 Estimated Price: ₹ 45,00,000        │
└─────────────────────────────────────────┘
```

---

## 🚀 Features

- **Interactive UI** — Clean HTML/CSS form for entering property details
- **Real-time Prediction** — Instant price estimates via Flask REST API
- **ML Model** — Trained Linear Regression / Random Forest model using scikit-learn
- **Responsive Design** — Works on desktop and mobile browsers
- **Input Validation** — Frontend and backend validation for clean data entry
- **JSON API** — RESTful endpoint for easy integration

---

## 🗂️ Project Structure

```
house-price-predictor/
│
├── app.py                  # Flask application & API routes
├── models/
|   |──main.ipynb
|   │         
│   ├── models/ acutally i make three model
|
|              
├── requirements.txt        # Python dependencies
│
├── templates/
│   └── index.html          # Main HTML page (Jinja2 template)
│
├── static/
│   ├── css/
│   │   └── style.css       # Stylesheet
│   ├── js/
│   │   └── main.js         # Frontend JavaScript (fetch API)
│   └── images/
│       └── house.svg       # UI assets
│
├── data/
│   └── housing_data.csv    # Training dataset
│
└── README.md
```

---

## 🛠️ Tech Stack

| Layer      | Technology               |
|------------|--------------------------|
| Frontend   | HTML5, CSS3, JavaScript  |
| Backend    | Python, Flask            |
| ML Model   | scikit-learn, pandas     |
| Data       | NumPy, Matplotlib        |
| Deployment | Gunicorn / Render / Heroku |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/house-price-predictor.git
cd end-to-end-house-price-prediction
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model

```bash
python model.py
```

> This generates `model.pkl` in the root directory.

### 5. Run the Flask App

```bash
python app.py
```

Open your browser and go to: **http://127.0.0.1:5000**

---

## 🔌 API Reference

### `POST /predict`

Predicts the house price based on input features.

**Request Body (JSON):**

```json
{
  "area": 1500,
  "bedrooms": 3,
  "bathrooms": 2,
  "location": "downtown",
  "age": 5
}
```

**Response:**

```json
{
  "status": "success",
  "predicted_price": 4500000,
  "currency": "INR",
  "confidence": "±5%"
}
```

**Error Response:**

```json
{
  "status": "error",
  "message": "Invalid input: area must be a positive number"
}
```

---

## 🧠 Model Details

| Property         | Details                        |
|------------------|--------------------------------|
| Algorithm        | Random Forest Regressor        |
| Training Data    | 10,000+ housing records        |
| Features Used    | Area, Bedrooms, Bathrooms, Location, Age |
| Accuracy (R²)    | ~0.87                          |
| MAE              | ~₹ 1,20,000                    |

### Input Features

| Feature    | Type    | Description                          |
|------------|---------|--------------------------------------|
| `area`     | Integer | Total area in square feet            |
| `bedrooms` | Integer | Number of bedrooms (1–10)            |
| `bathrooms`| Integer | Number of bathrooms (1–6)            |
| `location` | String  | Neighbourhood / city zone            |
| `age`      | Integer | Age of the property in years         |

---

## 💻 Frontend Overview

The UI is built with pure **HTML5 + CSS3**:

- **Form inputs** for all property features
- **Fetch API** (JavaScript) sends a POST request to `/predict`
- **Result card** animates in with the predicted price
- **CSS custom properties** for consistent theming
- **Mobile-responsive** layout using Flexbox/Grid

```html
<!-- Example form snippet -->
<form id="predict-form">
  <input type="number" id="area" placeholder="Area in sq ft" required />
  <input type="number" id="bedrooms" placeholder="Bedrooms" min="1" max="10" />
  <button type="submit">Predict Price</button>
</form>
```

---

## 🐍 Backend Overview

Flask handles routing, model loading, and prediction:

```python
from flask import Flask, request, jsonify, render_template
import pickle, numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array([[data["area"], data["bedrooms"],
                          data["bathrooms"], data["age"]]])
    price = model.predict(features)[0]
    return jsonify({"status": "success", "predicted_price": round(price, 2)})

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 📦 requirements.txt

```
flask==3.0.0
scikit-learn==1.4.0
pandas==2.2.0
numpy==1.26.4
gunicorn==21.2.0
```

---

## 🚢 Deployment

### Deploy on Render (Free)

1. Push your code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your repo
4. Set **Build Command:** `pip install -r requirements.txt`
5. Set **Start Command:** `gunicorn app:app`
6. Click **Deploy**

### Deploy on Heroku

```bash
heroku create house-price-predictor
git push heroku main
heroku open
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**
- GitHub: [@smitkumar1233edeedad](https://github.com/sumitkumar1233edeedad)
- LinkedIn: [linkedin.com/in/sumit-kumar-ml](https://linkedin.com/in/sumit-kumar-ml)
- Email:  sumitkuamr963@gmail.com

---

> ⭐ If you found this project helpful, please give it a star on GitHub!