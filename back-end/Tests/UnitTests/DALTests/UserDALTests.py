import bcrypt

from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from Entities.User import User

user_dao = UserDALImplementation()

test_password = str(bcrypt.hashpw("test".encode("utf-8"), bcrypt.gensalt()))
update_password = str(bcrypt.hashpw("updated".encode("utf-8"), bcrypt.gensalt()))

test_user = User(0, 'test@email.com', test_password)
updated_user = User(test_user.user_id, 'updated@email.com', update_password)

def test_create_user_success():
    result = user_dao.create_user(test_user)
    assert result.user_id != 0

def test_get_user_by_id_success():
    result = user_dao.get_user_by_id(test_user.user_id)
    assert result is not None

def test_get_user_by_email_success():
    result = user_dao.get_user_by_email(test_user.email)
    assert result is not None

def test_login_success():
    result = user_dao.login(test_user.email, test_user.password)
    assert result is not None

def test_change_email_success():
    result = user_dao.change_email(updated_user)
    assert result

def test_change_password_success():
    result = user_dao.change_password(updated_user)
    assert result

def test_delete_user_success():
    result = user_dao.delete_user(test_user.user_id)
    assert result
