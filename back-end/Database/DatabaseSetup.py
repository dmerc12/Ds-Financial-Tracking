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
    category_table_sql = '''
        CREATE TABLE Category (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT
        )
    '''

    # test_category = '''
    #     INSERT INTO CATEGORY (category_id, category_name) VALUES (-1, 'test category')
    # '''

    expense_table_sql = '''
        CREATE TABLE Expense (
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE,
            description TEXT,
            amount FLOAT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES Category(category_id)
        )
    '''

    deposit_table_sql = '''
        CREATE TABLE Deposit (
            deposit_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE,
            description TEXT,
            amount FLOAT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES Category(category_id)
        )
    '''

    create_data(category_table_sql, "Category table")
    create_data(test_category, "Test category")
    create_data(expense_table_sql, "Expense table")
    create_data(deposit_table_sql, "Deposit table")

    print("Database setup successfully!")
