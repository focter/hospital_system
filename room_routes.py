from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Room

room_bp = Blueprint('room_bp', __name__)

@room_bp.route('/rooms')
def list_rooms():
    rooms = Room.query.all()
    return render_template('room_list.html', rooms=rooms)

@room_bp.route('/rooms/add', methods=['GET', 'POST'])
def add_room():
    if request.method == 'POST':
        new_room = Room(
            room_id=request.form['room_id'],
            bed_no=request.form['bed_no'],
            department_id=request.form['department_id']
        )
        db.session.add(new_room)
        db.session.commit()
        return redirect(url_for('room_bp.list_rooms'))
    return render_template('room_edit.html', room=None)

@room_bp.route('/rooms/edit/<room_id>', methods=['GET', 'POST'])
def edit_room(room_id):
    room = Room.query.get_or_404(room_id)
    if request.method == 'POST':
        room.bed_no = request.form['bed_no']
        room.department_id = request.form['department_id']
        db.session.commit()
        return redirect(url_for('room_bp.list_rooms'))
    return render_template('room_edit.html', room=room)

@room_bp.route('/rooms/delete/<room_id>', methods=['POST'])
def delete_room(room_id):
    room = Room.query.get_or_404(room_id)
    db.session.delete(room)
    db.session.commit()
    return redirect(url_for('room_bp.list_rooms'))
