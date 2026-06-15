from flask import Flask, render_template, redirect, url_for, flash
from form import RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my-secret-key'


# Landing Page
@app.route('/', methods=['GET', 'POST'])
def landing_page():
    form = RegistrationForm()

    if form.validate_on_submit():
        email = form.email.data

        flash(
            f'Welcome, {email}! You registered successfully.',
            'success'
        )

        return redirect(url_for('home'))

    return render_template('landing.html', form=form)


# Home Page
@app.route('/home')
def home():
    return render_template('home.html')


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