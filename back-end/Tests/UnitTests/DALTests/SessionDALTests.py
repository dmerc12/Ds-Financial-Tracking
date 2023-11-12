from datetime import datetime, timedelta

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.Session import Session

session_dao = SessionDALImplementation()
updated_expiration = datetime.now() + timedelta(0, 0, 0, 0, 30)
test_session = Session(0, -1, datetime.now())
update_session = Session(test_session.session_id, test_session.user_id, updated_expiration)

def test_create_session_success():
    result = session_dao.create_session(test_session)
    assert result.session_id != 0

def test_get_session_success():
    result = session_dao.get_session(test_session.session_id)
    assert result is not None

def test_update_session_success():
    result = session_dao.update_session(update_session)
    assert result.expiration != test_session.expiration

def test_delete_session_success():
    result = session_dao.delete_session(test_session.session_id)
    assert result
