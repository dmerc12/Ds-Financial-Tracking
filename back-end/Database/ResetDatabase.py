from datetime import timedelta, datetime

import bcrypt

from Database.config import Connection


def truncate_table(table_name):
    connection = Connection.db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(f'TRUNCATE TABLE financial_tracker.{table_name} restart identity cascade;')
        connection.commit()
        print(f'{table_name} truncated successfully!')
    except Exception as error:
        print(f'Error truncating {table_name}: {str(error)}')
    finally:
        connection.close()

if __name__ == "__main__":
    tables_to_reset = ["User", "Session", "Expense", "Deposit", "Category"]

    for table in tables_to_reset:
        truncate_table(table)

    main_connection = Connection.db_connection()
    main_cursor = main_connection.cursor()

    test_password = bcrypt.hashpw("test".encode(), bcrypt.gensalt()).decode()
    main_cursor.execute(f"INSERT INTO financial_tracker.User (user_id, email, passwrd) VALUES (-1, 'test@email.com', "
                        f"'${test_password}');")

    main_cursor.execute(f"INSERT INTO financial_tracker.User (user_id, email, passwrd) "
                        f"VALUES (-2, 'deleteallsessions@email.com', "
                        f"'${test_password}');")

    main_cursor.execute("INSERT INTO financial_tracker.Session (session_id, user_id, expiration) "
                        "VALUES ('-1', -1, '2022-1-1 1:30:45');")

    main_cursor.execute("INSERT INTO financial_tracker.Session (session_id, user_id, expiration) "
                        "VALUES ('-2', -1, '2028-1-1 1:30:45');")

    main_cursor.execute("INSERT INTO financial_tracker.CATEGORY (category_id, user_id, grp, category_name) VALUES "
                        "(-1, -1, 'b', 'test category');")
    main_cursor.execute("INSERT INTO financial_tracker.CATEGORY (category_id, user_id, grp, category_name) VALUES "
                        "(-2, -1, 'b', 'unused category');")
    print("Test category created successfully!")

    main_connection.commit()
    main_connection.close()
