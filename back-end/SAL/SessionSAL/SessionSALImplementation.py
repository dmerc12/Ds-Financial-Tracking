import logging
from datetime import date, datetime

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from Entities.CustomError import CustomError
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
        if type(session.user_id) is not int:
            logging.warning("Error in SAL method create session, user ID not an integer")
            raise CustomError("The user ID field must be an integer, please try again!")
        elif type(session.expiration) is not date:
            logging.warning("Error in SAL method create session, expiration not a date")
            raise CustomError("The expiration field must be a date, please try again!")
        else:
            self.user_sao.get_user_by_id(session.user_id)
            new_session = self.session_dao.create_session(session)
            logging.info("Finishing SAL method create session with session: " +
                         str(new_session.convert_to_dictionary()))
            return new_session

    def get_session(self, session_id: int) -> Session:
        logging.info("Beginning SAL method get session with session ID: " + str(session_id))
        if type(session_id) is not int:
            logging.warning("Error in SAL method get session, session ID not an integer")
            raise CustomError("The session ID field must be an integer, please try again!")
        else:
            session = self.session_dao.get_session(session_id)
            if session.expiration == datetime(0000, 00, 00, 00, 00, 00, 00):
                logging.warning("Error in SAL method get session, no session found")
                raise CustomError("No session found, please try again!")
            elif session.expiration <= datetime.now():
                logging.warning("Error in SAL method get session, session expired")
                raise CustomError("Session has expired, please log in!")
            else:
                logging.info("Finishing SAL method get session with session: " + str(session.convert_to_dictionary()))
                return session

    def delete_session(self, session_id: int) -> bool:
        logging.info("Beginning SAL method update session with session ID: " + str(session_id))
        if type(session_id) is not int:
            logging.warning("Error in SAL method delete session, session ID not an integer")
            raise CustomError("The session ID field must be an integer, please try again!")
        else:
            self.get_session(session_id)
            result = self.session_dao.delete_session(session_id)
            logging.info("Finishing SAL method delete session with result: " + str(result))
            return result
