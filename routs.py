from flask import render_template,redirect, flash
from forms import Sign_in_worker,Sign_up_worker,Forgot_password_worker,Sign_in_company,Sign_up_company,Forgot_password_company,Siv,AddVacancy
from flask_login import login_user,logout_user,current_user,login_required
from os import path
from werkzeug.security import generate_password_hash
from models import BaseModel,User,Addvacancy

from ext import app,db

@app.route("/")
def OR():
    return render_template("OR.html")

@app.route("/home")
@login_required
def home_company():
    vacancy=Addvacancy.query.all()
    return render_template("home.html",vacancy=vacancy)

@app.route("/sign_in_worker",methods=["GET","POST"])
def signinworker():
    form=Sign_in_worker()
    if form.validate_on_submit():
        user = User.query.filter(User.name == form.name.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/home")
    return render_template("sign_in_worker.html",form=form)

registered=True

@app.route("/sign_up_worker",methods=["GET","POST"])
def signupworker():
    form=Sign_up_worker()
    if form.validate_on_submit():
        if User.query.filter(User.name == form.name.data).first():
            flash("მომხმარებელი უკვე არსებობს სცადეთ თავიდან")
        else:
            print("ara")
            if form.password.data == form.reppassword.data:
                user=User(name=form.name.data , code=form.code.data , password=form.password.data,role="worker")
                db.session.add(user)
                db.session.commit()
                return redirect("/sign_in_worker")
    return render_template("sign_up_worker.html",form=form)

@app.route("/forgot_password_worker",methods=["GET","POST"])
def forgotpasswordworker():
    form=Forgot_password_worker()
    if form.validate_on_submit():
        user = User.query.filter(User.name == form.name.data).first()
        if user and user.code == form.code.data:
            print("ki")
            if form.newpassword.data == form.reppassword.data:
                print("ara")
                user.password=generate_password_hash(form.newpassword.data)
                db.session.commit()
                return redirect("/sign_in_worker")

    return render_template("forgot_password_worker.html",form=form)

@app.route("/sign_in_company",methods=["GET","POST"])
def signincompany():
    form=Sign_in_company()
    if form.validate_on_submit():
        user = User.query.filter(User.name==form.name.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            print("kii")
            return redirect("/home")
    return render_template("sign_in_company.html",form=form)

@app.route("/sign_up_company",methods=["GET","POST"])
def signupcompany():
    form=Sign_up_company()
    if form.validate_on_submit():
        if User.query.filter(User.name==form.name.data).first():
            print("araa")
        else:
            if form.password.data == form.reppassword.data:
                print("fasofaosfk")
                user =User(name=form.name.data,code=form.code.data,password=form.password.data,role="company",siv="")
                db.session.add(user)
                db.session.commit()
                return redirect("/sign_in_company")
    return render_template("sign_up_company.html",form=form)

@app.route("/forgot_password_company",methods=["GET","POST"])
def forgotpasswordcompany():
    form=Forgot_password_company()
    if form.validate_on_submit():
        user = User.query.filter(User.name == form.name.data).first()
        if user and user.code == form.code.data:
            if form.newpassword.data == form.reppassword.data:
                user.password=generate_password_hash(form.newpassword.data)
                db.session.commit()
                return redirect("/Sign_in_company")
    return render_template("forgot_password_company.html",form=form)

@app.route("/siv",methods=["GET","POST"])
@login_required
def siv():
    form=Siv()
    return render_template("siv.html",form=form)

@app.route("/add_vacancy",methods=["GET","POST"])
@login_required
def add_vacancy():
    form=AddVacancy()
    if form.validate_on_submit():
        if User.query.filter(User.name==form.name.data).first():
            addvacancy = Addvacancy(name=form.name.data,company_name=form.compname.data,about=form.text.data,salary=form.salary.data,status="waiter")
            db.session.add(addvacancy)
            db.session.commit()
            return redirect("/home")
        else :
            flash("სახელი არ ემთხვევა თქვენს სახელს")
    return render_template("add_vacancy.html",form=form)

@app.route("/send_siv")
@login_required
def send_siv():
    flash("თქვენი სივი გაიგზავნა")
    return redirect("/home")

@app.route("/accept/<int:index>")
@login_required
def accept(index):
    vacancy=Addvacancy.query.get(index)
    vacancy.status="accepted"
    db.session.commit()
    return redirect("/confirm_vacancy")

@app.route("/delete/<int:index>")
@login_required
def delete(index):
    vacancy=Addvacancy.query.get(index)
    db.session.delete(vacancy)
    db.session.commit()
    return redirect("/home")

@app.route("/confirm_vacancy")
@login_required
def confirm_vacancy():
    vacancy=Addvacancy.query.all()
    return render_template("confirm_vacancy.html",vacancy=vacancy)

@app.route("/my_vacancy")
@login_required
def my_vacancy():
    vacancy=Addvacancy.query.all()
    return render_template("my_vacancy.html",vacancy=vacancy)

@app.route("/edit_vacancy/<int:index>",methods=["GET","POST"])
@login_required
def edit_vacancy(index):
    vacancy = Addvacancy.query.get(index)
    form = AddVacancy(name=vacancy.name,compname=vacancy.company_name,text=vacancy.about,salary=vacancy.salary)
    if form.validate_on_submit():
        vacancy.name=form.name.data
        vacancy.company_name=form.compname.data
        vacancy.about=form.text.data
        vacancy.salary=form.salary.data
        vacancy.status="waiter"
        db.session.commit()
        return redirect("/home")
    return render_template("add_vacancy.html",form=form)

@app.route("/edit_siv/<int:index>",methods=["GET","POST"])
@login_required
def edit_siv(index):
    user = User.query.get(index)
    form = Siv(siv=user.siv)
    if form.validate_on_submit():
        user.siv=form.siv.data
        db.session.commit()
        return redirect("/siv")
    return render_template("edit_siv.html",form=form)
@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")