from datetime import datetime, timedelta

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.CustomError import CustomError
from Entities.Session import Session
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
session_start = datetime.now()
session_expire = datetime.now() + timedelta(minutes=30)
successful_session = Session(0, -1, session_expire)
update_session = Session(-1, successful_session.user_id, datetime.now() + timedelta(minutes=3))

def test_create_session_customer_id_not_integer():
    try:
        test_session = Session(0, "-1", session_expire)
        session_sao.create_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "The user ID field must be an integer, please try again!"

def test_create_session_customer_not_found():
    try:
        test_session = Session(0, -50000000, session_expire)
        session_sao.create_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "This user cannot be found, please try again!"

def test_create_session_expire_date_time_not_date():
    try:
        test_session = Session(0, -1, session_expire)
        session_sao.create_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "The expiration field must be a date, please try again!"

def test_create_session_success():
    result = session_sao.create_session(successful_session)
    assert result.session_id != 0

def test_get_session_id_not_integer():
    try:
        session_sao.get_session("10")
        assert False
    except CustomError as error:
        assert str(error) == "The session ID field must be an integer, please try again!"

def test_get_session_not_found():
    try:
        session_sao.get_session(-500000000000)
        assert False
    except CustomError as error:
        assert str(error) == "No session found, please try again!"

def test_get_session_expired():
    try:
        result = session_sao.get_session(-2)
        print(result)
        assert False
    except CustomError as error:
        assert str(error) == "Session has expired, please log in!"

def test_get_session_success():
    result = session_sao.get_session(successful_session.session_id)
    assert result is not None

def test_get_session_with_updated_expiration_success():
    result = session_sao.get_session(-1)
    assert result.expiration != update_session.expiration and result.session_id == update_session.session_id

def test_delete_session_id_not_integer():
    try:
        session_sao.delete_session("1")
        assert False
    except CustomError as error:
        assert str(error) == "The session ID field must be an integer, please try again!"

def test_delete_session_not_found():
    try:
        session_sao.delete_session(-5000000000)
        assert False
    except CustomError as error:
        assert str(error) == "No session found, please try again!"

def test_delete_session_success():
    result = session_sao.delete_session(successful_session.session_id)
    assert result
