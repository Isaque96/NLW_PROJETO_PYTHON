import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
  subscriber_info = {
    "name": "meuNome",
    "email": "email@email.com",
    "evento_id": 2
  }
  subs_repo = SubscribersRepository()
  subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select_subscriber():
  email = "email@email.com"
  evento_id = 2

  subs_repo = SubscribersRepository()
  resp = subs_repo.select_subscriber(email, evento_id)
  print(resp.email)

@pytest.mark.skip("Ranking in DB")
def test_ranking():
  event_id = 3
  subs_repo = SubscribersRepository()
  resp = subs_repo.get_ranking(event_id)

  for element in resp:
    print(f"Link: {element.link}, total inscritos: {element.total}")