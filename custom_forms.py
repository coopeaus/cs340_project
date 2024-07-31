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


class UpdateStudentForm(FlaskForm):
    student_id = SelectField("Student ID #", choices=[i for i in range(1, 14)])
    first_name = StringField("First Name:")
    last_name = StringField("Last Name:")
    house_id = SelectField("House ID #", choices=[1, 2, 3, 4])
    grade_level = SelectField(
        "Level Attending", choices=[i for i in range(1, 8)]
    )
    submit = SubmitField("Update Student")


class DeleteStudentForm(FlaskForm):
    student_id = SelectField("Student ID #", choices=[i for i in range(1, 14)])
    first_name = StringField("First Name:")
    last_name = StringField("Last Name:")
    house_id = SelectField("House ID #", choices=[1, 2, 3, 4])
    grade_level = SelectField(
        "Level Attending", choices=[i for i in range(1, 8)]
    )
    submit = SubmitField("Delete Student")


class NewProfessorForm(FlaskForm):
    first_name = StringField("First Name:")
    last_name = StringField("Last Name:")
    submit = SubmitField("Add New Professor")


class UpdateProfessorForm(FlaskForm):
    professor_id = SelectField(
        "Professor ID #", choices=[i for i in range(1, 5)]
    )
    first_name = StringField("First Name:")
    last_name = StringField("Last Name:")
    submit = SubmitField("Update Professor")


# class DeleteProfessorForm(FlaskForm):
#     professor_id = SelectField(
#         "Professor ID #", choices=[i for i in range(1, 5)]
#     )
#     first_name = StringField("First Name:")
#     last_name = StringField("Last Name:")
#     submit = SubmitField("Delete Professor")


class NewHouseForm(FlaskForm):
    head_of_house = SelectField(
        "Head of House", choices=[i for i in range(1, 5)]
    )
    house_name = StringField("House Name:")
    house_animal = StringField("House Animal:")
    house_colors = StringField("House Colors:")
    submit = SubmitField("Add New House")


class UpdateHouseForm(FlaskForm):
    house_id = SelectField("House ID #", choices=[1, 2, 3, 4])
    head_of_house = SelectField(
        "Head of House", choices=[i for i in range(1, 5)]
    )
    house_name = StringField("House Name:")
    house_animal = StringField("House Animal:")
    house_colors = StringField("House Colors:")
    submit = SubmitField("Update House")


# class DeleteHouseForm(FlaskForm):
#     house_id = SelectField("House ID #", choices=[1, 2, 3, 4])
#     head_of_house = SelectField(
#         "Head of House", choices=[i for i in range(1, 5)]
#     )
#     house_name = StringField("House Name:")
#     house_animal = StringField("House Animal:")
#     house_colors = StringField("House Colors:")
#     submit = SubmitField("Delete House")


class NewSubjectForm(FlaskForm):
    subject_name = StringField("Subject Name:")
    core_elective = SelectField("Core(1)/Elective(0)", choices=[0, 1])
    submit = SubmitField("Add New Subject")


class UpdateSubjectForm(FlaskForm):
    subject_id = SelectField("Subject ID #", choices=[i for i in range(1, 13)])
    subject_name = StringField("Subject Name:")
    core_elective = SelectField("Core(1)/Elective(0)", choices=[0, 1])
    submit = SubmitField("Update Subject")


# class DeleteSubjectForm(FlaskForm):
#     subject_id = SelectField("Subject ID #", choices=[i for i in range(1, 13)])
#     subject_name = StringField("Subject Name:")
#     core_elective = SelectField("Core(1)/Elective(0)", choices=[0, 1])
#     submit = SubmitField("Delete Subject")


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


# class DeleteClassForm(FlaskForm):
#     class_id = SelectField("Class ID #", choices=[i for i in range(1, 21)])
#     subject_id = SelectField("Subject ID #", choices=[i for i in range(1, 13)])
#     professor_id = SelectField(
#         "Professor ID #", choices=[i for i in range(1, 5)]
#     )
#     class_level = SelectField("Class Level", choices=[i for i in range(1, 8)])
#     submit = SubmitField("Delete Class")


class NewRegistrationForm(FlaskForm):
    student_id = SelectField("Student ID #", choices=[i for i in range(1, 14)])
    class_id = SelectField("Class ID #", choices=[i for i in range(1, 21)])
    submit = SubmitField("Add New Registration")


# class DeleteRegistrationForm(FlaskForm):
#     student_id = SelectField("Student ID #", choices=[i for i in range(1, 14)])
#     class_id = SelectField("Class ID #", choices=[i for i in range(1, 21)])
#     submit = SubmitField("Delete Registration")
