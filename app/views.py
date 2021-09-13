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
from .compute import* 


views = Blueprint('views', __name__)

@views.route('/')
@login_required   
def home():
    return render_template("home.html",  user=current_user)    

@views.route('/Notebook', methods=['GET', 'POST'])
@login_required
def Notebook():
    if request.method == 'POST':
        note = request.form.get('note')

        if not note:
            flash('The Note cannot be empty!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('New note added!', category='success')

    return render_template("Notebook.html", user=current_user)


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
    

@views.route('/tools')
@login_required   
def tools():
    return render_template("tools.html",  user=current_user)

@views.route('/math-list')
@login_required   
def math_list():
    return render_template("math-list.html",  user=current_user)    

@views.route('/programing-list')
@login_required   
def prgraming_list():
    return render_template("programing-list.html",  user=current_user)  

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

@views.route('/python')
@login_required   
def python():
    return render_template("python.html",  user=current_user)  

@views.route('/quiz-python')
@login_required   
def quiz_python():
    return render_template("quiz-python.html",  user=current_user)      


@views.route('/compiler-python')
@login_required   
def compiler_python():
    return render_template("python_compiler.html",  user=current_user)    


@views.route('/Tostart') 
def start():
    return render_template("Tostart.html",  user=current_user)        

@views.route('/Plotting') 
def plot():
    return render_template("plotting.html",  user=current_user)            
    
@views.route('/plot2d') 
def plot2d():
    return render_template("plotting/2dplot.html",  user=current_user)          
@views.route('/plot3d') 
def plot3d():
    return render_template("plotting/3dplot.html",  user=current_user)          


@views.route('/DiscretSum', methods=['GET', 'POST'])
def DiscretSum():
    try:
        if request.method == 'POST':
            fun = request.form['fun']
            var = request.form['var']
            start = request.form['start']
            end = request.form['end']
            exp = expr(request.form['fun'],request.form['var'],request.form['start'],request.form['end'])
            result  = calc_(fun,var,start,end)
            simplify = simplified(result)
            flash(f'Done ! ', category='success')  
            return render_template('DiscretSum.html',exp=exp, result=latex(result), simplify=simplify, user=current_user)
    except Exception as e:    
        flash(f'Check your input again', category='error')   
    flash(f'Hey {current_user}! Great Day for some Calclus ', category='success')       
    return render_template("DiscretSum.html",  user=current_user)  
              
