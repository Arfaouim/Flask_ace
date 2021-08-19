from flask import Blueprint, render_template, request, flash, jsonify,Response
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from sympy.solvers import solve
from sympy.abc import*
from sympy import (Symbol, 
integrate,
init_printing, 
latex,
limit,
diff)
import io
from sympy.plotting import plot

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
    global result, res, limite, dintg, dif

    init_printing()
    x = Symbol('x')
    try:
        # Input Data

        a = request.form.get('a', '0')
        b = request.form.get('b', '0')
         #root
        f = request.form.get('f', '0')
         #int
        bmax = request.form.get('bmax', '0')
        bmin = request.form.get('bmin', '0')
        di = request.form.get('di', '0')
         #limit
        f_value = request.form.get('f_value', '0')
        x_value = request.form.get('x_value', '0')
         #plot
        diff_f =  request.form.get('diff_f', '0')

        # Results

        # 1 Sommation
        result= str(float(a) + float(b))
        # 2 Equation roots
        res = str(solve(f, x))
        # 3 Integrate a function
            # a defined integral
        dintg = latex(integrate(di, (x,bmin,bmax)))
        # 4 Limit a function
        limite = latex(limit(f_value, x, x_value))
        # 5 plot a function
        dif = latex(diff(diff_f,x))

    except Exception as e:    
        flash('The input field is incorrect/empty, Please check your data.', category='error')
    return render_template("Math.html", result=result, res=res, dintg=dintg, dif=dif, limite=limite, user=current_user)


