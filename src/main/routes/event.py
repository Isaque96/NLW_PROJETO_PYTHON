from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.validators.events_creator_validator import event_creator_validator
from src.controllers.events.events_creator import EventsCreator
from src.model.repositories.events_repository import EventsRepository

event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
  event_creator_validator(request)
  http_request = HttpRequest(body=request.json)
  events_repo = EventsRepository()
  events_creator = EventsCreator(events_repo)
  http_response = events_creator.create(http_request)

  return jsonify(http_response.body), http_response.status_code