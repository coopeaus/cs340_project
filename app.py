from flask import Flask, render_template
import database.db_connector as db

# Citation for the below config, Routes, and Listener
# Date: 7/23/24
# Adapted from:
# The main idea and organization was adapted from:
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

# Configuration
app = Flask(__name__)
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
    results = cursor.fetchall()
    return render_template("students.j2", students=results)


@app.route("/professors")
def professors():
    return render_template("professors.j2")


@app.route("/houses")
def houses():
    return render_template("houses.j2")


@app.route("/subjects")
def subjects():
    return render_template("subjects.j2")


@app.route("/classes")
def classes():
    return render_template("classes.j2")


# Listener
if __name__ == "__main__":
    app.run(port=65000, debug=True)
