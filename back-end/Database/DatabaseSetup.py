import bcrypt

from Database.config import Connection


def create_data(sql, data_name):
    connection = Connection.db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(sql)
        connection.commit()
        print(f'{data_name} successfully created!')
    except Exception as error:
        print(f'Error creating {data_name}: {str(error)}')
    finally:
        connection.close()

if __name__ == "__main__":
    schema_sql = "CREATE SCHEMA financial_tracker;"

    user_table_sql = '''
        CREATE TABLE financial_tracker.User (
            user_id SERIAL PRIMARY KEY,
            email VARCHAR(60) UNIQUE NOT NULL,
            passwrd TEXT NOT NULL
        );
    '''
    test_password = bcrypt.hashpw("test".encode(), bcrypt.gensalt()).decode()
    test_user_1 = f"INSERT INTO financial_tracker.User (user_id, email, passwrd) " \
                  f"VALUES (-1, 'test@email.com', '${test_password}');"

    test_user_2 = f"INSERT INTO financial_tracker.User (user_id, email, passwrd) " \
                  f"VALUES (-2, 'deleteallsessions@email.com', '${test_password}');"

    session_table_sql = '''
        CREATE TABLE financial_tracker.Session (
            session_id VARCHAR(60) PRIMARY KEY,
            user_id INT NOT NULL,
            expiration TIMESTAMP NOT NULL,
            CONSTRAINT user_session_fk FOREIGN KEY (user_id) REFERENCES 
            financial_tracker.User(user_id) ON DELETE CASCADE
        );
    '''

    test_session_1 = "INSERT INTO financial_tracker.Session (session_id, user_id, expiration) " \
                     "VALUES ('-1', -1, '2022-1-1 1:30:45');"

    test_session_2 = "INSERT INTO financial_tracker.Session (session_id, user_id, expiration) " \
                     "VALUES ('-2', -1, '2028-1-1 1:30:45');"

    category_table_sql = '''
        CREATE TABLE financial_tracker.Category (
            category_id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            grp CHAR(1) NOT NULL,
            category_name TEXT UNIQUE NOT NULL,
            CONSTRAINT user_category_fk FOREIGN KEY (user_id) REFERENCES 
            financial_tracker.User(user_id) ON DELETE CASCADE
        );
    '''

    test_category_1 = '''
        INSERT INTO financial_tracker.CATEGORY (category_id, user_id, grp, category_name) 
        VALUES (-1, -1, 'b', 'test category');
    '''

    test_category_2 = '''
        INSERT INTO financial_tracker.CATEGORY (category_id, user_id, grp, category_name) 
        VALUES (-2, -2, 'b', 'unused category');
    '''

    expense_table_sql = '''
        CREATE TABLE financial_tracker.Expense (
            expense_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            date DATE NOT NULL,
            description TEXT NOT NULL,
            amount FLOAT NOT NULL,           
            FOREIGN KEY (category_id) REFERENCES financial_tracker.Category(category_id),
            CONSTRAINT user_expense_fk FOREIGN KEY (user_id) REFERENCES 
            financial_tracker.User(user_id) ON DELETE CASCADE
        );
    '''

    deposit_table_sql = '''
        CREATE TABLE financial_tracker.Deposit (
            deposit_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            date DATE NOT NULL,
            description TEXT NOT NULL,
            amount FLOAT NOT NULL,
            FOREIGN KEY (category_id) REFERENCES financial_tracker.Category(category_id),
            CONSTRAINT user_deposit_fk FOREIGN KEY (user_id) REFERENCES 
            financial_tracker.User(user_id) ON DELETE CASCADE
        );
    '''

    create_data(schema_sql, "Financial tracking schema")
    create_data(user_table_sql, "User table")
    create_data(test_user_1, "Test user 1")
    create_data(test_user_2, "Test user 2")
    create_data(session_table_sql, "Session table")
    create_data(test_session_1, "test session")
    create_data(category_table_sql, "Category table")
    create_data(test_category_1, "Test category 1")
    create_data(test_category_2, "Test category 2")
    create_data(expense_table_sql, "Expense table")
    create_data(deposit_table_sql, "Deposit table")

    print("Database setup successfully!")
