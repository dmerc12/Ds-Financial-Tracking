import unittest.mock as mock
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from Entities.Category import Category
from Entities.CustomError import CustomError

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)

successful_category = Category(0, 'another test category')
current_category_id = 1
updated_category = Category(current_category_id, 'updated category name')

def test_sal_create_category_name_empty():
    try:
        test_category = Category(0, '')
        category_sao.create_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "The category name field cannot be left empty, please try again!"

def test_sal_create_category_already_exists():
    try:
        test_category = Category(0, 'test category')
        category_sao.create_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "A category with this name already exists, please try again!"

def test_sal_create_category_name_not_string():
    try:
        test_category = Category(0, 0)
        category_sao.create_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "The category name field must be a string, please try again!"

def test_sal_create_category_success():
    result = category_sao.create_category(successful_category)
    assert result.category_id != 0

def test_sal_get_category_not_found():
    try:
        category_sao.get_category(-4787358034)
        assert False
    except CustomError as error:
        assert str(error) == "Category not found, please try again!"

def test_sal_get_category_id_not_integer():
    try:
        category_sao.get_category('')
        assert False
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_sal_get_category_success():
    result = category_sao.get_category(current_category_id)
    assert result is not None

def test_sal_get_all_categories_none_found():
    with mock.patch.object(category_sao.category_dao, 'get_all_categories', return_value=[]):
        try:
            category_sao.get_all_categories()
            assert False
        except CustomError as error:
            assert str(error) == "No categories found, please try again!"

def test_sal_get_all_categories_success():
    result = category_sao.get_all_categories()
    assert len(result) > 0

def test_sal_update_category_nothing_changed():
    try:
        changed_category = Category(current_category_id, successful_category.category_name)
        category_sao.update_category(changed_category)
        assert False
    except CustomError as error:
        assert str(error) == "Nothing changed, please try again!"

def test_sal_update_category_already_exists():
    try:
        changed_category = Category(current_category_id, 'test category')
        category_sao.update_category(changed_category)
        assert False
    except CustomError as error:
        assert str(error) == "A category with this name already exists, please try again!"

def test_sal_update_category_name_empty():
    try:
        changed_category = Category(current_category_id, '')
        category_sao.update_category(changed_category)
        assert False
    except CustomError as error:
        assert str(error) == "The category name field cannot be left empty, please try again!"

def test_sal_update_category_name_not_string():
    try:
        changed_category = Category(current_category_id, 0)
        category_sao.update_category(changed_category)
        assert False
    except CustomError as error:
        assert str(error) == "The category name field must be a string, please try again!"

def test_sal_update_category_success():
    result = category_sao.update_category(updated_category)
    assert result.category_name != successful_category.category_name

def test_sal_delete_category_not_found():
    try:
        category_sao.delete_category(-759757638469)
        assert False
    except CustomError as error:
        assert str(error) == "Category not found, please try again!"

def test_sal_delete_category_id_not_integer():
    try:
        category_sao.delete_category('')
        assert False
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_sal_delete_category_success():
    result = category_sao.delete_category(current_category_id)
    assert result
