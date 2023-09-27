import logging
from typing import List

from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from SAL.CategorySAL.CategorySALInterface import CategorySALInterface
from Entities.Category import Category

class CategorySALImplementation(CategorySALInterface):

    def __init__(self, category_dao: CategoryDALImplementation):
        self.category_dao = category_dao

    def create_category(self, category: Category) -> Category:
        pass

    def get_category(self, category_id: int) -> Category:
        pass

    def get_all_categories(self) -> List[Category]:
        pass

    def update_category(self, category: Category) -> Category:
        pass

    def delete_category(self, category_id: int) -> bool:
        pass
