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

    category_table_sql = '''
        CREATE TABLE financial_tracker.Category (
            category_id SERIAL PRIMARY KEY,
            category_name TEXT
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
            date DATE,
            description TEXT,
            amount FLOAT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES financial_tracker.Category(category_id)
        );
    '''

    deposit_table_sql = '''
        CREATE TABLE financial_tracker.Deposit (
            deposit_id SERIAL PRIMARY KEY,
            date DATE,
            description TEXT,
            amount FLOAT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES financial_tracker.Category(category_id)
        );
    '''

    create_data(schema_sql, "Financial tracking schema")
    create_data(category_table_sql, "Category table")
    create_data(test_category_1, "Test category 1")
    create_data(test_category_2, "Test category 2")
    create_data(expense_table_sql, "Expense table")
    create_data(deposit_table_sql, "Deposit table")

    print("Database setup successfully!")
