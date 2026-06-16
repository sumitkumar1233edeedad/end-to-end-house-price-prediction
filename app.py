import os
import joblib
import pandas as pd
from flask import Flask, render_template, redirect, url_for, flash, request
from form import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'

# 1. Resolve absolute paths so Vercel always finds your files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCALER_PATH = os.path.join(BASE_DIR, 'models', 'bulided_model_selected_feature', 'scaler.pkl')
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'bulided_model_selected_feature', 'Linear_model.pkl')

# 2. Load model and scaler GLOBALLY once when the application boots up
try:
    scaler = joblib.load(SCALER_PATH)
    model = joblib.load(MODEL_PATH)
    print("Model and Scaler loaded successfully into memory.")
except Exception as e:
    print(f"CRITICAL ERROR: Failed to load model or scaler. Details: {e}")
    scaler, model = None, None


# Landing Page
@app.route('/', methods=['GET', 'POST'])
def landing_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        flash(f'Welcome, {email}! You registered successfully.', 'success')
        return redirect(url_for('home'))
    return render_template('landing.html', form=form)


# Home Page
@app.route('/home')
def home():
    return render_template('Home.html')


# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Safety check: Ensure the models are actually loaded
        if scaler is None or model is None:
            raise RuntimeError("Machine Learning models failed to load at startup.")

        # 1. Extract values from the form
        size_sqft = float(request.form.get('Size_sqft', 0))
        living_area_sqft = float(request.form.get('Living_Area_sqft', 0))
        tax_assessed_value = float(request.form.get('Tax_Assessed_Value', 0))

        full_baths = int(request.form.get('Full_Baths', 1))
        overall_quality = int(request.form.get('Overall_Quality', 5))
        kitchen_quality = int(request.form.get('Kitchen_Quality', 5))

        waterfront_list = request.form.getlist('Is_Waterfront')
        is_waterfront = int(waterfront_list[-1]) if waterfront_list else 0

        downtown_list = request.form.getlist('Zone_Downtown')
        zone_downtown = int(downtown_list[-1]) if downtown_list else 0

        # 2. Format features directly into a DataFrame
        feature_dict = {
            'Size_sqft': [size_sqft],
            'Living_Area_sqft': [living_area_sqft],
            'Full_Baths': [full_baths],
            'Overall_Quality': [overall_quality],
            'Kitchen_Quality': [kitchen_quality],
            'Is_Waterfront': [is_waterfront],
            'Zone_Downtown': [zone_downtown],
            'Tax_Assessed_Value': [tax_assessed_value]
        }
        features_df = pd.DataFrame(feature_dict)

        # 3. Transform and Predict using the GLOBAL instances (Super fast!)
        test = scaler.transform(features_df)
        prediction = model.predict(test)

        # 4. Format Output
        predicted_price = float(prediction[0])
        formatted_price = f"${predicted_price:,.2f}"

        submitted_inputs = {
            'Size_sqft': f"{size_sqft:,.0f}",
            'Living_Area_sqft': f"{living_area_sqft:,.0f}",
            'Full_Baths': full_baths,
            'Overall_Quality': overall_quality,
            'Kitchen_Quality': kitchen_quality,
            'Is_Waterfront': is_waterfront,
            'Zone_Downtown': zone_downtown,
            'Tax_Assessed_Value': f"₹{tax_assessed_value:,.0f}"
        }

        return render_template('home.html', prediction_text=f'Predicted Price: {formatted_price}', user_inputs=submitted_inputs)

    except Exception as e:
        print("\n" + "="*50)
        print(f"PIPELINE CRASHED! Actual Error: {str(e)}")
        print("="*50 + "\n")
        return render_template('home.html', prediction_text=f"Engine Error: {str(e)}")


# About Page
@app.route('/about')
def about():
    return render_template('about.html')


# Profile Page
@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug=True)