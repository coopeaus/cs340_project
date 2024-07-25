from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


class NewStudentForm(FlaskForm):
    first_name = StringField("First Name:")
    last_name = StringField("Last Name:")
    house_id = SelectField("House ID #", choices=[1, 2, 3, 4])
    grade_level = SelectField(
        "Level Attending", choices=[i for i in range(1, 8)]
    )
    submit = SubmitField("Enroll New Student")


class LookupStudentForm(FlaskForm):
    first_name = StringField("First Name:")
    last_name = StringField("Last Name:")
    submit = SubmitField("Find Student")


class NewProfessorForm(FlaskForm):
    first_name = StringField("First Name:")
    last_name = StringField("Last Name:")
    submit = SubmitField("Enroll New Student")
