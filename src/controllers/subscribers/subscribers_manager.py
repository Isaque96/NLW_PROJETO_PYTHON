from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscriberManager():
  def __init__(self, subscriber_repo: SubscribersRepositoryInterface):
    self.__subscriber_repo = subscriber_repo
  
  def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpResponse:
    link = http_request.params["link"]
    event_id = http_request.params["event_id"]

    subs = self.__subscriber_repo.select_subscribers_by_link(link, event_id)
    return self.__format_subs_by_link(subs)

  def get_events_ranking(self, http_request: HttpRequest) -> HttpResponse:
    event_id = http_request.params["event_id"]
    event_ranking = self.__subscriber_repo.get_ranking(event_id)

    return self.__format_event_ranking(event_ranking)

  def __format_event_ranking(self, event_ranking: list) -> HttpResponse:
    formatted_event_ranking = []
    for position in event_ranking:
      formatted_event_ranking.append(
        {
          "link": position.link,
          "total": position.total
        }
      )
    
    return HttpResponse(
      body={
        "data": {
          "type": "Ranking",
          "count": len(formatted_event_ranking),
          "subscribers": formatted_event_ranking
        }
      },
      status_code=200
    )
  
  def __format_subs_by_link(self, subs: list) -> HttpResponse:
    formatted_subscriber = []
    for sub in subs:
      formatted_subscriber.append(
        {
          "nome": sub.nome,
          "email": sub.email
        }
      )
    
    return HttpResponse(
      body={
        "data": {
          "type": "Inscritos",
          "count": len(formatted_subscriber),
          "subscribers": formatted_subscriber
        }
      },
      status_code=200
    )