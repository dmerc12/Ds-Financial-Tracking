import logging
from typing import List

from DAL.CategoryDAL.CategoryDALInterface import CategoryDALInterface
from Database.config import Connection
from Entities.Category import Category


class CategoryDALImplementation(CategoryDALInterface):

    def create_category(self, category: Category) -> Category:
        logging.info("Beginning DAL method create category with data: " + str(category.convert_to_dictionary()))
        sql = "INSERT INTO Category (category_name) VALUES (?) RETURNING category_id"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (category.category_name,))
        category.category_id = cursor.fetchone()[0]
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method create category with result: " + str(category.convert_to_dictionary()))
        return category

    def get_category(self, category_id: int) -> Category:
        logging.info("Beginning DAL method get category with category ID: " + str(category_id))
        sql = "SELECT * FROM Category WHERE category_id=?"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (category_id,))
        category_info = cursor.fetchone()
        cursor.close()
        connection.close()
        if category_info is None:
            category = Category(0, '')
            logging.info("Finishing DAL method get category, category not found")
            return category
        else:
            category = Category(*category_info)
            logging.info("Finishing DAL method get category with category: " + str(category.convert_to_dictionary()))
            return category

    def get_all_categories(self) -> List[Category]:
        logging.info("Beginning DAL method get all categories")
        sql = "SELECT * FROM Category"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        category_records = cursor.fetchall()
        categories = []
        for category in category_records:
            category = Category(*category)
            categories.append(category)
            logging.info("Finishing DAL method get all categories with result: " +
                         str(category.convert_to_dictionary()))
        cursor.close()
        connection.commit()
        connection.close()
        return categories

    def update_category(self, category: Category) -> Category:
        logging.info("Beginning DAL method update category with data: " + str(category.convert_to_dictionary()))
        sql = "UPDATE Category SET category_name=? WHERE category_id=?"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (category.category_name, category.category_id))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method update category with result: " + str(category.convert_to_dictionary()))
        return category

    def delete_category(self, category_id: int) -> bool:
        logging.info("Beginning DAL method delete category with category ID: " + str(category_id))
        sql = "DELETE FROM Category WHERE category_id=?"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (category_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete category")
        return True
