class Event:
    counter = 0

    def __init__(self, start_datetime, description, name):
        self.start_datetime = start_datetime
        self.description = description
        self.name = name
        self.id = Event.counter
        Event.counter += 1

    def get_attendees(self):
        pass

    @classmethod
    def get_event(cls, id):
        pass

    def update_event(self, start_datetime, description, name):
        pass

    def delete_event(self, user_id):
        pass

    def send_event_details(self, users):
        pass

    def add_location(self):
        pass

    @classmethod
    def get_events(cls, date=None):
        pass


class EventLocation:
    def __init__(self, event_id, location_id):
        self.event_id = event_id
        self.location_id = location_id


class EventUser:
    def __init__(self, event_id, user_id):
        self.event_id = event_id
        self.user_id = user_id


