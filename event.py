from datetime import datetime, date
from .user import User
from .data import *
from .location import Location


class Event:
    counter = 2  # TODO pick a number based on basic data

    def __init__(self, start_datetime, description, name, skip_append=False):
        self.start_datetime = start_datetime
        self.description = description
        self.name = name
        self.id = Event.counter

        if not skip_append:
            events.append(self.__dict__)
        Event.counter += 1

    def get_attendees(self):
        attendees = []
        for eu in event_users:
            if eu['event_id'] == self.id:
                user = User.get_user(eu['user_id'])
                attendees.append(user)
        return attendees

    @classmethod
    def get_event(cls, event_id: int):
        for e in events:
            if e['id'] == event_id:
                return e
        return None

    def update_event(self, start_datetime: datetime, description: str, name: str):
        self.start_datetime = start_datetime
        self.description = description
        self.name = name

        for e in events:
            if e['id'] == self.id:
                e['start_datetime'] = start_datetime
                e['description'] = description
                e['name'] = name

    def delete_event(self, user_id: int):
        event_user = EventUser.get_eu(self.id, user_id)
        if event_user['is_host']:
            for e in events:
                if e['id'] == self.id:
                    events.remove(e)
        else:
            return False  # user doesn't have access to do this

    def send_event_details(self, users):
        pass

    def add_location(self, location_id):
        el = EventLocation(self.id, location_id)
        event_locations.append(el.__dict__)
        return True

    def get_event_location(self):
        for el in event_locations:
            if el['event_id'] == self.id:
                return Location.get_location(el['location_id'])

    @classmethod
    def get_events(cls, selected_date=None):
        if not selected_date:
            selected_date = datetime.today()

        all_events = []
        for e in events:
            if e['start_datetime'] >= selected_date:
                all_events.append(e)


class EventLocation:
    def __init__(self, event_id, location_id):
        self.event_id = event_id
        self.location_id = location_id
        event_locations.append(self.__dict__)


class EventUser:
    def __init__(self, event_id, user_id, is_host):
        self.event_id = event_id
        self.user_id = user_id
        self.is_host = is_host
        event_users.append(self.__dict__)

    @classmethod
    def get_eu(cls, event_id, user_id):
        for eu in event_users:
            if eu['event_id'] == event_id and eu['user_id'] == user_id:
                return eu
        return None
