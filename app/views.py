from app import app, db
from flask import render_template, request, redirect, url_for
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
    form = request.form
    doctor = Doctor.query.filter_by(email=form['email-address']).first()
    if doctor.check_password(form['password']):
        return redirect (url_for('patients'))
    else:
        return 'Error'
    
@app.route('/patients', methods=['POST'])
def patients():
    return 'Successfully Logged in'