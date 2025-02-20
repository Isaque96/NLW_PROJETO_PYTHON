import random
from src.model.configs.connection import DbConnectionHandler
from src.model.entities.eventos_link import EventosLink
from .interfaces.events_link_repository import EventsLinkRepositoryInterface

class EventsLinkRepository(EventsLinkRepositoryInterface):
  def insert(self, event_id: int, subscriber_id: int) -> str:
    with DbConnectionHandler() as db:
      try:
        link_final = ''.join(random.choices('0123456789', k=7))
        foramted_link = f"evento-{event_id}-{subscriber_id}-{link_final}"

        new_events_link = EventosLink(
          evento_id=event_id,
          inscrito_id=subscriber_id,
          link=foramted_link
        )
        db.session.add(new_events_link)
        db.session.commit()

        return foramted_link
      except Exception as exception:
        db.session.rollback()
        raise exception
  
  def select_events_link(self, event_id: int, subscriber_id: int) -> EventosLink:
    with DbConnectionHandler() as db:
      data = (
        db.session
          .query(EventosLink)
          .filter(
            EventosLink.evento_id == event_id,
            EventosLink.inscrito_id == subscriber_id
          )
          .one_or_none()
      )
    return data
      