from flask import Blueprint, render_template, request, flash, jsonify,Response
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import matplotlib.pyplot as plt
from numpy import*
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random

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
    a = request.form.get('a', '0')
    b = request.form.get('b', '0')
    result= str(float(a) + float(b))
    return render_template("Math.html",result=result, user=current_user)


@views.route('/plot.png')
@login_required   
def plot()->None:
    """Generating a simple plot for a given function 

    Returns:
        [type]: [description]
    """
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@views.route('/Math',methods=['GET'])
@login_required  
def create_figure():
    function = request.form.get('function', '0')
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = arange(0,100)
    ys = eval(function(xs))
    axis.plot(xs, ys)
    return fig