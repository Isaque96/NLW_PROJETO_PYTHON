from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.validators.subscribers_creator_validator import subscribers_crator_validator
from src.controllers.subscribers.subscribers_creator import SubscribersCreator
from src.controllers.subscribers.subscribers_manager import SubscriberManager
from src.model.repositories.subscribers_repository import SubscribersRepository

subs_route_bp = Blueprint("subscribers_route", __name__)

@subs_route_bp.route("/subscriber", methods=["POST"])
def create_new_subscriber():
  subscribers_crator_validator(request)
  http_request = HttpRequest(body=request.json)
  subs_repo = SubscribersRepository()
  subs_creator = SubscribersCreator(subs_repo)
  http_response = subs_creator.create(http_request)

  return jsonify(http_response.body), http_response.status_code

@subs_route_bp.route("/subscriber/link/<link>/event/<event_id>", methods=["GET"])
def subscribers_by_link(link, event_id):
  http_request = HttpRequest(params={"link": link, "event_id": event_id})
  subs_repo = SubscribersRepository()
  subs_manager = SubscriberManager(subs_repo)
  http_response = subs_manager.get_subscribers_by_link(http_request)

  return jsonify(http_response.body), http_response.status_code

@subs_route_bp.route("/subscriber/event/<event_id>", methods=["GET"])
def link_ranking(event_id):
  http_request = HttpRequest(params={"event_id": event_id})
  subs_repo = SubscribersRepository()
  subs_manager = SubscriberManager(subs_repo)
  http_response = subs_manager.get_events_ranking(http_request)

  return jsonify(http_response.body), http_response.status_code