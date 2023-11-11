from Database.config import Connection


def drop_table(table_name):
    connection = Connection.db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(f'DROP TABLE IF EXISTS financial_tracker.{table_name};')
        connection.commit()
        print(f'{table_name} table dropped successfully!')
    except Exception as error:
        print(f'Error dropping {table_name} table: {str(error)}')
    finally:
        connection.close()

    try:
        cursor.execute("DROP SCHEMA IF EXISTS financial_tracker CASCADE;")
        connection.commit()
        print("Schema successfully dropped!")
    except Exception as error:
        print(f'Error dropping schema: {str(error)}')
    finally:
        connection.close()


if __name__ == "__main__":
    tables_to_drop = ["User", "Session", "Expense", "Deposit", "Category"]

    for table in tables_to_drop:
        drop_table(table)
