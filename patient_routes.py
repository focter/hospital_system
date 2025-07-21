from flask import Blueprint, render_template, request, redirect, url_for, session
from models import db, Patient, Doctor, Room

patient_bp = Blueprint('patient_bp', __name__)

@patient_bp.route('/patients')
def list_patients():
    if 'doctor_id' not in session:
        return redirect(url_for('login_bp.login'))
    patients = Patient.query.all()
    return render_template('patient_list.html', patients=patients)

@patient_bp.route('/patients/add', methods=['GET', 'POST'])
def add_patient():
    doctors = Doctor.query.all()
    rooms = Room.query.all()
    if request.method == 'POST':
        new_patient = Patient(
            patient_id=request.form['patient_id'],
            name=request.form['name'],
            age=int(request.form['age']),
            sex=request.form['sex'],
            doctor_id=request.form['doctor_id'],
            room_id=request.form['room_id']
        )
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('patient_bp.list_patients'))
    return render_template('patient_edit.html', patient=None, doctors=doctors, rooms=rooms)

@patient_bp.route('/patients/edit/<patient_id>', methods=['GET', 'POST'])
def edit_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    doctors = Doctor.query.all()
    rooms = Room.query.all()
    if request.method == 'POST':
        patient.name = request.form['name']
        patient.age = int(request.form['age'])
        patient.sex = request.form['sex']
        patient.doctor_id = request.form['doctor_id']
        patient.room_id = request.form['room_id']
        db.session.commit()
        return redirect(url_for('patient_bp.list_patients'))
    return render_template('patient_edit.html', patient=patient, doctors=doctors, rooms=rooms)

@patient_bp.route('/patients/delete/<patient_id>', methods=['POST'])
def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for('patient_bp.list_patients'))
