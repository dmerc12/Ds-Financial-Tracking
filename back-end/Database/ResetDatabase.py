from Database.config import Connection


def truncate_table(table_name):
    connection = Connection.db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(f'DELETE FROM {table_name}')
        connection.commit()
        print(f'{table_name} truncated successfully!')
    except Exception as error:
        print(f'Error truncating {table_name}: {str(error)}')
    finally:
        connection.close()

if __name__ == "__main__":
    tables_to_reset = ["Expense", "Deposit", "Category"]

    for table in tables_to_reset:
        truncate_table(table)
