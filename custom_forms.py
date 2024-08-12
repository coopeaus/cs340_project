from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

# Citation for the below classes
# Date: 7/30/2024
# Adapted from:
# Examples in WTForms documentation
# Source URL: https://wtforms.readthedocs.io/en/3.1.x/fields/


class NewStudentForm(FlaskForm):
    """Represents the Create Student Form"""

    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    house_name = SelectField("House Name")
    level_attending = SelectField(
        "Level Attending", choices=[i for i in range(1, 8)]
    )
    submit = SubmitField("Enroll New Student")


class LookupStudentForm(FlaskForm):
    """Represents the Student Lookup Form"""

    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    submit = SubmitField("Find Student")


class UpdateStudentForm(FlaskForm):
    """Represents the Update Student Form"""

    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    house_name = SelectField("House Name")
    level_attending = SelectField(
        "Level Attending", choices=[i for i in range(1, 8)]
    )
    submit = SubmitField("Update Student")


class NewProfessorForm(FlaskForm):
    """Represents the Create Professor Form"""

    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    submit = SubmitField("Add New Professor")


class UpdateProfessorForm(FlaskForm):
    """Represents the Update Professor Form"""

    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    submit = SubmitField("Update Professor")


class NewHouseForm(FlaskForm):
    """Represents the Create House Form"""

    head_of_house = SelectField("Head of House")
    house_name = StringField("House Name")
    house_animal = StringField("House Animal")
    house_colors = StringField("House Colors")
    submit = SubmitField("Add New House")


class UpdateHouseForm(FlaskForm):
    """Represents the Update House Form"""

    head_of_house = SelectField("Head of House")
    house_name = StringField("House Name")
    house_animal = StringField("House Animal")
    house_colors = StringField("House Colors")
    submit = SubmitField("Update House")


class NewSubjectForm(FlaskForm):
    """Represents the Create Subject Form"""

    subject_name = StringField("Subject Name")
    core_elective = SelectField("Core(1)/Elective(0)", choices=[0, 1])
    submit = SubmitField("Add New Subject")


class UpdateSubjectForm(FlaskForm):
    """Represents the Update Subject Form"""

    subject_name = StringField("Subject Name")
    core_elective = SelectField("Core(1)/Elective(0)", choices=[0, 1])
    submit = SubmitField("Update Subject")


class NewClassForm(FlaskForm):
    """Represents the Create Class Form"""

    subject_name = SelectField("Subject Name")
    professor_name = SelectField("Professor Name")
    class_level = SelectField("Class Level", choices=[i for i in range(1, 8)])
    submit = SubmitField("Add New Class")


class UpdateClassForm(FlaskForm):
    """Represents the Update Class Form"""

    subject_name = SelectField("Subject Name")
    professor_name = SelectField("Professor Name")
    class_level = SelectField("Class Level", choices=[i for i in range(1, 8)])
    submit = SubmitField("Update Class")


class NewRegistrationForm(FlaskForm):
    """Represents the Create Class_Registration Form"""

    student_name = SelectField("Student Name")
    class_detail = SelectField("Class Detail")
    submit = SubmitField("Add New Registration")


class UpdateRegistrationForm(FlaskForm):
    """Represents the Update Class_Registration Form"""

    student_name = SelectField("Student Name")
    class_detail = SelectField("Class Detail")
    submit = SubmitField("Update Registration")
