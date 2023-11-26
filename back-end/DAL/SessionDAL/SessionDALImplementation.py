import logging
from datetime import datetime

from DAL.SessionDAL.SessionDALInterface import SessionDALInterface
from Database.config import Connection
from Entities.Session import Session


class SessionDALImplementation(SessionDALInterface):

    def create_session(self, session: Session) -> bool:
        logging.info("Beginning DAL method create session with session: " + session.convert_to_dictionary())
        sql = "INSERT INTO financial_tracker.Session (session_id, user_id, expiration) VALUES (%s, %s, %s) " \
              "RETURNING session_id;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (session.session_id, session.user_id, session.expiration))
        connection.commit()
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method create session")
        return True

    def get_session(self, session_id: str) -> Session:
        logging.info("Beginning DAL method get session with session ID: " + str(session_id))
        sql = "SELECT * FROM financial_tracker.Session WHERE session_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (session_id,))
        session_info = cursor.fetchone()
        cursor.close()
        connection.close()
        if session_info is None:
            session = Session("0", 0, datetime(0000, 00, 00))
            logging.info("Finishing DAL method get session, not found")
            return session
        else:
            session = Session(*session_info)
            logging.info("Finishing DAL method get session with session: " + str(session.convert_to_dictionary()))
            return session

    def update_session(self, session: Session) -> bool:
        logging.info("Beginning DAL method update session with session: " + str(session.convert_to_dictionary()))
        sql = "UPDATE financial_tracker.Session SET expiration=%s WHERE session_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (session.expiration, session.session_id))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method update_session")
        return True

    def delete_session(self, session_id: str) -> bool:
        logging.info("Beginning DAL method delete session with session ID: " + str(session_id))
        sql = "DELETE FROM financial_tracker.Session WHERE session_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (session_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete session")
        return True

    def delete_all_sessions(self, user_id: int) -> bool:
        logging.info("Beginning DAL method delete all sessions with user ID: " + str(user_id))
        sql = "DELETE FROM financial_tracker.Session WHERE user_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete all sessions")
        return True
