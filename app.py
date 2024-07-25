from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
import secrets
import custom_forms
import database.db_connector as db

# Citation for the below config, Routes, and Listener
# Date: 7/23/24
# Adapted from:
# The main idea and organization was adapted from:
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

# Configuration
app = Flask(__name__)
token = secrets.token_urlsafe(16)
app.secret_key = token

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)
db_connection = db.connect_to_database()


# Routes
@app.route("/")
@app.route("/index.html")
@app.route("/home")
def home():
    return render_template("index.j2")


@app.route("/students")
def students():
    query = "SELECT * FROM Students;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    students = cursor.fetchall()

    # Structured these into a dictionary, to pass in as **kwargs
    values = {
        "title": "Students",
        "records": students,
        "enroll_form": custom_forms.NewStudentForm(),
        "find_form": custom_forms.LookupStudentForm(),
    }
    return render_template("students.j2", **values)


@app.route("/professors")
def professors():
    query = "SELECT * FROM Professors;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    professors = cursor.fetchall()
    values = {
        "title": "Professors",
        "records": professors,
        "new_prof": custom_forms.NewProfessorForm(),
    }
    return render_template("professors.j2", **values)


@app.route("/houses")
def houses():
    query = "SELECT * FROM Houses;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    houses = cursor.fetchall()
    return render_template(
        "houses.j2",
        records=houses,
    )


@app.route("/subjects")
def subjects():
    query = "SELECT * FROM Subjects;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    subjects = cursor.fetchall()
    return render_template(
        "subjects.j2",
        records=subjects,
    )


@app.route("/classes")
def classes():
    query = "SELECT * FROM Classes;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    classes = cursor.fetchall()
    query = "SELECT * FROM Class_Registrations;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    registrations = cursor.fetchall()
    print(registrations[0].keys())
    values = {
        "title": "Classes",
        "records": classes,
        "class_registrations": registrations,
        "buttons": [
            "Create a Class",
            "Find a Class",
        ],
        "buttons2": [
            "Register Student for a Class",
            "Find Class Registrations",
        ],
    }

    return render_template("classes.j2", **values)


# Listener
if __name__ == "__main__":
    app.run(port=65000, debug=True)
