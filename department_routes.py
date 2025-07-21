from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Department

department_bp = Blueprint('department_bp', __name__)

@department_bp.route('/departments')
def list_departments():
    departments = Department.query.all()
    return render_template('department_list.html', departments=departments)

@department_bp.route('/departments/add', methods=['GET', 'POST'])
def add_department():
    if request.method == 'POST':
        new_department = Department(
            department_id=request.form['department_id'],
            address=request.form['address'],
            telephone=request.form['telephone']
        )
        db.session.add(new_department)
        db.session.commit()
        return redirect(url_for('department_bp.list_departments'))
    return render_template('department_edit.html', department=None)

@department_bp.route('/departments/edit/<department_id>', methods=['GET', 'POST'])
def edit_department(department_id):
    department = Department.query.get_or_404(department_id)
    if request.method == 'POST':
        department.address = request.form['address']
        department.telephone = request.form['telephone']
        db.session.commit()
        return redirect(url_for('department_bp.list_departments'))
    return render_template('department_edit.html', department=department)

@department_bp.route('/departments/delete/<department_id>', methods=['POST'])
def delete_department(department_id):
    department = Department.query.get_or_404(department_id)
    db.session.delete(department)
    db.session.commit()
    return redirect(url_for('department_bp.list_departments'))
