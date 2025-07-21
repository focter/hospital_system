# app.py
from flask import Flask, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from models import db
from login import login_bp
from patient_routes import patient_bp
from doctor_routes import doctor_bp
from room_routes import room_bp
from department_routes import department_bp

app = Flask(__name__)
app.secret_key = 'hospital-login-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/hospital_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(login_bp)
app.register_blueprint(patient_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(room_bp)
app.register_blueprint(department_bp)

@app.route('/')
def home():
    if 'doctor_id' not in session:
        return redirect(url_for('login_bp.login'))
    return redirect(url_for('patient_bp.list_patients'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
