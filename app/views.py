from app import app, db
from flask import render_template, request
from app.models import Doctor

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/register-doctor', methods=['POST'])
def register_doctor():
    form = request.form
    doctor = Doctor(
        name = form['name'],
        email = form['email-address'],
        phone_number = form['phone-number'],
        government_number = form['government-id'],
    )
    doctor.set_password(form['password'])
    db.session.add(doctor)
    db.session.commit()
    return 'Successfully Registered'

@app.route('/login-doctor')
def individual_patient():
    return 'Individual Patient'