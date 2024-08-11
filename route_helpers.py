import MySQLdb
import MySQLdb.cursors
import database.db_connector as db


def delete_record(id: int, table_name: str, primary_key_name: str):
    """Remove a specific record from the given table

    :param id: The primary key ID for the record to delete
    :type id: int
    :param table_name: The table to delete from
    :type table_name: str
    :param primary_key_name: The primary key name for the table. Ex: 'student_id'
    :type primary_key_name: str
    """

    try:
        db_connection = db.connect_to_database()
        query = f"DELETE FROM {table_name} WHERE {primary_key_name} = '%s';"
        print(query)
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query, (id,))
        db_connection.commit()
        return

    except MySQLdb.Error as e:
        raise e

    finally:
        cursor.close()
        db_connection.close()
