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
            SELECT house_id FROM Houses WHERE house_name = %s;"""
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
        house_query = "SELECT house_name from Houses WHERE house_id = %s;" % (
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


def get_professor_ids() -> list[int]:
    """Return a list of professor_ids

    :return: A list of all current professor_ids
    :rtype: list[int]
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        # Get Professor IDs
        query = """
            SELECT professor_id from Professors;
        """
        cursor.execute(query)
        prof_ids = cursor.fetchall()
        head_of_house_ids = []

        # fetchall returns a tuple of dicts. Access each item of the tuple, then extract
        # the id numbers
        for pair in prof_ids:
            for label, value in pair.items():
                head_of_house_ids.append(value)

        return head_of_house_ids

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        cursor.close()
        db_connection.close()


def get_subject_ids() -> list[int]:
    """Return a list of subject_ids

    :return: A list of all current subject_ids
    :rtype: list[int]
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        # Get Subject IDs
        query = """
            SELECT subject_id from Subjects;
        """
        cursor.execute(query)
        sub_ids_found = cursor.fetchall()
        sub_ids = []

        # fetchall returns a tuple of dicts. Access each item of the tuple, then extract
        # the id numbers
        for pair in sub_ids_found:
            for label, value in pair.items():
                sub_ids.append(value)

        return sub_ids

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        cursor.close()
        db_connection.close()


def get_class_ids() -> list[int]:
    """Return a list of class_ids

    :return: A list of all current class_ids
    :rtype: list[int]
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        # Get Class IDs
        query = """
            SELECT class_id from Classes;
        """
        cursor.execute(query)
        class_ids_found = cursor.fetchall()
        class_ids = []

        # fetchall returns a tuple of dicts. Access each item of the tuple, then extract
        # the id numbers
        for pair in class_ids_found:
            for label, value in pair.items():
                class_ids.append(value)

        return class_ids

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        cursor.close()
        db_connection.close()


def get_student_ids() -> list[int]:
    """Return a list of student_ids

    :return: A list of all current student_ids
    :rtype: list[int]
    """
    try:
        db_connection = db.connect_to_database()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        # Get Class IDs
        query = """
            SELECT student_id from Students;
        """
        cursor.execute(query)
        student_ids_found = cursor.fetchall()
        student_ids = []

        # fetchall returns a tuple of dicts. Access each item of the tuple, then extract
        # the id numbers
        for pair in student_ids_found:
            for label, value in pair.items():
                student_ids.append(value)

        return student_ids

    except MySQLdb.Error as e:
        print(e)
        raise e

    finally:
        cursor.close()
        db_connection.close()