from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscribersCreator:
  def __init__(self, subs_repo: SubscribersRepositoryInterface):
    self.__subs_repo = subs_repo
    
  def create(self, http_request: HttpRequest) -> HttpResponse:
    subs_info = http_request.body["data"]
    subs_email = subs_info["email"]
    evento_id = subs_info["evento_id"]

    self.__check_subscriber(subs_email, evento_id)
    self.__insert_subscriber(subscribers_info=subs_info)
    return self.__format_response(subscribers_info=subs_info)

  def __check_subscriber(self, subs_email: str, evento_id: int) -> None:
    response = self.__subs_repo.select_subscriber(email=subs_email, event_id=evento_id)

    if response: raise Exception("Subscriber already exists!")

  def __insert_subscriber(self, subscribers_info: dict) -> None:
    self.__subs_repo.insert(subscribers_info)

  def __format_response(self, subscribers_info: dict) -> HttpResponse:
    return HttpResponse(
      body={
        "data": {
          "type": "Inscrito",
          "count": 1,
          "attributes": subscribers_info
        }        
      },
      status_code=201
    )