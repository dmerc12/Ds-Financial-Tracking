from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from Entities.CustomError import CustomError
from Entities.User import User
from SAL.UserSAL.UserSALImplementation import UserSALImplementation

user_dao = UserDALImplementation()
user_sao = UserSALImplementation(user_dao)

successful_user = User(0, "first", "last", "new@email.com", "password")
successful_confirmation = "password"

def test_create_user_first_name_not_string():
    try:
        test_user = User(0, 0, "last", "test@email.com", "password")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The first name field must be a string, please try again!"

def test_create_user_first_name_too_long():
    try:
        test_user = User(0, "this has too many characters and so it should raise the desired exception", "last",
                         "test@email.com", "password")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The first name field cannot exceed 36 characters, please try again!"

def test_create_user_first_name_empty():
    try:
        test_user = User(0, "", "last", "test@email.com", "password")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The first name field cannot be left empty, please try again!"

def test_create_user_last_name_not_string():
    try:
        test_user = User(0, "first", 0, "test@email.com", "password")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The last name field must be a string, please try again!"

def test_create_user_last_name_too_long():
    try:
        test_user = User(0, "first", "this has too many characters and so it should raise the desired exception",
                         "test@email.com", "password")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The last name field cannot exceed 36 characters, please try again!"

def test_create_user_last_name_empty():
    try:
        test_user = User(0, "first", "", "test@email.com", "password")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The last name field cannot be left empty, please try again!"

def test_create_user_password_not_string():
    try:
        test_user = User(0, "first", "last", "test@email.com", 0)
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The password field must be a string, please try again!"

def test_create_user_password_empty():
    try:
        test_user = User(0, "first", "last", "test@email.com", "")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The password field cannot be left  empty, please try again!"

def test_create_user_password_too_long():
    try:
        test_user = User(0, "first", "last", "test@email.com", "this is much too long and so it should fail "
                                                               "and get the desired error message")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The password field cannot exceed 60 characters, please try again!"

def test_create_user_confirmation_password_empty():
    try:
        test_user = User(0, "first", "last", "test@email.com", "password")
        user_sao.create_user(test_user, "")
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field cannot be left empty, please try again!"

def test_create_user_confirmation_password_too_long():
    try:
        test_user = User(0, "first", "last", "test@email.com", "pass")
        user_sao.create_user(test_user, "this is much too long and should raise the desired error")
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field cannot exceed 60 characters, please try again!"

def test_create_user_confirmation_password_not_string():
    try:
        test_user = User(0, "first", "last", "test@email.com", "test")
        user_sao.create_user(test_user, 6)
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field must be a string, please try again!"

def test_create_user_email_not_string():
    try:
        test_user = User(0, "first", "last", 0, "password")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_create_user_email_too_long():
    try:
        test_user = User(0, "first", "last", "this has too many characters and so it should raise the "
                                             "desired exception", "password")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot exceed 60 characters, please try again!"

def test_create_user_email_empty():
    try:
        test_user = User(0, "first", "last", "", "password")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot be left empty, please try again!"

def test_create_user_confirmation_password_not_matching_password():
    try:
        failed_confirmation = "not going to work"
        user_sao.create_user(successful_user, failed_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The passwords do not match, please try again!"

def test_create_user_already_exists():
    try:
        test_user = User(0, "first", "last", "password", "test@email.com")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "A user already exists with this email, please log in!"

def test_create_user_success():
    result = user_sao.create_user(successful_user, successful_confirmation)
    assert result.user_id != 0

def test_get_user_by_id_not_integer():
    try:
        user_sao.get_user_by_id("this won't work")
        assert False
    except CustomError as error:
        assert str(error) == "User ID field must be an integer, please try again!"

def test_get_user_by_id_not_found():
    try:
        user_sao.get_user_by_id(-500000)
        assert False
    except CustomError as error:
        assert str(error) == "This user cannot be found, please try again!"

def test_get_user_by_id_success():
    result = user_sao.get_user_by_id(successful_user.user_id)
    assert result is not None

def test_get_user_by_email_not_a_string():
    try:
        user_sao.get_user_by_email(50)
        assert False
    except CustomError as error:
        assert str(error) == "Email field must be a string, please try again!"

def test_get_user_by_email_success():
    result = user_sao.get_user_by_email(successful_user.email)
    assert result is not None

def test_login_email_not_string():
    try:
        user_sao.login(0, successful_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_login_email_empty():
    try:
        user_sao.login("", successful_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot be left empty, please try again!"

def test_login_password_not_string():
    try:
        user_sao.login(successful_user.email, 0)
        assert False
    except CustomError as error:
        assert str(error) == "The password field must be a string, please try again!"

def test_login_password_empty():
    try:
        user_sao.login(successful_user.email, "")
        assert False
    except CustomError as error:
        assert str(error) == "The password field cannot be left empty, please try again!"

def test_login_email_or_password_incorrect():
    try:
        user_sao.login("incorrect", "credentials")
        assert False
    except CustomError as error:
        assert str(error) == "Either the email or password are incorrect, please try again!"

def test_login_success():
    result = user_sao.login("test@email.com", "test")
    assert result is not None

def test_update_user_first_name_not_string():
    try:
        test_user = User(successful_user.user_id, 0, "last", "test@email.com", "password")
        user_sao.update_user(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The first name field must be a string, please try again!"

def test_update_user_first_name_empty():
    try:
        test_user = User(successful_user.user_id, "", "last", "test@email.com", "password")
        user_sao.update_user(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The first name field cannot be empty, please try again!"

def test_update_user_first_name_too_long():
    try:
        test_user = User(successful_user.user_id, "this has too many characters and so it should raise the "
                                                  "desired exception", "last", "test@email.com", "password")
        user_sao.update_user(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The first name field cannot exceed 36 characters, please try again!"

def test_update_user_last_name_not_string():
    try:
        test_user = User(successful_user.user_id, "first", 0, "test@email.com", "password")
        user_sao.update_user(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The last name field must be a string, please try again!"

def test_update_user_last_name_too_long():
    try:
        test_user = User(successful_user.user_id, "first", "this has too many characters and so it should raise "
                                                           "the desired exception", "test@email.com", "password")
        user_sao.update_user(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The last name field cannot exceed 36 characters, please try again!"

def test_update_user_last_name_empty():
    try:
        test_user = User(successful_user.user_id, "first", "", "test@email.com", "password")
        user_sao.update_user(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The last name field cannot be empty, please try again!"


def test_update_user_email_not_string():
    try:
        test_user = User(successful_user.user_id, "first", "last", 0, "password")
        user_sao.update_user(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_update_customer_email_empty():
    try:
        test_user = User(successful_user.user_id, "first", "last", "", "password")
        user_sao.update_user(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot be empty, please try again!"

def test_update_customer_email_too_long():
    try:
        test_user = User(successful_user.user_id, "first", "last", "this has too many characters so it should "
                                                                   "raise the desired exception", "password")
        user_sao.update_user(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot exceed 60 characters, please try again!"

def test_update_customer_no_info_changed():
    try:
        user_sao.update_user(successful_user)
        assert False
    except CustomError as error:
        assert str(error) == "No information has changed!"

def test_update_user_success():
    updated_user = User(successful_user.user_id, "new", "names", "new@email.com", "new")
    result = user_sao.update_user(updated_user)
    assert result.first_name == updated_user.first_name and result.last_name == updated_user.last_name \
           and result.email == updated_user.email

def test_change_password_user_not_found():
    try:
        user_sao.change_password(-5000000000, "new", "new")
        assert False
    except CustomError as error:
        assert str(error) == "This user cannot be found, please try again!"

def test_change_password_password_new_password_not_string():
    try:
        user_sao.change_password(successful_user.user_id, -500000, "new")
        assert False
    except CustomError as error:
        assert str(error) == "The new password field must be a string, please try again!"

def test_change_password_password_new_password_empty():
    try:
        user_sao.change_password(successful_user.user_id, "", "new")
        assert False
    except CustomError as error:
        assert str(error) == "The password field cannot be left empty, please try again!"

def test_change_password_password_new_password_too_long():
    try:
        user_sao.change_password(successful_user.user_id, "this is too long and so it should raise the desired "
                                                          "error message", "new")
        assert False
    except CustomError as error:
        assert str(error) == "The password field cannot exceed 60 characters, please try again!"

def test_change_password_confirmation_password_not_string():
    try:
        user_sao.change_password(successful_user.user_id, "new", -5000000)
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field must be a string, please try again!"

def test_change_password_password_confirmation_password_empty():
    try:
        user_sao.change_password(successful_user.user_id, "new", "")
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password cannot be left empty, please try again!"

def test_change_password_password_confirmation_password_too_long():
    try:
        user_sao.change_password(successful_user.user_id, "new", "this is too long and so it should raise the "
                                                                 "desired error message")
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field cannot exceed 36 characters, please try again!"

def test_change_password_user_id_not_integer():
    try:
        user_sao.change_password("this won't work", "new", "new")
        assert False
    except CustomError as error:
        assert str(error) == "The user ID field must be an integer, please try again!"

def test_change_password_new_password_does_not_match_confirmation_password():
    try:
        user_sao.change_password(successful_user.user_id, "new", "old")
        assert False
    except CustomError as error:
        assert str(error) == "The passwords don't match, please try again!"

def test_change_password_nothing_changed():
    try:
        user_sao.change_password(successful_user.user_id, "password", "password")
        assert False
    except CustomError as error:
        assert str(error) == "Nothing has changed, please try again!"

def test_change_password_success():
    result = user_sao.change_password(successful_user.user_id, "new", "new")
    assert result

def test_delete_user_not_found():
    try:
        user_sao.delete_user(-500000)
        assert False
    except CustomError as error:
        assert str(error) == "This user cannot be found, please try again!"

def test_delete_user_success():
    result = user_sao.delete_user(successful_user.user_id)
    assert result
