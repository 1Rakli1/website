from ext import db , app ,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class BaseModel:

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.commit()

class User(db.Model,BaseModel,UserMixin):
    id= db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    code=db.Column(db.String)
    password=db.Column(db.String)
    role=db.Column(db.String)
    siv=db.Column(db.String)

    def __init__(self,name,code,password,role,siv=""):
        self.name=name
        self.code=code
        self.password=generate_password_hash(password)
        self.role=role
        self.siv=siv

    def check_password(self,password):
        return check_password_hash(self.password,password)

class Addvacancy(db.Model,BaseModel):
    id= db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    company_name=db.Column(db.String)
    about = db.Column(db.String)
    salary=db.Column(db.Integer)
    status=db.Column(db.String)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__=="__main__":
    with app.app_context(): 
        db.create_all()

    app.app_context().push()
    new_user=User(name="admin_user",password="adminuser",role="admin",code="123456789123456789")
    db.session.add(new_user)
    db.session.commit()

