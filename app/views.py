from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from sympy.solvers import solve
from sympy import Symbol, integrate, init_printing, latex

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
    

@views.route('/Math',methods=['GET', 'POST'])
@login_required   
def calc():
    #Global Variable for output
    global result, res, intg

    init_printing()
    x = Symbol('x')
    try:
        # Input Data
        a = request.form.get('a', '0')
        b = request.form.get('b', '0')
        f = request.form.get('f', '0')
        i = request.form.get('i', '0')

        # Results
        # 1 Sommation
        result= str(float(a) + float(b))
        # 2 Equation roots
        res = str(solve(f, x))
        # 3 Integrate a function
        intg = latex(integrate(i, x))



    except Exception as e:    
        flash('The input field is incorrect/empty, Please check your data.', category='error')
    return render_template("Math.html", result=result, res=res, intg=intg, user=current_user)

