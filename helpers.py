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


def get_pks_from_table(table_name: str, primary_key_name: str) -> list[int]:
    """Return a list of primary keys, given the table name and primary key name.

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

