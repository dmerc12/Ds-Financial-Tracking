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
            first_name VARCHAR(36),
            last_name VARCHAR(36),
            email VARCHAR(60),
            passwrd VARCHAR(60)
        );
    '''

    test_user_1 = '''
        INSERT INTO financial_tracker.User (user_id, first_name, last_name, email, passwrd) 
        VALUES (-1, 'test', 'test', 'test@email.com', 'test');
    '''

    session_table_sql = '''
        CREATE TABLE financial_tracker.Session (
            session_id SERIAL PRIMARY KEY,
            user_id INT,
            expires VARCHAR(26),
            CONSTRAINT user_session_fk FOREIGN KEY (user_id) REFERENCES 
            financial_tracker.User(user_id) ON DELETE CASCADE
        );
    '''

    category_table_sql = '''
        CREATE TABLE financial_tracker.Category (
            category_id SERIAL PRIMARY KEY,
            user_id INT,
            category_name TEXT,
            CONSTRAINT user_category_fk FOREIGN KEY (user_id) REFERENCES 
            financial_tracker.User(user_id) ON DELETE CASCADE
        );
    '''

    test_category_1 = '''
        INSERT INTO financial_tracker.CATEGORY (category_id, category_name) VALUES (-1, 'test category');
    '''

    test_category_2 = '''
            INSERT INTO financial_tracker.CATEGORY (category_id, category_name) VALUES (-2, 'unused category');
        '''

    expense_table_sql = '''
        CREATE TABLE financial_tracker.Expense (
            expense_id SERIAL PRIMARY KEY,
            user_id INTEGER,
            category_id INTEGER,
            date DATE,
            description TEXT,
            amount FLOAT,           
            FOREIGN KEY (category_id) REFERENCES financial_tracker.Category(category_id),
            CONSTRAINT user_expense_fk FOREIGN KEY (user_id) REFERENCES 
            financial_tracker.User(user_id) ON DELETE CASCADE
        );
    '''

    deposit_table_sql = '''
        CREATE TABLE financial_tracker.Deposit (
            deposit_id SERIAL PRIMARY KEY,
            user_id INTEGER,
            category_id INTEGER,
            date DATE,
            description TEXT,
            amount FLOAT,
            FOREIGN KEY (category_id) REFERENCES financial_tracker.Category(category_id)
            CONSTRAINT user_deposit_fk FOREIGN KEY (user_id) REFERENCES 
            financial_tracker.User(user_id) ON DELETE CASCADE
        );
    '''

    create_data(schema_sql, "Financial tracking schema")
    create_data(user_table_sql, "User table")
    create_data(test_user_1, "Test user 1")
    create_data(session_table_sql, "Session table")
    create_data(category_table_sql, "Category table")
    create_data(test_category_1, "Test category 1")
    create_data(test_category_2, "Test category 2")
    create_data(expense_table_sql, "Expense table")
    create_data(deposit_table_sql, "Deposit table")

    print("Database setup successfully!")
