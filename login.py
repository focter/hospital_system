from flask import Blueprint, render_template, request, redirect, url_for, session
from models import db, Doctor

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        password = request.form['password']
        doctor = Doctor.query.filter_by(doctor_id=doctor_id, password=password).first()
        if doctor:
            session['doctor_id'] = doctor_id
            session['doctor_name'] = doctor.name
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='工号或密码错误')
    return render_template('login.html')

@login_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_bp.login'))
