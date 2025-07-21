from flask import Blueprint, render_template, request, redirect, url_for, session
from models import db, Doctor

doctor_bp = Blueprint('doctor_bp', __name__)

@doctor_bp.route('/doctors')
def list_doctors():
    doctors = Doctor.query.all()
    return render_template('doctor_list.html', doctors=doctors)

@doctor_bp.route('/doctors/add', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        new_doctor = Doctor(
            doctor_id=request.form['doctor_id'],
            name=request.form['name'],
            age=int(request.form['age']),
            sex=request.form['sex'],
            title=request.form['title'],
            department_id=request.form['department_id'],
            password=request.form['password']
        )
        db.session.add(new_doctor)
        db.session.commit()
        return redirect(url_for('doctor_bp.list_doctors'))
    return render_template('doctor_edit.html', doctor=None)

@doctor_bp.route('/doctors/edit/<doctor_id>', methods=['GET', 'POST'])
def edit_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    if request.method == 'POST':
        doctor.name = request.form['name']
        doctor.age = int(request.form['age'])
        doctor.sex = request.form['sex']
        doctor.title = request.form['title']
        doctor.department_id = request.form['department_id']
        doctor.password = request.form['password']
        db.session.commit()
        return redirect(url_for('doctor_bp.list_doctors'))
    return render_template('doctor_edit.html', doctor=doctor)

@doctor_bp.route('/doctors/delete/<doctor_id>', methods=['POST'])
def delete_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    db.session.delete(doctor)
    db.session.commit()
    return redirect(url_for('doctor_bp.list_doctors'))
