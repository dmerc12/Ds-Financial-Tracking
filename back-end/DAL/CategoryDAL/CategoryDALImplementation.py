import logging
from typing import List

from DAL.CategoryDAL.CategoryDALInterface import CategoryDALInterface
from Database.config import Connection
from Entities.Category import Category


class CategoryDALImplementation(CategoryDALInterface):

    def create_category(self, category: Category) -> Category:
        logging.info("Beginning DAL method create category with data: " + str(category.convert_to_dictionary()))
        sql = "INSERT INTO Category (category_name) VALUES (?) RETURNING category_id"
        print(sql)
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (category.category_name,))
        category.category_id = cursor.fetchone()[0]
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method create category with result: " + str(category.convert_to_dictionary()))
        return category

    def get_all_categories(self) -> List[Category]:
        pass

    def update_category(self, category: Category) -> Category:
        pass

    def delete_category(self, category_id: int) -> bool:
        pass
