from abc import ABC, abstractmethod
from src.model.entities.eventos import Eventos

class EventsRepositoryInterface(ABC):
  @abstractmethod
  def insert(self, event_name: str) -> None: pass
  
  @abstractmethod
  def select_event(self, event_name: str) -> Eventos: pass