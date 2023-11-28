from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from Entities.Category import Category

category_dao = CategoryDALImplementation()
test_category = Category(0, -1, "d", "test")
current_category_id = 1
updated_category = Category(current_category_id, test_category.user_id, "e", "updated")

def test_create_category_success():
    result = category_dao.create_category(test_category)
    assert result.category_id != 0

def test_get_category_success():
    result = category_dao.get_category(current_category_id)
    assert result is not None

def test_get_all_categories_success():
    result = category_dao.get_all_categories(test_category.user_id)
    assert len(result) > 0

def test_get_categories_by_group_success():
    result = category_dao.get_categories_by_group(test_category.group)
    assert len(result) > 0

def test_update_category_success():
    result = category_dao.update_category(updated_category)
    assert result

def test_delete_category_success():
    result = category_dao.delete_category(current_category_id)
    assert result

def test_delete_all_categories_success():
    result = category_dao.delete_all_categories(-2)
    assert result
