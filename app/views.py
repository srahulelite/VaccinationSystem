from app import app, db
from flask import render_template, request, redirect, url_for, flash, jsonify, session
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

@app.route('/validate-doctor-registration', methods=['POST'])
def validate_doctor_registration():
    if request.method == "POST":
        email_address = request.get_json()['email']
        doctor = Doctor.query.filter_by(email=email_address).first()
        if doctor:
            return jsonify({"user_exists": "true"})
        else:
            return jsonify({"user_exists": "false"})
    return 

@app.route('/login-doctor', methods=['POST'])
def individual_patient():
    form = request.form
    doctor = Doctor.query.filter_by(email=form['email-add']).first()
    if not doctor:
        flash("Doctor doesn't exist")
        return redirect(url_for('index'))
    
    if doctor.check_password(form['pass']):
        session['doctor'] = doctor.id
        return redirect (url_for('patients'))
    else:
        flash("Password was incorrect")
        return redirect(url_for('index'))
    
@app.route('/logout-doctor', methods=['GET', 'POST'])
def logout_doctor():
    session.pop('doctor', None)
    return redirect(url_for('index'))
    
@app.route('/patients', methods=['POST', 'GET'])
def patients():
    doctor_id = None
    if session['doctor']:
        doctor_id = session['doctor']
    return render_template('patients.html')