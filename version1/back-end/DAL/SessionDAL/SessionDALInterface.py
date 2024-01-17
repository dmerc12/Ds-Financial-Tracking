from abc import ABC, abstractmethod

from Entities.Session import Session

class SessionDALInterface(ABC):

    @abstractmethod
    def create_session(self, session: Session) -> bool:
        pass

    @abstractmethod
    def get_session(self, session_id: str) -> Session:
        pass

    @abstractmethod
    def get_all_sessions(self):
        pass

    @abstractmethod
    def update_session(self, session: Session) -> bool:
        pass

    @abstractmethod
    def delete_session(self, session_id: str) -> bool:
        pass

    @abstractmethod
    def delete_all_sessions(self, user_id: int) -> bool:
        pass
