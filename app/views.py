from app import app
from app.models import Work, Project_img
from flask import render_template





@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/projets')
def projets():
    works = Work.query.all()
    pj_imgs = Project_img.query.all()
    
    context = {
        "works": works,
        "pj_imgs": pj_imgs
    }
    
    return render_template('public/projets.html', **context)

@app.route('/apropos')
def apropos():
    return render_template('public/apropos.html')

@app.route('/projets/<title>')
def projet(title):
    work = Work.query.filter_by(title=title).first_or_404()
    pj_imgs = Project_img.query.filter_by(work_id=work.id).first_or_404()
    
    context = {
        "work": work,
        "pj_imgs": pj_imgs
    }
    return render_template('public/projet.html', **context)




