from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
import MySQLdb
import MySQLdb.cursors
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


# Routes
@app.route("/")
@app.route("/index.html")
@app.route("/home")
def home():
    """Home page route"""
    return render_template("index.j2")


@app.route("/students", methods=["post", "get"])
def students():
    """Displays the Students page and associated CRUD operations"""
    form = custom_forms.NewStudentForm(request.form)
    if request.method == "POST":
        try:
            # We were having connection issues, so decided
            # to renew the DB connection on each request.
            # Per the MySQLdb library docs, the cursor should be closed
            # at a minimum each time.
            db_connection = db.connect_to_database()
            first_name = form.first_name.data
            last_name = form.last_name.data
            house_name = form.house_name.data
            level_attending = form.level_attending.data
            if house_name == "":
                query = """
                    INSERT INTO Students (first_name, last_name,
                    level_attending) VALUES (%s,%s,%s);"""
                cursor = db.execute_query(
                    db_connection=db_connection,
                    query=query,
                    query_params=(
                        first_name,
                        last_name,
                        level_attending,
                    ),
                )
                # Close the cursor and connection each time.
                cursor.close()
                db_connection.close()
                return redirect("/students")
            else:
                query_house = """SELECT Houses.house_id,
                    Houses.house_name FROM Houses;"""
                cursor = db.execute_query(
                    db_connection=db_connection, query=query_house
                )
                houses = cursor.fetchall()
                for house in houses:
                    if house_name == house["house_name"]:
                        house_id = house["house_id"]
                query = """
                    INSERT INTO Students (first_name, last_name, house_id,
                    level_attending) VALUES (%s, %s,%s,%s);"""
                cursor = db.execute_query(
                    db_connection=db_connection,
                    query=query,
                    query_params=(
                        first_name,
                        last_name,
                        house_id,
                        level_attending,
                    ),
                )
                # Close the cursor and connection each time.
                cursor.close()
                db_connection.close()
                return redirect("/students")
        except MySQLdb.Error as e:
            # Catch and display any DB errors
            print(e)
            return e
    else:
        try:
            db_connection = db.connect_to_database()
            query = (
                "SELECT Students.student_id, Students.first_name, "
                "Students.last_name, Houses.house_name AS house_name, "
                "Students.level_attending FROM Students LEFT JOIN Houses "
                "ON Students.house_id = Houses.house_id;"
            )
            cursor = db.execute_query(db_connection=db_connection, query=query)
            students = cursor.fetchall()

            # Structured these into a dictionary, to pass in as **kwargs
            values = {
                "title": "Students",
                "records": students,
                "fkey": list(students[0].keys())[0],
                "enroll_form": custom_forms.NewStudentForm(),
                "find_form": custom_forms.LookupStudentForm(),
                "update_form": custom_forms.UpdateStudentForm(),
            }
            return render_template("students.j2", **values)
        except MySQLdb.Error as e:
            # Catch and display any DB errors
            return e
        finally:
            # Close the cursor and connection each time.
            cursor.close()
            db_connection.close()


@app.route("/delete_Students/<int:id>")
def delete_student(id):
    try:
        db_connection = db.connect_to_database()
        query = "DELETE FROM Students WHERE student_id = '%s';"
        cursor = db.execute_query(
            db_connection=db_connection, query=query, query_params=(id,)
        )
        return redirect("/students")
    except MySQLdb.Error as e:
        return e
    finally:
        cursor.close()
        db_connection.close()


@app.route("/edit_Students/<int:id>", methods=["post", "get"])
def edit_student(id):
    try:
        # Create one connection and query to be re-used for both methods
        # DictCursor type found here:
        # https://mysqlclient.readthedocs.io/user_guide.html#cursor-objects
        # Used so that fetchone returns key:value pairs instead of just a list
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        # Check if house_id is null for the student we wish to edit
        query_null = (
            "SELECT ISNULL(house_id) FROM Students WHERE student_id = %s;"
            % (id)
        )
        cursor.execute(query=query_null)
        house_null = cursor.fetchone()

        if not house_null:
            query = "SELECT * FROM Students WHERE student_id = %s;" % (id)
            cursor.execute(
                query=query,
            )
            student = cursor.fetchone()
            # Find the student's house name and add it to the
            # student dictionary
            house_id = student["house_id"]
            house_query = (
                "SELECT house_name from Houses WHERE house_id = %s;"
                % (house_id)
            )
            cursor.execute(query=house_query)
            house = cursor.fetchone()
            student["house_name"] = house["house_name"]
        else:
            query = "SELECT * FROM Students WHERE student_id = %s;" % (id)
            cursor.execute(query=query)
            student = cursor.fetchone()
            student["house_name"] = ""
        # Create the form. If we are sending a POST request, create the form
        # appropriately.
        # Unpack the data in students for use as default, pre-filled values
        form = custom_forms.UpdateStudentForm(
            request.form if request.method == "POST" else None, **student
        )

        if request.method == "GET":
            # Structured these into a dictionary, to pass in as **kwargs
            values = {
                "title": "Students",
                "records": student,
                "fkey": list(student.keys()),
                "update_form": form,
            }
            return render_template("edit_students.j2", **values)

        if request.method == "POST":
            # Get form data
            first_name = form.first_name.data
            last_name = form.last_name.data
            house_name = form.house_name.data
            level_attending = form.level_attending.data

            if house_name == "":
                update_query = """
                UPDATE Students SET
                    first_name = %s,
                    last_name = %s,
                    house_id = NULL,
                    level_attending = %s
                WHERE student_id = %s;
                """
                cursor.execute(
                    update_query,
                    (first_name, last_name, level_attending, id),
                )
                db_connection.commit()
                return redirect("/students")
            else:
                # Derive house_id from house_name
                house_query = """
                    SELECT house_id FROM Houses WHERE house_name = %s;"""
                cursor.execute(house_query, (house_name,))
                house_id = cursor.fetchone()
                house_id = house_id["house_id"]

                # Update the database with the request
                update_query = """
                UPDATE Students SET
                    first_name = %s,
                    last_name = %s,
                    house_id = %s,
                    level_attending = %s
                WHERE student_id = %s;
                """
                cursor.execute(
                    update_query,
                    (first_name, last_name, house_id, level_attending, id),
                )
                db_connection.commit()

                return redirect("/students")

    except Exception as e:
        return e
    finally:
        cursor.close()
        db_connection.close()


@app.route("/professors")
def professors():
    """Displays the Professors page and associated CRUD operations"""
    try:
        db_connection = db.connect_to_database()
        query = "SELECT * FROM Professors;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        professors = cursor.fetchall()
        values = {
            "title": "Professors",
            "records": professors,
            "new_prof": custom_forms.NewProfessorForm(),
            "update_form": custom_forms.UpdateProfessorForm(),
        }
        return render_template("professors.j2", **values)
    except MySQLdb.Error as e:
        # Catch and display any DB errors
        return e
    finally:
        # Close the cursor and connection.
        cursor.close()
        db_connection.close()


@app.route("/houses")
def houses():
    """Displays the Houses page and associated CRUD operations"""
    try:
        db_connection = db.connect_to_database()
        query = "SELECT * FROM Houses;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        houses = cursor.fetchall()
        values = {
            "title": "Houses",
            "records": houses,
            "new_house": custom_forms.NewHouseForm(),
            "update_form": custom_forms.UpdateHouseForm(),
        }
        return render_template("houses.j2", **values)
    except MySQLdb.Error as e:
        # Catch and display any DB errors
        return e
    finally:
        # Close the cursor and connection.
        cursor.close()
        db_connection.close()


@app.route("/subjects")
def subjects():
    """Displays the Subjects page and associated CRUD operations"""
    try:
        db_connection = db.connect_to_database()
        query = "SELECT * FROM Subjects;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        subjects = cursor.fetchall()
        values = {
            "title": "Subjects",
            "records": subjects,
            "new_sub": custom_forms.NewSubjectForm(),
            "update_form": custom_forms.UpdateSubjectForm(),
        }
        return render_template("subjects.j2", **values)
    except MySQLdb.Error as e:
        # Catch and display any DB errors
        return e
    finally:
        # Close the cursor and connection.
        cursor.close()
        db_connection.close()


@app.route("/classes")
def classes():
    """Displays the Classes page and associated CRUD operations"""
    try:
        db_connection = db.connect_to_database()
        query = "SELECT * FROM Classes;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        classes = cursor.fetchall()
        values = {
            "title": "Classes",
            "records": classes,
            "new_class": custom_forms.NewClassForm(),
            "update_form": custom_forms.UpdateClassForm(),
        }
        return render_template("classes.j2", **values)
    except MySQLdb.Error as e:
        # Catch and display any DB errors
        return e
    finally:
        cursor.close()
        db_connection.close()


@app.route("/registrations")
def registrations():
    """Displays the Class_Registrations page and associated CRUD operations"""
    try:
        db_connection = db.connect_to_database()
        query = "SELECT * FROM Class_Registrations;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        registrations = cursor.fetchall()
        values = {
            "title": "Registrations",
            "records": registrations,
            "buttons": [
                "Find Students in a Class",
                "Find Class Registrations for a Student",
            ],
            "new_reg": custom_forms.NewRegistrationForm(),
        }
        return render_template("registrations.j2", **values)
    except MySQLdb.Error as e:
        # Catch and display any DB errors
        return e
    finally:
        # Close the cursor and connection.
        cursor.close()
        db_connection.close()
