from Database.config import Connection


def truncate_table(table_name):
    connection = Connection.db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(f'DELETE FROM {table_name}')
        cursor.execute(f"UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name='{table_name}'")
        connection.commit()
        print(f"Auto-increment ID reset for {table}")
        print(f'{table_name} truncated successfully!')
    except Exception as error:
        print(f'Error truncating {table_name}: {str(error)}')
    finally:
        connection.close()

if __name__ == "__main__":
    tables_to_reset = ["Expense", "Deposit", "Category"]

    for table in tables_to_reset:
        truncate_table(table)

    main_connection = Connection.db_connection()
    main_cursor = main_connection.cursor()

    main_cursor.execute("INSERT INTO CATEGORY (category_id, category_name) VALUES (-1, 'test category')")
    print("Test category created successfully!")

    main_connection.commit()
    main_connection.close()
