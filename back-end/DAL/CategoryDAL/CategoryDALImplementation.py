from typing import List

from DAL.CategoryDAL.CategoryDALInterface import CategoryDALInterface
from Entities.Category import Category


class CategoryDALImplementation(CategoryDALInterface):

    def create_category(self, category: Category) -> Category:
        pass

    def get_all_categories(self) -> List[Category]:
        pass

    def update_category(self, category: Category) -> Category:
        pass

    def delete_category(self, category_id: int) -> bool:
        pass
    