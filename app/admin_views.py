from app import app
from flask import render_template

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')


@app.route('/jinja')
def jinja():
    # Strings
    my_name = "Cristhian"

    # Integers
    my_age = 30

    # Lists
    langs = ["Python", "JavaScript", "Bash", "Ruby", "C", "Rust"]

    # Dictionaries
    friends = {
        "Diego": 43,
        "Diego R": 28,
        "Mabel": 26,
        "Andrea": 23,
        "Rose": 39
    }

    # Tuples
    colors = ("Red", "Blue")

    # Booleans
    cool = True

    # Classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description 
            self.domain = domain

        def pull(self):
            return f"Pulling repo '{self.name}'"

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask web framework for Python",
        domain="https://github.com/Julian-Nash/learning-flask.git"
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty

    context = {
        'my_name': my_name,
        'my_age': my_age,
        'langs': langs,
        'friends': friends,
        'cool': cool,
        'GitRemote': GitRemote,
        'my_remote': my_remote,
        'repeat': repeat
    }

    return render_template('admin/jinja.html', **context)