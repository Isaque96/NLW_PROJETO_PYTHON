import pytest
from .events_link_repository import EventsLinkRepository

@pytest.mark.skip("Insert in DB")
def test_insert_eventos_link():
  event_id = 12
  subs_id = 18
  event_link_repo = EventsLinkRepository()

  event_link_repo.insert(event_id, subscriber_id=subs_id)