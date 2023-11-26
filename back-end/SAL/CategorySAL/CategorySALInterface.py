from abc import ABC, abstractmethod
from typing import List

from Entities.Category import Category


class CategorySALInterface(ABC):

    @abstractmethod
    def create_category(self, category: Category) -> Category:
        pass

    @abstractmethod
    def get_category(self, category_id: int) -> Category:
        pass

    @abstractmethod
    def get_all_categories(self, user_id: int) -> List[Category]:
        pass

    @abstractmethod
    def get_categories_by_group(self, group: str) -> List[Category]:
        pass

    @abstractmethod
    def update_category(self, category: Category) -> Category:
        pass

    @abstractmethod
    def delete_category(self, category_id: int) -> bool:
        pass

    @abstractmethod
    def delete_all_categories(self, user_id: int) -> bool:
        pass
