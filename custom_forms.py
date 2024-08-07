from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
import database.db_connector as db

# Citation for the below classes
# Date: 7/30/2024
# Adapted from:
# Examples in WTForms documentation
# Source URL: https://wtforms.readthedocs.io/en/3.1.x/fields/


class NewStudentForm(FlaskForm):
    """Represents the Create Student Form"""

    db_connection = db.connect_to_database()
    query_house_names = "SELECT house_name FROM Houses;"
    cursor = db.execute_query(
        db_connection=db_connection, query=query_house_names
    )
    house_names = cursor.fetchall()
    hname_choices = [house_name["house_name"] for house_name in house_names]
    hname_choices.insert(0, "")
    cursor.close()
    db_connection.close()

    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    house_name = SelectField("House Name", choices=hname_choices)
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

    db_connection = db.connect_to_database()
    query_house_names = "SELECT house_name FROM Houses;"
    cursor = db.execute_query(
        db_connection=db_connection, query=query_house_names
    )
    house_names = cursor.fetchall()
    hname_choices = [house_name["house_name"] for house_name in house_names]
    hname_choices.insert(0, "")
    cursor.close()
    db_connection.close()
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    house_name = SelectField("House Name", choices=hname_choices)
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

    professor_id = SelectField(
        "Professor ID #", choices=[i for i in range(1, 5)]
    )
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    submit = SubmitField("Update Professor")


class NewHouseForm(FlaskForm):
    """Represents the Create House Form"""

    head_of_house = SelectField(
        "Head of House", choices=[i for i in range(1, 5)]
    )
    house_name = StringField("House Name")
    house_animal = StringField("House Animal")
    house_colors = StringField("House Colors")
    submit = SubmitField("Add New House")


class UpdateHouseForm(FlaskForm):
    """Represents the Update House Form"""

    house_id = SelectField("House ID #", choices=[1, 2, 3, 4])
    head_of_house = SelectField(
        "Head of House", choices=[i for i in range(1, 5)]
    )
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

    subject_id = SelectField("Subject ID #", choices=[i for i in range(1, 13)])
    subject_name = StringField("Subject Name")
    core_elective = SelectField("Core(1)/Elective(0)", choices=[0, 1])
    submit = SubmitField("Update Subject")


class NewClassForm(FlaskForm):
    """Represents the Create Class Form"""

    subject_id = SelectField("Subject ID #", choices=[i for i in range(1, 13)])
    professor_id = SelectField(
        "Professor ID #", choices=[i for i in range(1, 5)]
    )
    class_level = SelectField("Class Level", choices=[i for i in range(1, 8)])
    submit = SubmitField("Add New Class")


class UpdateClassForm(FlaskForm):
    """Represents the Update Class Form"""

    class_id = SelectField("Class ID #", choices=[i for i in range(1, 21)])
    subject_id = SelectField("Subject ID #", choices=[i for i in range(1, 13)])
    professor_id = SelectField(
        "Professor ID #", choices=[i for i in range(1, 5)]
    )
    class_level = SelectField("Class Level", choices=[i for i in range(1, 8)])
    submit = SubmitField("Update Class")


class NewRegistrationForm(FlaskForm):
    """Represents the Create Class_Registration Form"""

    student_id = SelectField("Student ID #", choices=[i for i in range(1, 14)])
    class_id = SelectField("Class ID #", choices=[i for i in range(1, 21)])
    submit = SubmitField("Add New Registration")


class UpdateRegistrationForm(FlaskForm):
    """Represents the Update Class_Registration Form"""

    student_id = SelectField("Student ID #", choices=[i for i in range(1, 14)])
    class_id = SelectField("Class ID #", choices=[i for i in range(1, 21)])
    submit = SubmitField("Update Registration")
