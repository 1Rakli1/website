from flask_wtf import FlaskForm
from wtforms.fields import StringField,IntegerField,DateField,SubmitField,PasswordField,TextAreaField
from flask_wtf.file import FileField , FileRequired , FileAllowed,FileSize
from wtforms.validators import DataRequired,Length

class Sign_in_worker(FlaskForm):
    name = StringField("სახელი და გვარი",validators=[DataRequired(message="სახელი არ არის შემოტანილი") ])
    password = PasswordField("პაროლი",validators=[Length(min=8,message="პაროლი უნდა იყოს 8 ასოზე მეტი"),DataRequired(message="პაროლი არ არის შემოყვანილი")])
    submit=SubmitField("შესვლა")

class Sign_up_worker(FlaskForm):
    name = StringField("სახელი და გვარი",validators=[DataRequired(message="სახელი არ არის შემოტანილი") ])
    password = PasswordField("პაროლი",validators=[Length(min=8,message="პაროლი უნდა იყოს 8 ციფრზე მეტი"),DataRequired(message="პაროლი არ არის შემოყვანილი")])
    reppassword = PasswordField("გაიმეორე პაროლი",validators=[Length(min=8,message="პაროლი უნდა იყოს 8 ციფრზე მეტი"),DataRequired(message="პაროლი არ არის შემოყვანილი")])
    code = StringField("სპეციალური კოდი",validators=[Length(min=16,message="კოდი უნდა იყოს 16 ციფრზე"),DataRequired(message="aკოდი არ არის შეყვანილი")])
    submit=SubmitField("შესვლა")

class Forgot_password_worker(FlaskForm):
    name = StringField("სახელი და გვარი",validators=[DataRequired(message="სახელი არ არის შემოტანილი") ])
    code = StringField("სპეციალური კოდი",validators=[Length(min=16,message="კოდი უნდა იყოს 16 ციფრზე"),DataRequired(message="aკოდი არ არის შეყვანილი")])
    newpassword = PasswordField("ახალი პაროლი",validators=[Length(min=8,message="პაროლი უნდა იყოს 8 ციფრზე მეტი"),DataRequired(message="პაროლი არ არის შემოყვანილი")])
    reppassword = PasswordField("გაიმეორე პაროლი",validators=[Length(min=8,message="პაროლი უნდა იყოს 8 ციფრზე მეტი"),DataRequired(message="პაროლი არ არის შემოყვანილი")])
    submit=SubmitField("შესვლა")

class Sign_up_company(FlaskForm):
    name = StringField("სახელი და გვარი",validators=[DataRequired(message="სახელი არ არის შემოტანილი") ])
    password = PasswordField("პაროლი",validators=[Length(min=8,message="პაროლი უნდა იყოს 8 ციფრზე მეტი"),DataRequired(message="პაროლი არ არის შემოყვანილი")])
    reppassword = PasswordField("გაიმეორე პაროლი",validators=[Length(min=8,message="პაროლი უნდა იყოს 8 ციფრზე მეტი"),DataRequired(message="პაროლი არ არის შემოყვანილი")])
    code = StringField("სპეციალური კოდი",validators=[Length(min=16,message="კოდი უნდა იყოს 16 ციფრზე"),DataRequired(message="aკოდი არ არის შეყვანილი")])
    submit=SubmitField("შესვლა")

class Sign_in_company(FlaskForm):
    name = StringField("სახელი და გვარი",validators=[DataRequired(message="სახელი არ არის შემოტანილი") ])
    password = PasswordField("პაროლი",validators=[Length(min=8,message="პაროლი უნდა იყოს 8 ასოზე მეტი"),DataRequired(message="პაროლი არ არის შემოყვანილი")])
    submit=SubmitField("შესვლა")

class Forgot_password_company(FlaskForm):
    name = StringField("სახელი და გვარი",validators=[DataRequired(message="სახელი არ არის შემოტანილი") ])
    compname=StringField("კომპანიის სახელი",validators=[DataRequired(message="სახელი არ არის შემოტანილი")])
    code = StringField("სპეციალური კოდი",validators=[Length(min=16,message="კოდი უნდა იყოს 16 ციფრზე"),DataRequired(message="aკოდი არ არის შეყვანილი")])
    newpassword = PasswordField("ახალი პაროლი",validators=[Length(min=8,message="პაროლი უნდა იყოს 8 ციფრზე მეტი"),DataRequired(message="პაროლი არ არის შემოყვანილი")])
    reppassword = PasswordField("გაიმეორე პაროლი",validators=[Length(min=8,message="პაროლი უნდა იყოს 8 ციფრზე მეტი"),DataRequired(message="პაროლი არ არის შემოყვანილი")])
    submit=SubmitField("შესვლა")

class AddVacancy(FlaskForm):
    name = StringField("სახელი და გვარი",validators=[DataRequired(message="სახელი არ არის შემოტანილი") ])
    compname=StringField("კომპანიის სახელი",validators=[DataRequired(message="სახელი არ არის შემოტანილი")])
    text =TextAreaField("თქვენს შესახებ",validators=[DataRequired(message="არ არის შემოტანილი ტექსტი")])
    salary = IntegerField("ხელფასი ხელზე",validators=[DataRequired(message="ხელფასი არ არის შევსებული")])
    button = SubmitField("გაგზავნა")

class Siv(FlaskForm):
    siv=TextAreaField("დაწერე შენი სივი",validators=[DataRequired(message="სივი არ არის შევსებული")])
    submit=SubmitField("დასეივება")