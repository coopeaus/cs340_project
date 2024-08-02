from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
import database.db_connector as db


db_connection = db.connect_to_database()
query_house_names = "SELECT house_name FROM Houses;"
cursor = db.execute_query(db_connection=db_connection, query=query_house_names)
house_names = cursor.fetchall()
hname_choices = [house_name["house_name"] for house_name in house_names]
hname_choices.insert(0, "")

query_student_ids = "SELECT student_id FROM Students;"
cursor = db.execute_query(db_connection=db_connection, query=query_student_ids)
student_ids = cursor.fetchall()
sid_choices = [student_id["student_id"] for student_id in student_ids]

cursor.close()
db_connection.close()


class NewStudentForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    house_name = SelectField("House Name", choices=hname_choices)
    level_attending = SelectField(
        "Level Attending", choices=[i for i in range(1, 8)]
    )
    submit = SubmitField("Enroll New Student")


class LookupStudentForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    submit = SubmitField("Find Student")


class UpdateStudentForm(FlaskForm):
    student_id = SelectField("Student ID #", choices=sid_choices)
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    house_name = SelectField("House Name", choices=hname_choices)
    level_attending = SelectField(
        "Level Attending", choices=[i for i in range(1, 8)]
    )
    submit = SubmitField("Update Student")


class NewProfessorForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    submit = SubmitField("Add New Professor")


class UpdateProfessorForm(FlaskForm):
    professor_id = SelectField(
        "Professor ID #", choices=[i for i in range(1, 5)]
    )
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    submit = SubmitField("Update Professor")


class NewHouseForm(FlaskForm):
    head_of_house = SelectField(
        "Head of House", choices=[i for i in range(1, 5)]
    )
    house_name = StringField("House Name")
    house_animal = StringField("House Animal")
    house_colors = StringField("House Colors")
    submit = SubmitField("Add New House")


class UpdateHouseForm(FlaskForm):
    house_id = SelectField("House ID #", choices=[1, 2, 3, 4])
    head_of_house = SelectField(
        "Head of House", choices=[i for i in range(1, 5)]
    )
    house_name = StringField("House Name")
    house_animal = StringField("House Animal")
    house_colors = StringField("House Colors")
    submit = SubmitField("Update House")


class NewSubjectForm(FlaskForm):
    subject_name = StringField("Subject Name")
    core_elective = SelectField("Core(1)/Elective(0)", choices=[0, 1])
    submit = SubmitField("Add New Subject")


class UpdateSubjectForm(FlaskForm):
    subject_id = SelectField("Subject ID #", choices=[i for i in range(1, 13)])
    subject_name = StringField("Subject Name")
    core_elective = SelectField("Core(1)/Elective(0)", choices=[0, 1])
    submit = SubmitField("Update Subject")


class NewClassForm(FlaskForm):
    subject_id = SelectField("Subject ID #", choices=[i for i in range(1, 13)])
    professor_id = SelectField(
        "Professor ID #", choices=[i for i in range(1, 5)]
    )
    class_level = SelectField("Class Level", choices=[i for i in range(1, 8)])
    submit = SubmitField("Add New Class")


class UpdateClassForm(FlaskForm):
    class_id = SelectField("Class ID #", choices=[i for i in range(1, 21)])
    subject_id = SelectField("Subject ID #", choices=[i for i in range(1, 13)])
    professor_id = SelectField(
        "Professor ID #", choices=[i for i in range(1, 5)]
    )
    class_level = SelectField("Class Level", choices=[i for i in range(1, 8)])
    submit = SubmitField("Update Class")


class NewRegistrationForm(FlaskForm):
    student_id = SelectField("Student ID #", choices=[i for i in range(1, 14)])
    class_id = SelectField("Class ID #", choices=[i for i in range(1, 21)])
    submit = SubmitField("Add New Registration")
