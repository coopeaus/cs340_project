import MySQLdb
import database.db_connector as db


def get_house_id_from_name(house_name: str) -> int:
    """Given a house_name, return the house_id

    :param house_name: A Hogwarts house name
    :type house_name: str
    :raises e: MySQLdb errors
    :return: The house_id number corresponding to the house_name
    :rtype: int
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor()

        # The SQL query used to find the house_id
        house_query = """
        SELECT house_id FROM Houses WHERE house_name = %s;
        """
        cursor.execute(house_query, (house_name,))
        house_id = cursor.fetchone()

        return house_id[0]

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        # Clean up connections
        cursor.close()
        db_connection.close()


def get_house_name_from_id(house_id: int) -> str:
    """Given a house_id, return the house_name

    :param house_id: A Hogwarts house house_id
    :type house_id: int
    :raises e: MySQLdb errors
    :return: The house_name corresponding to the house_id
    :rtype: str
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor()

        # The SQL query used to find the house_name
        house_query = """
        SELECT house_name from Houses WHERE house_id = %s;
        """ % (
            house_id
        )
        cursor.execute(house_query)
        house = cursor.fetchone()

        return house[0]

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        # Clean up connections
        cursor.close()
        db_connection.close()


def get_professor_id_from_name(first_name: str, last_name: str) -> int:
    """Given first_name and last_name, return the professor_id

    :param first_name and last_name: A Hogwarts professor name
    :type first_name and last_name: str
    :raises e: MySQLdb errors
    :return: The professor_id number corresponding to
            the first_name and last_name
    :rtype: int
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor()

        # The SQL query used to find the professor_id
        professor_query = """
        SELECT professor_id FROM Professors WHERE first_name = %s
        AND last_name = %s;
        """
        cursor.execute(
            professor_query,
            (
                first_name,
                last_name,
            ),
        )
        professor_id = cursor.fetchone()

        return professor_id[0]

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        # Clean up connections
        cursor.close()
        db_connection.close()


def get_professor_name_from_id(professor_id: int) -> str:
    """Given a professor_id, return the professor_name

    :param professor_id: A Hogwarts professor professor_id
    :type professor_id: int
    :raises e: MySQLdb errors
    :return: The professor_name corresponding to the professor_id
    :rtype: str
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor()

        # The SQL query used to find the professor_name
        professor_query = """
        SELECT first_name, last_name from Professors
        WHERE professor_id = %s;
        """ % (
            professor_id
        )
        cursor.execute(professor_query)
        professor = cursor.fetchone()
        professor_name = professor[0] + " " + professor[1]

        return professor_name

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        # Clean up connections
        cursor.close()
        db_connection.close()


def get_subject_id_from_name(subject_name: str) -> int:
    """Given a subject_name, return the subject_id

    :param subject_name: A Hogwarts subject name
    :type subject_name: str
    :raises e: MySQLdb errors
    :return: The subject_id number corresponding to the subject_name
    :rtype: int
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor()

        # The SQL query used to find the subject_id
        subject_query = """
        SELECT subject_id FROM Subjects WHERE subject_name = %s;
        """
        cursor.execute(subject_query, (subject_name,))
        subject_id = cursor.fetchone()

        return subject_id[0]

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        # Clean up connections
        cursor.close()
        db_connection.close()


def get_subject_name_from_id(subject_id: int) -> str:
    """Given a subject_id, return the subject_name

    :param subject_id: A Hogwarts subject subject_id
    :type subject_id: int
    :raises e: MySQLdb errors
    :return: The subject_name corresponding to the subject_id
    :rtype: str
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor()

        # The SQL query used to find the subject_name
        subject_query = """
        SELECT subject_name from Subjects WHERE subject_id = %s;
        """ % (
            subject_id
        )
        cursor.execute(subject_query)
        subject = cursor.fetchone()

        return subject[0]

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        # Clean up connections
        cursor.close()
        db_connection.close()


def get_student_id_from_name(first_name: str, last_name: str) -> int:
    """Given first_name and last_name, return the student_id

    :param first_name and last_name: A Hogwarts student name
    :type first_name and last_name: str
    :raises e: MySQLdb errors
    :return: The student_id number corresponding to
            the first_name and last_name
    :rtype: int
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor()

        # The SQL query used to find the student_id
        student_query = """
        SELECT student_id FROM Students WHERE first_name = %s
        AND last_name = %s;
        """
        cursor.execute(
            student_query,
            (
                first_name,
                last_name,
            ),
        )
        student_id = cursor.fetchone()

        return student_id[0]

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        # Clean up connections
        cursor.close()
        db_connection.close()


def get_student_name_from_id(student_id: int) -> str:
    """Given a student_id, return the student_name

    :param professor_id: A Hogwarts professor student_id
    :type student_id: int
    :raises e: MySQLdb errors
    :return: The student_name corresponding to the student_id
    :rtype: str
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor()

        # The SQL query used to find the student_name
        student_query = """
        SELECT first_name, last_name from Students
        WHERE student_id = %s;
        """ % (
            student_id
        )
        cursor.execute(student_query)
        student = cursor.fetchone()
        student_name = student[0] + " " + student[1]

        return student_name

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        # Clean up connections
        cursor.close()
        db_connection.close()


def get_class_id_from_class_detail(
    subject_id: int, class_level: int, professor_id: int
) -> int:
    """Given subject_id, class_level and professor_id, return the class_id

    :param subject_id, class_level and professor_id
    :type subject_id, class_level and professor_id: int
    :raises e: MySQLdb errors
    :return: The class_id number corresponding to
            the subject_id, class_level and professor_id
    :rtype: int
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor()

        # The SQL query used to find the class_id
        class_query = """
        SELECT class_id FROM Classes WHERE subject_id = %s
        AND class_level = %s AND
        (CASE
            WHEN Classes.professor_id IS NOT NULL THEN professor_id = %s
            ELSE ISNULL(professor_id)
        END);
        """
        cursor.execute(
            class_query,
            (
                subject_id,
                class_level,
                professor_id,
            ),
        )
        class_id = cursor.fetchone()

        return class_id[0]

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        # Clean up connections
        cursor.close()
        db_connection.close()


def get_pks_from_table(table_name: str, primary_key_name: str) -> list[int]:
    """Return a list of primary keys, given the table name and primary key
        name.

    :param table_name: The name of the table to get primary keys from.
    :type tablename: str
    :param primary_key_name: The primary key name, ex: 'student_id'
    :type primary_key_name: str
    :return: A list of primary keys for the given table
    :rtype: list[int]
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        # Get Primary Keys
        query = f"""
            SELECT {primary_key_name} from {table_name};
        """
        cursor.execute(query)
        pks_found = cursor.fetchall()
        pks = []

        # fetchall returns a tuple of dicts. Access each item of the tuple,
        # then extract the id numbers
        for pair in pks_found:
            for label, value in pair.items():
                pks.append(value)

        return pks

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        cursor.close()
        db_connection.close()
