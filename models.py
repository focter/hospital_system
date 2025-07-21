from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    patient_id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(2), nullable=False)
    doctor_id = db.Column(db.String(12))
    room_id = db.Column(db.String(4))

class Doctor(db.Model):
    doctor_id = db.Column(db.String(12), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(2))
    title = db.Column(db.String(20))
    department_id = db.Column(db.String(20))
    password = db.Column(db.String(100), nullable=False, default='123456')

class Room(db.Model):
    room_id = db.Column(db.String(4), primary_key=True)
    bed_no = db.Column(db.String(4), nullable=False)
    department_id = db.Column(db.String(20))

class Department(db.Model):
    department_id = db.Column(db.String(20), primary_key=True)
    address = db.Column(db.String(50))
    telephone = db.Column(db.String(15))
