from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from Entities.Category import Category
from Entities.CustomError import CustomError

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)

successful_category = Category(0, 'test')

def test_sal_create_category_name_empty():
    try:
        test_category = Category(0, '')
        category_sao.create_category(test_category)
        assert False
    except CustomError as error:
        assert str(error) == "The category name field cannot be left empty, please try again!"

def test_sal_create_category_already_exists():
    try:
        pass
    except CustomError as error:
        assert str(error) == ""

def test_sal_create_category_name_not_string():
    try:
        pass
    except CustomError as error:
        assert str(error) == ""

def test_sal_create_category_success():
    pass

def test_sal_get_category_not_found():
    try:
        pass
    except CustomError as error:
        assert str(error) == ""

def test_sal_get_category_id_not_integer():
    try:
        pass
    except CustomError as error:
        assert str(error) == ""

def test_sal_get_category_success():
    pass

def test_sal_get_all_categories_none_found():
    try:
        pass
    except CustomError as error:
        assert str(error) == ""

def test_sal_get_all_categories_success():
    pass

def test_sal_update_category_nothing_changed():
    try:
        pass
    except CustomError as error:
        assert str(error) == ""

def test_sal_update_category_already_exists():
    try:
        pass
    except CustomError as error:
        assert str(error) == ""

def test_sal_update_category_name_empty():
    try:
        pass
    except CustomError as error:
        assert str(error) == ""

def test_sal_update_category_name_not_string():
    try:
        pass
    except CustomError as error:
        assert str(error) == ""

def test_sal_update_category_success():
    pass

def test_sal_delete_category_not_found():
    try:
        pass
    except CustomError as error:
        assert str(error) == ""

def test_sal_delete_category_id_not_integer():
    try:
        pass
    except CustomError as error:
        assert str(error) == ""

def test_sal_delete_category_success():
    pass
