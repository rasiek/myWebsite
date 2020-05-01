from app import app
from app.models import Work, Project_img
from flask import render_template





@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/projets')
def projets():
    works = Work.query.all()
    
    for work in works:
        print(works.title)

    return render_template('public/projets.html')

@app.route('/apropos')
def apropos():
    return render_template('public/apropos.html')

@app.route('/projets/<id>')
def projet(id):
    return render_template('public/projet.html', id=id)




