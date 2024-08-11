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

    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    submit = SubmitField("Update Professor")


class NewHouseForm(FlaskForm):
    """Represents the Create House Form"""

    db_connection = db.connect_to_database()
    query_professor_names = """
        SELECT CONCAT(Professors.first_name, ' ', Professors.last_name)
        AS professor_name FROM Professors;"""
    cursor = db.execute_query(
        db_connection=db_connection, query=query_professor_names
    )
    professor_names = cursor.fetchall()
    pname_choices = [
        professor_name["professor_name"] for professor_name in professor_names
    ]
    pname_choices.insert(0, "")
    cursor.close()
    db_connection.close()

    head_of_house = SelectField("Head of House", choices=pname_choices)
    house_name = StringField("House Name")
    house_animal = StringField("House Animal")
    house_colors = StringField("House Colors")
    submit = SubmitField("Add New House")


class UpdateHouseForm(FlaskForm):
    """Represents the Update House Form"""

    db_connection = db.connect_to_database()
    query_professor_names = """
        SELECT CONCAT(Professors.first_name, ' ', Professors.last_name)
        AS professor_name FROM Professors;"""
    cursor = db.execute_query(
        db_connection=db_connection, query=query_professor_names
    )
    professor_names = cursor.fetchall()
    pname_choices = [
        professor_name["professor_name"] for professor_name in professor_names
    ]
    pname_choices.insert(0, "")
    cursor.close()
    db_connection.close()

    head_of_house = SelectField("Head of House", choices=pname_choices)
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

    db_connection = db.connect_to_database()
    query_professor_names = """
        SELECT CONCAT(Professors.first_name, ' ', Professors.last_name)
        AS professor_name FROM Professors;"""
    cursor = db.execute_query(
        db_connection=db_connection, query=query_professor_names
    )
    professor_names = cursor.fetchall()
    pname_choices = [
        professor_name["professor_name"] for professor_name in professor_names
    ]
    pname_choices.insert(0, "")

    query_subject_names = """
        SELECT Subjects.subject_name FROM Subjects;"""
    cursor = db.execute_query(
        db_connection=db_connection, query=query_subject_names
    )
    subject_names = cursor.fetchall()
    sname_choices = [
        subject_name["subject_name"] for subject_name in subject_names
    ]
    cursor.close()
    db_connection.close()

    subject_name = SelectField("Subject Name", choices=sname_choices)
    professor_name = SelectField("Professor Name", choices=pname_choices)
    class_level = SelectField("Class Level", choices=[i for i in range(1, 8)])
    submit = SubmitField("Add New Class")


class UpdateClassForm(FlaskForm):
    """Represents the Update Class Form"""

    db_connection = db.connect_to_database()
    query_professor_names = """
        SELECT CONCAT(Professors.first_name, ' ', Professors.last_name)
        AS professor_name FROM Professors;"""
    cursor = db.execute_query(
        db_connection=db_connection, query=query_professor_names
    )
    professor_names = cursor.fetchall()
    pname_choices = [
        professor_name["professor_name"] for professor_name in professor_names
    ]
    pname_choices.insert(0, "")

    query_subject_names = """
        SELECT Subjects.subject_name FROM Subjects;"""
    cursor = db.execute_query(
        db_connection=db_connection, query=query_subject_names
    )
    subject_names = cursor.fetchall()
    sname_choices = [
        subject_name["subject_name"] for subject_name in subject_names
    ]
    cursor.close()
    db_connection.close()

    subject_name = SelectField("Subject Name", choices=sname_choices)
    professor_name = SelectField("Professor Name", choices=pname_choices)
    class_level = SelectField("Class Level", choices=[i for i in range(1, 8)])
    submit = SubmitField("Update Class")


class NewRegistrationForm(FlaskForm):
    """Represents the Create Class_Registration Form"""

    db_connection = db.connect_to_database()
    query_student_names = """
        SELECT CONCAT(Students.first_name, ' ', Students.last_name)
        AS student_name FROM Students;"""
    cursor = db.execute_query(
        db_connection=db_connection, query=query_student_names
    )
    student_names = cursor.fetchall()
    stname_choices = [
        student_name["student_name"] for student_name in student_names
    ]

    query_class_details = """
        SELECT CONCAT(Subjects.subject_name, ', ', Classes.class_level, ', ',
        Professors.first_name, ' ', Professors.last_name) AS class_detail
        FROM Classes
        LEFT JOIN Subjects
        ON Classes.subject_id = Subjects.subject_id
        LEFT JOIN Professors
        ON Classes.professor_id = Professors.professor_id;"""
    cursor = db.execute_query(
        db_connection=db_connection, query=query_class_details
    )
    class_details = cursor.fetchall()
    cdetail_choices = [
        class_detail["class_detail"] for class_detail in class_details
    ]
    cursor.close()
    db_connection.close()

    student_name = SelectField("Student Name", choices=stname_choices)
    class_detail = SelectField("Class Detail", choices=cdetail_choices)
    submit = SubmitField("Add New Registration")


class UpdateRegistrationForm(FlaskForm):
    """Represents the Update Class_Registration Form"""

    db_connection = db.connect_to_database()
    query_student_names = """
        SELECT CONCAT(Students.first_name, ' ', Students.last_name)
        AS student_name FROM Students;"""
    cursor = db.execute_query(
        db_connection=db_connection, query=query_student_names
    )
    student_names = cursor.fetchall()
    stname_choices = [
        student_name["student_name"] for student_name in student_names
    ]

    query_class_details = """
        SELECT CONCAT(Subjects.subject_name, ', ', Classes.class_level, ', ',
        Professors.first_name, ' ', Professors.last_name) AS class_detail
        FROM Classes
        LEFT JOIN Subjects
        ON Classes.subject_id = Subjects.subject_id
        LEFT JOIN Professors
        ON Classes.professor_id = Professors.professor_id;"""
    cursor = db.execute_query(
        db_connection=db_connection, query=query_class_details
    )
    class_details = cursor.fetchall()
    cdetail_choices = [
        class_detail["class_detail"] for class_detail in class_details
    ]
    cursor.close()
    db_connection.close()

    student_name = SelectField("Student Name", choices=stname_choices)
    class_detail = SelectField("Class Detail", choices=cdetail_choices)
    submit = SubmitField("Update Registration")
