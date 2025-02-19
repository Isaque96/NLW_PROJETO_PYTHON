from src.model.configs.connection import DbConnectionHandler
from src.model.entities.inscritos import Inscritos
from .interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscribersRepository(SubscribersRepositoryInterface):
  def insert(self, subscribers_info: dict) -> None:
    with DbConnectionHandler() as db:
      try:
        new_event = Inscritos(
          nome=subscribers_info.get("name"),
          email=subscribers_info.get("email"),
          link=subscribers_info.get("link"),
          evento_id=subscribers_info.get("evento_id"),
        )
        db.session.add(new_event)
        db.session.commit()
      except Exception as exception:
        db.session.rollback()
        raise exception

  def select_subscriber(self, email: str, event_id: int) -> Inscritos:
    with DbConnectionHandler() as db:
      data = (
        db.session
          .query(Inscritos)
          .filter(
            Inscritos.email == email,
            Inscritos.evento_id == event_id
          )
          .one_or_none()
      )

      return data