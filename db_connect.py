import psycopg
from psycopg.rows import dict_row
from functools import wraps


def db_connect(database: str):
    """
        Decorator used to connect to PostgreSQL database. This will add cursor object as keyword argument and returned
        with the wrapped function.

    Args:
        database: str: Database name to which the connection will be made.

    Returns:
        None: None

    """

    def method_decorator(fns):
        @wraps(fns)
        def wrapper(*args, **kwargs):
            db_config = {
                "host": "localhost",
                "dbname": database,
                "user": "postgres",
                "password": "postgres",
                "port": "5432"
            }
            with psycopg.connect(**db_config) as connection:
                with connection.cursor(row_factory=dict_row) as cursor:
                    try:
                        kwargs["cursor"] = cursor
                        return fns(*args, **kwargs)
                    except Exception as e:
                        print(f"[Error]: Transacting while communicating to database. The detailed are: {e}")
                        raise

        return wrapper

    return method_decorator


if __name__ == '__main__':
    @db_connect("postgres")
    def test(test_var: str, cursor: any = None) -> dict:
        """
            A Test function to test the database connection and get the details from the database.

        Args:
            test_var: str: Test_variable for printing
            cursor: any: Cursor object.

        Returns:
            dict: Details from database.

        """
        print(test_var)
        sql_command = f'SELECT * FROM "public"."Test_Table" WHERE id = 1;'
        cursor.execute(sql_command)
        return cursor.fetchall()


    result = test("test_variable")
    print(result)
