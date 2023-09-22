from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from Entities.Category import Category

category_dao = CategoryDALImplementation()
test_category = Category(0, "test")

def test_create_category_success():
    result = category_dao.create_category(test_category)
    assert result.category_id != test_category.category_id
