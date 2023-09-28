import logging
from typing import List

from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from SAL.CategorySAL.CategorySALInterface import CategorySALInterface
from Entities.Category import Category
from Entities.CustomError import CustomError

class CategorySALImplementation(CategorySALInterface):

    def __init__(self, category_dao: CategoryDALImplementation):
        self.category_dao = category_dao

    def create_category(self, category: Category) -> Category:
        logging.info("Beginning SAL method create category with data: " + str(category.convert_to_dictionary()))
        existing_categories = self.category_dao.get_all_categories()
        for existing_category in existing_categories:
            if existing_category.category_name == category.category_name:
                logging.warning("Error in SAL method create category, category already exists")
                raise CustomError("A category with this name already exists, please try again!")
        if category.category_name == '':
            logging.warning("Error in SAL method create category, category name empty")
            raise CustomError("The category name field cannot be left empty, please try again!")
        elif type(category.category_name) != str:
            logging.warning("Error in SAL method create category, category name not a string")
            raise CustomError("The category name field must be a string, please try again!")
        else:
            self.category_dao.create_category(category)
            logging.info("Finishing SAL method create category with result: " + str(category.convert_to_dictionary()))
            return category


    def get_category(self, category_id: int) -> Category:
        logging.info("Beginning SAL method get category with category ID: " + str(category_id))
        if type(category_id) != int:
            logging.warning("Error in SAL method get category, category ID not an integer")
            raise CustomError("The category ID field must be an integer, please try again!")
        else:
            category = self.category_dao.get_category(category_id)
            if category.category_id == 0 and category.category_name == '':
                logging.warning("Error in SAL method get category, category not found")
                raise CustomError("Category not found, please try again!")
            else:
                logging.info("Finishing SAL method get category with result: " + str(category.convert_to_dictionary()))
                return category

    def get_all_categories(self) -> List[Category]:
        logging.info("Beginning SAL method get all categories")
        categories = self.category_dao.get_all_categories()
        if len(categories) == 0:
            logging.warning("Error in SAL method get all categories, none found")
            raise CustomError("No categories found, please try again!")
        else:
            logging.info("Finishing SAL method get all categories with categories")
            return categories

    def update_category(self, category: Category) -> Category:
        logging.info("Beginning SAL method update category with data: " + str(category.convert_to_dictionary()))
        current_category_info = self.category_dao.get_category(category.category_id)
        if category.category_name == current_category_info.category_name:
            logging.warning("Error in SAL method update category, nothing changed")
            raise CustomError("Nothing changed, please try again!")
        elif category.category_name == '':
            logging.warning("Error in SAL method update category, category name empty")
            raise CustomError("The category name field cannot be left empty, please try again!")
        elif type(category.category_name) != str:
            logging.warning("Error in SAL method update category, category name not a string")
            raise CustomError("The category name field must be a string, please try again!")
        else:
            existing_categories = self.category_dao.get_all_categories()
            for existing_category in existing_categories:
                if category.category_name == existing_category.category_name:
                    logging.warning("Error in SAL method update category, category already exists")
                    raise CustomError("A category with this name already exists, please try again!")
            updated_category = self.category_dao.update_category(category)
            logging.info("Finishing SAL method update category with result: " +
                         str(updated_category.convert_to_dictionary()))
            return updated_category

    def delete_category(self, category_id: int) -> bool:
        logging.info("Beginning SAL method delete category with category ID: " + str(category_id))
        if type(category_id) != int:
            logging.warning("Error in SAL method delete category, category ID not an integer")
            raise CustomError("The category ID field must be an integer, please try again!")
        else:
            self.get_category(category_id)
            result = self.category_dao.delete_category(category_id)
            logging.info("Finishing SAL method delete category")
            return result
