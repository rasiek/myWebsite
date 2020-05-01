from app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, DataRequired


class ContactForm(FlaskForm):
    name = StringField('Votre Nom et Prenom', [DataRequired()])
    email = EmailField('Votre email', [DataRequired(), Email(message='Saisir un email valide')])
    sujet = StringField('Sujet')
    message = TextAreaField('Écrire votre message ici...', [DataRequired()])
    submit = SubmitField('Envoyer')



@app.route('/contact', methods=['GET', 'POST'])
def contact():

    contact_form = ContactForm()

    context = {
        'contact_form': contact_form
    }

    return render_template('contact/contact.html', **context)