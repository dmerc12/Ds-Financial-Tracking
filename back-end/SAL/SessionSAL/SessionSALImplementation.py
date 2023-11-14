import logging

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from Entities.Session import Session
from SAL.SessionSAL.SessionSALInterface import SessionSALInterface
from SAL.UserSAL.UserSALImplementation import UserSALImplementation


class SessionSALImplementation(SessionSALInterface):
    user_dao = UserDALImplementation()
    user_sao = UserSALImplementation(user_dao)

    def __init__(self, session_dao: SessionDALImplementation):
        self.session_dao = session_dao

    def create_session(self, session: Session) -> Session:
        logging.info("Beginning SAL method create session with session: " + str(session.convert_to_dictionary()))
        pass

    def get_session(self, session_id: int) -> Session:
        logging.info("Beginning SAL method get session with session ID: " + str(session_id))
        pass

    def delete_session(self, session_id: int) -> bool:
        logging.info("Beginning SAL method update session with session ID: " + str(session_id))
        pass

    def delete_all_sessions(self, user_id: int) -> bool:
        logging.info("Beginning SAL method delete session with user ID: " + str(user_id))
        pass
