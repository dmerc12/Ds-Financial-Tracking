from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from Entities.Category import Category

category_dao = CategoryDALImplementation()
test_category = Category(0, "test")

def test_create_category_success():
    result = category_dao.create_category(test_category)
    assert result.category_id != 0

def test_get_all_categories_success():
    result = category_dao.get_all_categories()
    assert len(result) > 0

def test_update_category_success():
    pass

def test_delete_category_success():
    pass
