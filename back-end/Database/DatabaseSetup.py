from Database.config import Connection


def create_table(sql, table_name):
    connection = Connection.db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(sql)
        connection.commit()
        print(f'{table_name} table successfully created!')
    except Exception as error:
        print(f'Error creating {table_name} table: {str(error)}')
    finally:
        connection.close()

if __name__ == "__main__":
    category_table_sql = '''
        CREATE TABLE Category (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT
        )
    '''

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

    create_table(category_table_sql, "Category")
    create_table(expense_table_sql, "Expense")
    create_table(deposit_table_sql, "Deposit")

    print("Database setup successfully!")
