from DAL.SessionDAL.SessionDALInterface import SessionDALInterface
from Entities.Session import Session


class SessionDALImplementation(SessionDALInterface):

    def create_session(self, session: Session) -> Session:
        pass

    def get_session(self, session_id: int) -> Session:
        pass

    def update_session(self, session: Session) -> Session:
        pass

    def delete_session(self, session_id: int) -> bool:
        pass

    def delete_all_sessions(self, user_id: int) -> bool:
        pass
