from abc import ABC, abstractmethod
from typing import List

from Entities.Session import Session

class SessionSALInterface(ABC):

    @abstractmethod
    def create_session(self, session: Session) -> Session:
        pass

    @abstractmethod
    def get_session(self, session_id: str) -> Session:
        pass

    # @abstractmethod
    # def get_all_sessions(self, user_id: int) -> List[Session]:
    #     pass

    @abstractmethod
    def update_session(self, session: Session) -> bool:
        pass

    @abstractmethod
    def delete_session(self, session_id: str) -> bool:
        pass

    @abstractmethod
    def delete_all_sessions(self, user_id: int) -> bool:
        pass
