from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
import MySQLdb
import MySQLdb.cursors
import secrets
import custom_forms
import database.db_connector as db
import helpers
from route_helpers import delete_record

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
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)
        form = custom_forms.NewStudentForm(
            request.form if request.method == "POST" else None
        )

        # Get house choices for the house form
        query_house_names = "SELECT house_name FROM Houses;"
        cursor = db.execute_query(
            db_connection=db_connection, query=query_house_names
        )
        house_names = cursor.fetchall()
        hname_choices = [
            house_name["house_name"] for house_name in house_names
        ]
        hname_choices.insert(0, "")
        form.house_name.choices = hname_choices

        # Handle post requests
        if request.method == "POST":

            if form.house_name.data == "":
                house_id = None
            else:
                house_id = helpers.get_house_id_from_name(form.house_name.data)

            # Insert the new student data
            query = """
            INSERT INTO Students (first_name, last_name, house_id,
            level_attending) VALUES (%s, %s,%s,%s);
            """
            cursor.execute(
                query,
                (
                    form.first_name.data,
                    form.last_name.data,
                    house_id,
                    form.level_attending.data,
                ),
            )

            # Commit changes
            db_connection.commit()
            return redirect("/students")

        # Handle GET requests
        elif request.method == "GET":
            query = """
            SELECT Students.student_id, Students.first_name,
            Students.last_name, Houses.house_name AS house_name,
            Students.level_attending FROM Students LEFT JOIN Houses
            ON Students.house_id = Houses.house_id;
            """
            cursor.execute(query=query)
            students = cursor.fetchall()

            # Structured these into a dictionary, to pass in as **kwargs
            values = {
                "title": "Students",
                "records": students,
                "fkey": list(students[0].keys())[0],
                "enroll_form": form,
            }
            return render_template("students.j2", **values)

    except Exception as e:
        print(e)
        return e

    finally:
        # Close the cursor and db_connection due to stability issues
        cursor.close()
        db_connection.close()


@app.route("/delete_Students/<int:id>")
def delete_student(id: int):
    """Remove a specific record from the Students table

    :param id: The student_id for the Student record to delete
    :type id: int
    """
    delete_record(id=id, table_name="Students", primary_key_name="student_id")
    return redirect("/students")


@app.route("/edit_Students/<int:id>", methods=["post", "get"])
def edit_student(id: int):
    try:
        # Create one connection and query to be re-used for both methods
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        query = "SELECT * FROM Students WHERE student_id = %s;" % (id)
        cursor.execute(
            query=query,
        )
        student = cursor.fetchone()

        # Find the student's house name and add it to the
        # student dictionary
        house_id = student["house_id"]
        if house_id:
            student["house_name"] = helpers.get_house_name_from_id(house_id)
        else:
            student["house_name"] = None

        # Create the form. If we are sending a POST request, create the form
        # appropriately.
        # Unpack the data in students for use as default, pre-filled values
        form = custom_forms.UpdateStudentForm(
            request.form if request.method == "POST" else None, **student
        )

        # Get house names for the form choices
        query_house_names = "SELECT house_name FROM Houses;"
        cursor = db.execute_query(
            db_connection=db_connection, query=query_house_names
        )
        house_names = cursor.fetchall()
        hname_choices = [
            house_name["house_name"] for house_name in house_names
        ]
        hname_choices.insert(0, "")

        form.house_name.choices = hname_choices

        # Handle GET requests
        if request.method == "GET":
            # Structured these into a dictionary, to pass in as **kwargs
            values = {
                "title": "Students",
                "records": student,
                "fkey": list(student.keys()),
                "update_form": form,
            }
            return render_template("edit_students.j2", **values)

        # Handle POST requests
        if request.method == "POST":
            # Support for nullable house_id foreign key.
            if form.house_name.data == "":
                house_id = None
            else:
                house_id = helpers.get_house_id_from_name(form.house_name.data)

            # Query used to update a Student
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
                (
                    form.first_name.data,
                    form.last_name.data,
                    house_id,
                    form.level_attending.data,
                    id,
                ),
            )

            # Save changes to DB
            db_connection.commit()
            return redirect("/students")

    except Exception as e:
        print(e)
        return e

    finally:
        cursor.close()
        db_connection.close()


@app.route("/professors", methods=["post", "get"])
def professors():
    """Displays the Professors page and associated CRUD operations"""
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        if request.method == "POST":
            form = custom_forms.NewProfessorForm(request.form)

            # Insert the new professor data
            query = """
            INSERT INTO Professors (first_name, last_name)
            VALUES (%s, %s);
            """
            cursor.execute(
                query,
                (
                    form.first_name.data,
                    form.last_name.data,
                ),
            )

            # Commit changes
            db_connection.commit()
            return redirect("/professors")

        elif request.method == "GET":
            query = "SELECT * FROM Professors;"
            cursor.execute(query=query)
            professors = cursor.fetchall()

            # Structured these into a dictionary, to pass in as **kwargs
            values = {
                "title": "Professors",
                "records": professors,
                "fkey": list(professors[0].keys())[0],
                "new_prof": custom_forms.NewProfessorForm(),
                "update_form": custom_forms.UpdateProfessorForm(),
            }

            return render_template("professors.j2", **values)

    except Exception as e:
        print(e)
        return e

    finally:
        # Close the cursor and db_connection due to stability issues
        cursor.close()
        db_connection.close()


@app.route("/delete_Professors/<int:id>")
def delete_professor(id: int):
    """Remove a specific record from the Professors table

    :param id: The professor_id for the Professor record to delete
    :type id: int
    """
    delete_record(
        id=id, table_name="Professors", primary_key_name="professor_id"
    )
    return redirect("/professors")


@app.route("/edit_Professors/<int:id>", methods=["post", "get"])
def edit_professor(id: int):
    try:
        # Create one connection and query to be re-used for both methods
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        query = "SELECT * FROM Professors WHERE professor_id = %s;" % (id)
        cursor.execute(
            query=query,
        )
        professor = cursor.fetchone()

        # Create the form. If we are sending a POST request, create the form
        # appropriately.
        # Unpack the data in professors for use as default, pre-filled values
        form = custom_forms.UpdateProfessorForm(
            request.form if request.method == "POST" else None, **professor
        )

        if request.method == "GET":
            # Structured these into a dictionary, to pass in as **kwargs
            values = {
                "title": "Professors",
                "records": professor,
                "fkey": list(professor.keys()),
                "update_form": form,
            }
            return render_template("edit_professors.j2", **values)

        if request.method == "POST":
            # Query used to update a Professor
            update_query = """
            UPDATE Professors SET
                first_name = %s,
                last_name = %s
            WHERE professor_id = %s;
            """
            cursor.execute(
                update_query,
                (
                    form.first_name.data,
                    form.last_name.data,
                    id,
                ),
            )

            # Save changes to DB
            db_connection.commit()
            return redirect("/professors")

    except Exception as e:
        print(e)
        return e

    finally:
        cursor.close()
        db_connection.close()


@app.route("/houses", methods=["post", "get"])
def houses():
    """Displays the Houses page and associated CRUD operations"""
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)
        form = custom_forms.NewHouseForm(
            request.form if request.method == "POST" else None
        )

        # Get professor names for the drop down menu choices
        query_professor_names = """
        SELECT CONCAT(Professors.first_name, ' ', Professors.last_name)
        AS professor_name FROM Professors;
        """
        cursor = db.execute_query(
            db_connection=db_connection, query=query_professor_names
        )
        professor_names = cursor.fetchall()
        pname_choices = [
            professor_name["professor_name"]
            for professor_name in professor_names
        ]
        pname_choices.insert(0, "")
        form.head_of_house.choices = pname_choices

        # Handle POST requests
        if request.method == "POST":

            if form.head_of_house.data == "":
                head_of_house = None
            else:
                first_name, last_name = form.head_of_house.data.split()
                head_of_house = helpers.get_professor_id_from_name(
                    first_name, last_name
                )

            # Insert the new house data
            query = """
            INSERT INTO Houses
                (head_of_house, house_name, house_animal, house_colors)
            VALUES (%s, %s, %s, %s);
            """
            cursor.execute(
                query,
                (
                    head_of_house,
                    form.house_name.data,
                    form.house_animal.data,
                    form.house_colors.data,
                ),
            )

            # Commit changes
            db_connection.commit()
            return redirect("/houses")

        # Handle GET requests
        elif request.method == "GET":
            query = """
            SELECT Houses.house_id,
            CONCAT(Professors.first_name, ' ', Professors.last_name)
            AS head_of_house, Houses.house_name,
            Houses.house_animal, Houses.house_colors
            FROM Houses LEFT JOIN Professors
            ON Houses.head_of_house = Professors.professor_id;
            """
            cursor = db.execute_query(db_connection=db_connection, query=query)
            houses = cursor.fetchall()

            values = {
                "title": "Houses",
                "records": houses,
                "fkey": list(houses[0].keys())[0],
                "new_house": form,
            }
            return render_template("houses.j2", **values)

    except Exception as e:
        print(e)
        return e

    finally:
        # Close the cursor and db_connection due to stability issues
        cursor.close()
        db_connection.close()


@app.route("/delete_Houses/<int:id>")
def delete_house(id: int):
    """Remove a specific record from the Houses table

    :param id: The house_id for the House record to delete
    :type id: int
    """
    delete_record(id=id, table_name="Houses", primary_key_name="house_id")
    return redirect("/houses")


@app.route("/edit_Houses/<int:id>", methods=["post", "get"])
def edit_house(id: int):
    try:
        # Create one connection and query to be re-used for both methods
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        query = "SELECT * FROM Houses WHERE house_id = %s;" % (id)
        cursor.execute(
            query=query,
        )
        house = cursor.fetchone()

        # Find the head_of_house's name and add it to the
        # house dictionary
        professor_id = house["head_of_house"]
        if professor_id:
            house["head_of_house"] = helpers.get_professor_name_from_id(
                professor_id
            )
        else:
            house["head_of_house"] = None

        # Create the form. If we are sending a POST request, create the form
        # appropriately.
        # Unpack the data in house for use as default, pre-filled values
        form = custom_forms.UpdateHouseForm(
            request.form if request.method == "POST" else None, **house
        )

        # Get professor names for dropdown menu choices
        query_professor_names = """
        SELECT CONCAT(Professors.first_name, ' ', Professors.last_name)
        AS professor_name FROM Professors;
        """
        cursor = db.execute_query(
            db_connection=db_connection, query=query_professor_names
        )
        professor_names = cursor.fetchall()
        pname_choices = [
            professor_name["professor_name"]
            for professor_name in professor_names
        ]
        pname_choices.insert(0, "")

        form.head_of_house.choices = pname_choices

        # Handle GET requests
        if request.method == "GET":
            # Structured these into a dictionary, to pass in as **kwargs
            values = {
                "title": "Houses",
                "records": house,
                "fkey": list(house.keys()),
                "update_form": form,
            }
            return render_template("edit_houses.j2", **values)

        # Handle POST requests
        if request.method == "POST":
            # Support for nullable professor_id foreign key.
            if form.head_of_house.data == "":
                head_of_house = None
            else:
                first_name, last_name = form.head_of_house.data.split()
                head_of_house = helpers.get_professor_id_from_name(
                    first_name, last_name
                )

            # Query used to update a House
            update_query = """
            UPDATE Houses SET
                head_of_house = %s,
                house_name = %s,
                house_animal = %s,
                house_colors = %s
            WHERE house_id = %s;
            """
            cursor.execute(
                update_query,
                (
                    head_of_house,
                    form.house_name.data,
                    form.house_animal.data,
                    form.house_colors.data,
                    id,
                ),
            )

            # Save changes to DB
            db_connection.commit()
            return redirect("/houses")

    except Exception as e:
        print(e)
        return e

    finally:
        cursor.close()
        db_connection.close()


@app.route("/subjects", methods=["post", "get"])
def subjects():
    """Displays the Subjects page and associated CRUD operations"""
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        # Create the form
        form = custom_forms.NewSubjectForm(request.form)

        if request.method == "POST":
            # Insert the new professor data
            query = """
            INSERT INTO Subjects (subject_name, core_elective)
            VALUES (%s, %s);
            """
            cursor.execute(
                query,
                (
                    form.subject_name.data,
                    form.core_elective.data,
                ),
            )

            # Commit changes
            db_connection.commit()
            return redirect("/subjects")

        elif request.method == "GET":
            query = "SELECT * FROM Subjects;"
            cursor.execute(query=query)
            subjects = cursor.fetchall()

            # Structured these into a dictionary, to pass in as **kwargs
            values = {
                "title": "Subjects",
                "records": subjects,
                "fkey": list(subjects[0].keys())[0],
                "new_sub": form,
            }
            return render_template("subjects.j2", **values)

    except Exception as e:
        print(e)
        return e

    finally:
        # Close the cursor and db_connection due to stability issues
        cursor.close()
        db_connection.close()


@app.route("/delete_Subjects/<int:id>")
def delete_subject(id: int):
    """Remove a specific record from the Subjects table

    :param id: The subject_id for the Subject record to delete
    :type id: int
    """
    delete_record(id=id, table_name="Subjects", primary_key_name="subject_id")
    return redirect("/subjects")


@app.route("/edit_Subjects/<int:id>", methods=["post", "get"])
def edit_subject(id: int):
    try:
        # Create one connection and query to be re-used for both methods
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        query = "SELECT * FROM Subjects WHERE subject_id = %s;" % (id)
        cursor.execute(
            query=query,
        )
        subject = cursor.fetchone()

        # Create the form. If we are sending a POST request, create the form
        # appropriately.
        # Unpack the data in subject for use as default, pre-filled values
        form = custom_forms.UpdateSubjectForm(
            request.form if request.method == "POST" else None, **subject
        )

        if request.method == "GET":
            # Structured these into a dictionary, to pass in as **kwargs
            values = {
                "title": "Subjects",
                "records": subject,
                "fkey": list(subject.keys()),
                "update_form": form,
            }
            return render_template("edit_subjects.j2", **values)

        if request.method == "POST":
            # Query used to update a Subject
            update_query = """
            UPDATE Subjects SET
                subject_name = %s,
                core_elective = %s
            WHERE subject_id = %s;
            """
            cursor.execute(
                update_query,
                (
                    form.subject_name.data,
                    form.core_elective.data,
                    id,
                ),
            )

            # Save changes to DB
            db_connection.commit()
            return redirect("/subjects")

    except Exception as e:
        print(e)
        return e

    finally:
        cursor.close()
        db_connection.close()


@app.route("/classes", methods=["post", "get"])
def classes():
    """Displays the Classes page and associated CRUD operations"""
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        form = custom_forms.NewClassForm(
            request.form if request.method == "POST" else None
        )

        # Get professor names to prefill dropdown choices
        query_professor_names = """
        SELECT CONCAT(Professors.first_name, ' ', Professors.last_name)
        AS professor_name FROM Professors;
        """
        cursor = db.execute_query(
            db_connection=db_connection, query=query_professor_names
        )
        professor_names = cursor.fetchall()
        pname_choices = [
            professor_name["professor_name"]
            for professor_name in professor_names
        ]
        pname_choices.insert(0, "")

        # Get subject names to prefill dropdown choices
        query_subject_names = """
        SELECT Subjects.subject_name FROM Subjects;
        """
        cursor = db.execute_query(
            db_connection=db_connection, query=query_subject_names
        )
        subject_names = cursor.fetchall()
        sname_choices = [
            subject_name["subject_name"] for subject_name in subject_names
        ]

        form.subject_name.choices = sname_choices
        form.professor_name.choices = pname_choices

        # Handle POST requests
        if request.method == "POST":

            if form.professor_name.data == "":
                professor_id = None
            else:
                first_name, last_name = form.professor_name.data.split()
                professor_id = helpers.get_professor_id_from_name(
                    first_name, last_name
                )
            subject_id = helpers.get_subject_id_from_name(
                form.subject_name.data
            )

            # Insert the new class data
            query = """
            INSERT INTO Classes (subject_id, professor_id, class_level)
            VALUES (%s, %s, %s);
            """
            cursor.execute(
                query,
                (
                    subject_id,
                    professor_id,
                    form.class_level.data,
                ),
            )

            # Commit changes
            db_connection.commit()
            return redirect("/classes")

        # Handle GET requests
        elif request.method == "GET":
            query = """
            SELECT Classes.class_id, Subjects.subject_name AS subject_name,
            CONCAT(Professors.first_name, ' ', Professors.last_name)
            AS professor_name, Classes.class_level
            FROM Classes
            LEFT JOIN Subjects
            ON Classes.subject_id = Subjects.subject_id
            LEFT JOIN Professors
            ON Classes.professor_id = Professors.professor_id;
            """
            cursor.execute(query=query)
            classes = cursor.fetchall()

            # Structured these into a dictionary, to pass in as **kwargs
            values = {
                "title": "Classes",
                "records": classes,
                "fkey": list(classes[0].keys())[0],
                "new_class": form,
            }
            return render_template("classes.j2", **values)

    except Exception as e:
        print(e)
        return e

    finally:
        # Close the cursor and db_connection due to stability issues
        cursor.close()
        db_connection.close()


@app.route("/delete_Classes/<int:id>")
def delete_class(id: int):
    """Remove a specific record from the Classes table

    :param id: The class_id for the Class record to delete
    :type id: int
    """
    delete_record(id=id, table_name="Classes", primary_key_name="class_id")
    return redirect("/classes")


@app.route("/edit_Classes/<int:id>", methods=["post", "get"])
def edit_class(id: int):
    try:
        # Create one connection and query to be re-used for both methods
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        query = """
        SELECT Classes.class_id, Classes.subject_id AS subject_name,
        Classes.professor_id AS professor_name, Classes.class_level
        FROM Classes WHERE class_id = %s;
        """ % (
            id
        )
        cursor.execute(
            query=query,
        )
        target_class = cursor.fetchone()

        # Find the professor_id and subject_id's names and add them to the
        # class dictionary
        professor_id = target_class["professor_name"]
        if professor_id:
            target_class["professor_name"] = (
                helpers.get_professor_name_from_id(professor_id)
            )
        else:
            target_class["professor_name"] = None

        subject_id = target_class["subject_name"]
        target_class["subject_name"] = helpers.get_subject_name_from_id(
            subject_id
        )

        # Create the form. If we are sending a POST request, create the form
        # appropriately.
        # Unpack the data in target_class for use as default, pre-filled values
        form = custom_forms.UpdateClassForm(
            request.form if request.method == "POST" else None, **target_class
        )

        # Get professor names to prefill dropdown choices
        query_professor_names = """
        SELECT CONCAT(Professors.first_name, ' ', Professors.last_name)
        AS professor_name FROM Professors;
        """
        cursor = db.execute_query(
            db_connection=db_connection, query=query_professor_names
        )
        professor_names = cursor.fetchall()
        pname_choices = [
            professor_name["professor_name"]
            for professor_name in professor_names
        ]
        pname_choices.insert(0, "")

        # Get subject names to prefill dropdown choices
        query_subject_names = """
        SELECT Subjects.subject_name FROM Subjects;
        """
        cursor = db.execute_query(
            db_connection=db_connection, query=query_subject_names
        )
        subject_names = cursor.fetchall()
        sname_choices = [
            subject_name["subject_name"] for subject_name in subject_names
        ]

        form.subject_name.choices = sname_choices
        form.professor_name.choices = pname_choices

        # Handle GET requests
        if request.method == "GET":
            # Structured these into a dictionary, to pass in as **kwargs
            values = {
                "title": "Classes",
                "records": target_class,
                "fkey": list(target_class.keys()),
                "update_form": form,
            }
            return render_template("edit_classes.j2", **values)

        # Handle POST requests
        if request.method == "POST":
            # Support for nullable professor_id foreign key.
            if form.professor_name.data == "":
                professor_id = None
            else:
                first_name, last_name = form.professor_name.data.split()
                professor_id = helpers.get_professor_id_from_name(
                    first_name, last_name
                )

            subject_name = form.subject_name.data
            subject_id = helpers.get_subject_id_from_name(subject_name)

            # Query used to update a Subject
            update_query = """
            UPDATE Classes SET
                subject_id = %s,
                professor_id = %s,
                class_level = %s
            WHERE class_id = %s;
            """
            cursor.execute(
                update_query,
                (
                    subject_id,
                    professor_id,
                    form.class_level.data,
                    id,
                ),
            )

            # Save changes to DB
            db_connection.commit()
            return redirect("/classes")

    except Exception as e:
        print(e)
        return e

    finally:
        cursor.close()
        db_connection.close()


@app.route("/registrations", methods=["post", "get"])
def registrations():
    """Displays the Class_Registrations page and associated CRUD operations"""
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        form = custom_forms.NewRegistrationForm(
            request.form if request.method == "POST" else None
        )

        # Get student names for prefilling data
        query_student_names = """
        SELECT CONCAT(Students.first_name, ' ', Students.last_name)
        AS student_name FROM Students;
        """
        cursor = db.execute_query(
            db_connection=db_connection, query=query_student_names
        )
        student_names = cursor.fetchall()
        stname_choices = [
            student_name["student_name"] for student_name in student_names
        ]

        # Get class details for prefilling data
        query_class_details = """
        SELECT CONCAT(Subjects.subject_name, ', ', Classes.class_level, ', ',
        (CASE
            WHEN Classes.professor_id IS NULL THEN 'None'
            ELSE CONCAT(Professors.first_name, ' ', Professors.last_name)
        END)) AS class_detail
        FROM Classes
        LEFT JOIN Subjects
        ON Classes.subject_id = Subjects.subject_id
        LEFT JOIN Professors
        ON Classes.professor_id = Professors.professor_id;
        """
        cursor = db.execute_query(
            db_connection=db_connection, query=query_class_details
        )
        class_details = cursor.fetchall()
        cdetail_choices = [
            class_detail["class_detail"] for class_detail in class_details
        ]

        form.student_name.choices = stname_choices
        form.class_detail.choices = cdetail_choices

        if request.method == "GET":
            # Display the table
            query = """
            SELECT Class_Registrations.student_id,
            CONCAT(Students.first_name, ' ', Students.last_name)
            AS student_name, Class_Registrations.class_id,
            Subjects.subject_name, Classes.class_level,
            (CASE
                WHEN Classes.professor_id IS NULL THEN 'None'
                ELSE CONCAT(Professors.first_name, ' ', Professors.last_name)
            END) AS class_detail
            FROM Class_Registrations
            LEFT JOIN Students
            ON Class_Registrations.student_id = Students.student_id
            LEFT JOIN Classes
            ON Class_Registrations.class_id = Classes.class_id
            LEFT JOIN Subjects
            ON Classes.subject_id = Subjects.subject_id
            LEFT JOIN Professors
            ON Classes.professor_id = Professors.professor_id;
            """
            cursor.execute(query)
            registrations = cursor.fetchall()
            values = {
                "title": "Registrations",
                "records": registrations,
                "new_reg": form,
            }
            return render_template("registrations.j2", **values)

        elif request.method == "POST":

            first_name, last_name = form.student_name.data.split()
            student_id = helpers.get_student_id_from_name(
                first_name, last_name
            )

            subject_name, class_level, professor_name = (
                form.class_detail.data.split(", ")
            )
            subject_id = helpers.get_subject_id_from_name(subject_name)
            if professor_name != "None":
                first_name, last_name = professor_name.split()
                professor_id = helpers.get_professor_id_from_name(
                    first_name, last_name
                )
            else:
                professor_id = None
            class_id = helpers.get_class_id_from_class_detail(
                subject_id, class_level, professor_id
            )

            # INSERT a new Class_Registrations record
            query = """
                INSERT into Class_Registrations (student_id, class_id)
                VALUES (%s, %s);"""
            cursor.execute(query, (student_id, class_id))
            db_connection.commit()
            return redirect("/registrations")

    except Exception as e:
        print(e)
        return e

    finally:
        # Close the cursor and connection.
        cursor.close()
        db_connection.close()


@app.route("/delete_Registrations/<int:student_id>&<int:class_id>")
def delete_registration(student_id: int, class_id: int):
    """Remove a specific record from the Students table

    :param student_id: The student_id for the Class_Registrations record to
                        delete
    :type id: int
    :param class_id: The class_id for the Class_Registrations record to delete
    :type id: int
    """

    # No delete helper here, due to composite primary key.
    try:
        db_connection = db.connect_to_database()
        query = """
            DELETE FROM Class_Registrations WHERE
                student_id = '%s' and class_id = '%s';"""
        cursor = db.execute_query(
            db_connection=db_connection,
            query=query,
            query_params=(student_id, class_id),
        )
        return redirect("/registrations")
    except MySQLdb.Error as e:
        return e
    finally:
        cursor.close()
        db_connection.close()


@app.route(
    "/edit_Registrations/<int:student_id>&<int:class_id>",
    methods=["post", "get"],
)
def edit_registration(student_id: int, class_id: int):
    try:
        # Create one connection and query to be re-used for both methods
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        query = """
        SELECT CONCAT(Students.first_name, ' ', Students.last_name)
        AS student_name,
        CONCAT(Subjects.subject_name, ', ', Classes.class_level, ', ',
        (CASE
            WHEN Classes.professor_id IS NULL THEN 'None'
            ELSE CONCAT(Professors.first_name, ' ', Professors.last_name)
        END)) AS class_detail
        FROM Class_Registrations
        LEFT JOIN Students
        ON Class_Registrations.student_id = Students.student_id
        LEFT JOIN Classes
        ON Class_Registrations.class_id = Classes.class_id
        LEFT JOIN Subjects
        ON Classes.subject_id = Subjects.subject_id
        LEFT JOIN Professors
        ON Classes.professor_id = Professors.professor_id
        WHERE Class_Registrations.student_id = '%s' and
        Class_Registrations.class_id = '%s'
        """
        cursor.execute(query, (student_id, class_id))
        registration = cursor.fetchone()
        registration["student_id"] = student_id
        registration["class_id"] = class_id
        # Create the form. If we are sending a POST request, create the form
        # appropriately.
        # Unpack the data in students for use as default, pre-filled values
        form = custom_forms.UpdateRegistrationForm(
            request.form if request.method == "POST" else None, **registration
        )

        # Get student names for prefilling data
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

        # Get class details for prefilling data
        query_class_details = """
        SELECT CONCAT(Subjects.subject_name, ', ', Classes.class_level, ', ',
        (CASE
            WHEN Classes.professor_id IS NULL THEN 'None'
            ELSE CONCAT(Professors.first_name, ' ', Professors.last_name)
        END)) AS class_detail
        FROM Classes
        LEFT JOIN Subjects
        ON Classes.subject_id = Subjects.subject_id
        LEFT JOIN Professors
        ON Classes.professor_id = Professors.professor_id;
        """
        cursor = db.execute_query(
            db_connection=db_connection, query=query_class_details
        )
        class_details = cursor.fetchall()
        cdetail_choices = [
            class_detail["class_detail"] for class_detail in class_details
        ]

        form.student_name.choices = stname_choices
        form.class_detail.choices = cdetail_choices

        if request.method == "GET":
            # Structured these into a dictionary, to pass in as **kwargs
            values = {
                "title": "Registrations",
                "records": registration,
                "update_form": form,
            }
            return render_template("edit_registrations.j2", **values)

        if request.method == "POST":
            form = custom_forms.UpdateRegistrationForm(request.form)
            first_name, last_name = form.student_name.data.split()
            update_student_id = helpers.get_student_id_from_name(
                first_name, last_name
            )

            subject_name, class_level, professor_name = (
                form.class_detail.data.split(", ")
            )
            subject_id = helpers.get_subject_id_from_name(subject_name)
            if professor_name != "None":
                first_name, last_name = professor_name.split()
                professor_id = helpers.get_professor_id_from_name(
                    first_name, last_name
                )
            else:
                professor_id = None
            update_class_id = helpers.get_class_id_from_class_detail(
                subject_id, class_level, professor_id
            )

            # Query used to update a Class_Registration
            update_query = """
            UPDATE Class_Registrations SET
                student_id = %s,
                class_id = %s
            WHERE student_id = %s and class_id = %s;
            """
            cursor.execute(
                update_query,
                (
                    update_student_id,
                    update_class_id,
                    student_id,
                    class_id,
                ),
            )

            # Save changes to DB
            db_connection.commit()
            return redirect("/registrations")

    except Exception as e:
        print(e)
        return e

    finally:
        cursor.close()
        db_connection.close()
