
from flask import Blueprint, render_template, request

from models.event import Event
from models.events_list import events

# create a new blueprint (a place to put routes)
events_blueprint = Blueprint("events", __name__)

# routes:
# INDEX, display all events
# GET /events
@events_blueprint.route('/events')
def index():
    # a tool to show some html with some data
    # html = "index.jinja" data = (title="Events Page" and events_list=events)
    return render_template("index.jinja", title="Events Page", event_list=events) 

# CREATE, create a new event
# POST /events
@events_blueprint.route('/events', methods=['POST'])
def create_event():
    # the fields from the form
    name = request.form["name"] # request = what the client sends 
    date = request.form["date"]
    location = request.form["location"]
    number_of_guests = request.form["num_of_guests"]
    description = request.form["description"]
    # create the new event using the fields
    new_event = Event(name, date, number_of_guests, location, description )
    # add the new event to the list of events
    events.append(new_event)
    # return render_template

    return render_template("index.jinja", title="Events Page", event_list=events)


    

