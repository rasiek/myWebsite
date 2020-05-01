from app import db

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    is_academique = db.Column(db.Boolean)
    description = db.Column(db.Text)
    meta_descript = db.Column(db.String(100), index=True, unique=True) 
    organisation = db.Column(db.String(100), index=True, unique=True)
    task = db.Column(db.String(100), index=True, unique=True)
    key_words = db.Column(db.String(100), index=True)
    pj_imgs = db.relationship('Project_img', backref='work', lazy=True)

    def __repr__(self):
        return f'<Work {self.title}>'


class Project_img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logo = db.Column(db.String(100), index=True, unique=True)
    hero_img = db.Column(db.String(100), index=True, unique=True)
    several_img = db.Column(db.ARRAY(db.String(200)), index=True)

    work_id = db.Column(db.Integer, db.ForeignKey('work.id'), nullable=False)

    def __repr__(self):
        return f'id {self.id}'




