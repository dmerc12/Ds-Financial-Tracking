from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from Entities.Category import Category
from Entities.CustomError import CustomError

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)

successful_category = Category(0, 'test')

def test_sal_create_category_name_empty():
    pass

def test_sal_create_category_already_exists():
    pass

def test_sal_create_category_name_not_string():
    pass

def test_sal_create_category_success():
    pass

def test_sal_get_category_not_found():
    pass

def test_sal_get_category_id_not_integer():
    pass

def test_sal_get_category_success():
    pass

def test_sal_get_all_categories_none_found():
    pass

def test_sal_get_all_categories_success():
    pass

def test_sal_update_category_nothing_changed():
    pass

def test_sal_update_category_already_exists():
    pass

def test_sal_update_category_name_empty():
    pass

def test_sal_update_category_name_not_string():
    pass

def test_sal_update_category_success():
    pass

def test_sal_delete_category_not_found():
    pass

def test_sal_delete_category_id_not_integer():
    pass

def test_sal_delete_category_success():
    pass
