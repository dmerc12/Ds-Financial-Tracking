import unittest.mock as mock

from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from Entities.CustomError import CustomError
from Entities.Category import Category

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)

successful_category = Category(0, -1, "d", 'another test category')
current_category_id = 1
updated_category = Category(current_category_id, successful_category.user_id, "e", 'updated category name')

def test_create_category_name_empty():
    try:
        test_category = Category(0, -1, "b", '')
        category_sao.create_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "The category name field cannot be left empty, please try again!"

def test_create_category_already_exists():
    try:
        test_category = Category(0, -1, "b", 'test category')
        category_sao.create_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "A category with this name already exists, please try again!"

def test_create_category_name_not_string():
    try:
        test_category = Category(0, -1, "b", 0)
        category_sao.create_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "The category name field must be a string, please try again!"

def test_create_category_group_not_string():
    try:
        test_category = Category(0, -1, 0, "test")
        category_sao.create_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "The group field must be a string, please try again!"

def test_create_category_group_too_long():
    try:
        test_category = Category(0, -1, "bb", "test")
        category_sao.create_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "The group field cannot be longer than a single character, please try again!"

def test_create_category_group_empty():
    try:
        test_category = Category(0, -1, "", "test")
        category_sao.create_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "The group field cannot be left empty, please try again!"

def test_create_category_group_not_allowable():
    try:
        test_category = Category(0, -1, "a", "test")
        category_sao.create_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "The group field can only be expense (e), deposit (d), or both (b); please try again!"

def test_create_category_success():
    result = category_sao.create_category(successful_category)
    assert result.category_id != 0

def test_get_category_not_found():
    try:
        category_sao.get_category(-4787358034)
        assert False
    except CustomError as error:
        assert str(error) == "Category not found, please try again!"

def test_get_category_id_not_integer():
    try:
        category_sao.get_category('')
        assert False
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_get_category_success():
    result = category_sao.get_category(current_category_id)
    assert result is not None

def test_get_all_categories_none_found():
    with mock.patch.object(category_sao.category_dao, 'get_all_categories', return_value=[]):
        try:
            category_sao.get_all_categories(successful_category.user_id)
            assert False
        except CustomError as error:
            assert str(error) == "No categories found, please try again!"

def testl_get_all_categories_success():
    result = category_sao.get_all_categories(successful_category.user_id)
    assert len(result) > 0

def test_get_categories_by_group_not_string():
    pass

def test_get_categories_by_group_too_long():
    pass

def test_get_categories_by_group_empty():
    pass

def test_get_categories_by_group_not_allowable():
    pass

def test_get_categories_by_group_none_found():
    pass

def test_get_categories_by_group_success():
    pass

def test_update_category_already_exists():
    try:
        changed_category = Category(current_category_id, successful_category.user_id, "d", 'test category')
        category_sao.update_category(changed_category)
        assert False
    except CustomError as error:
        assert str(error) == "A category with this name already exists, please try again!"

def test_update_category_name_empty():
    try:
        changed_category = Category(current_category_id, -1, "b", '')
        category_sao.update_category(changed_category)
        assert False
    except CustomError as error:
        assert str(error) == "The category name field cannot be left empty, please try again!"

def test_update_category_name_not_string():
    try:
        changed_category = Category(current_category_id, -1, "b", 0)
        category_sao.update_category(changed_category)
        assert False
    except CustomError as error:
        assert str(error) == "The category name field must be a string, please try again!"

def test_update_category_group_not_string():
    try:
        test_category = Category(0, -1, 1, "test")
        category_sao.update_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "The group field must be a string, please try again!"

def test_update_category_group_too_long():
    try:
        test_category = Category(0, -1, "bb", "test")
        category_sao.update_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "The group field cannot be longer than a single character, please try again!"

def test_update_category_group_empty():
    try:
        test_category = Category(0, -1, "", "test")
        category_sao.update_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "The group field cannot be left empty, please try again!"

def test_update_category_group_not_allowable():
    try:
        test_category = Category(0, -1, "a", "test")
        category_sao.update_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "The group field can only be expense (e), deposit (d), or both (b); please try again!"

def test_update_category_success():
    result = category_sao.update_category(updated_category)
    assert result.category_name != successful_category.category_name

def test_delete_category_not_found():
    try:
        category_sao.delete_category(-759757638469)
        assert False
    except CustomError as error:
        assert str(error) == "Category not found, please try again!"

def test_delete_category_id_not_integer():
    try:
        category_sao.delete_category('')
        assert False
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_delete_category_success():
    result = category_sao.delete_category(current_category_id)
    assert result

def test_delete_all_categories_user_id_not_integer():
    pass

def test_delete_all_categories_user_not_found():
    pass

def test_delete_all_categories_success():
    pass
