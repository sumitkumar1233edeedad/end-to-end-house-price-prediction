# 🏠 House Price Predictor

A full-stack machine learning web application that predicts house prices based on key property features. Built with a clean **HTML/CSS frontend** and a **Python Flask backend**, powered by a trained regression model.

🌐 **Live Demo:** [https://end-to-end-house-price-prediction-dlk5.onrender.com](https://end-to-end-house-price-prediction-dlk5.onrender.com)

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
- **ML Model** — Trained Linear Regression model using scikit-learn
- **Responsive Design** — Works on desktop and mobile browsers
- **Input Validation** — Frontend and backend validation for clean data entry
- **JSON API** — RESTful endpoint for easy integration

---

## 🗂️ Project Structure

```
house-price-predictor/
│
├── app.py                  # Flask application & API routes
├── form.py                 # WTForms registration form
├── models/
│   └── bulided_model_selected_feature/
│       ├── Linear_model.pkl   # Trained Linear Regression model
│       └── scaler.pkl         # StandardScaler for feature scaling
│
├── requirements.txt        # Python dependencies
│
├── templates/
│   ├── landing.html        # Landing / registration page
│   ├── home.html           # Prediction page
│   ├── about.html          # About page
│   └── profile.html        # Profile page
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
| Deployment | Gunicorn + Render        |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sumitkumar1233edeedad/end-to-end-house-price-prediction.git
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

### 4. Run the Flask App

```bash
python app.py
```

Open your browser and go to: **http://127.0.0.1:5000**

---

## 🔌 API Reference

### `POST /predict`

Predicts the house price based on input features.

**Request Body (Form Data):**

| Field               | Type    | Description                        |
|---------------------|---------|------------------------------------|
| `Size_sqft`         | Float   | Total size in square feet          |
| `Living_Area_sqft`  | Float   | Living area in square feet         |
| `Tax_Assessed_Value`| Float   | Tax assessed value of property     |
| `Full_Baths`        | Integer | Number of full bathrooms           |
| `Overall_Quality`   | Integer | Overall quality score (1–10)       |
| `Kitchen_Quality`   | Integer | Kitchen quality score (1–10)       |
| `Is_Waterfront`     | Integer | Waterfront property? (0 or 1)      |
| `Zone_Downtown`     | Integer | Downtown zone? (0 or 1)            |

**Response:**

```json
{
  "status": "success",
  "predicted_price": 4500000,
  "currency": "USD"
}
```

---

## 🧠 Model Details

| Property      | Details                                              |
|---------------|------------------------------------------------------|
| Algorithm     | Linear Regression                                    |
| Scaler        | StandardScaler                                       |
| Training Data | 10,000+ housing records                              |
| Features Used | Size, Living Area, Baths, Quality, Waterfront, Zone, Tax Value |
| Accuracy (R²) | ~0.87                                                |
| MAE           | ~₹ 1,20,000                                          |

---

## 🚢 Deployment

### Deploy on Render (Free)

1. Push your code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your repo
4. Set **Build Command:** `pip install -r requirements.txt`
5. Set **Start Command:** `gunicorn app:app`
6. Add `.python-version` file with `3.11.9`
7. Click **Deploy**

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

**Sumit Kumar**
- GitHub: [@sumitkumar1233edeedad](https://github.com/sumitkumar1233edeedad)
- LinkedIn: [linkedin.com/in/sumit-kumar-ml](https://linkedin.com/in/sumit-kumar-ml)
- Email: sumitkuamr963@gmail.com

---

> ⭐ If you found this project helpful, please give it a star on GitHub!
