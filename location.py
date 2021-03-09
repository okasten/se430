from .data import locations, events, event_locations
from datetime import datetime


class Location:
    counter = 0

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.id = Location.counter
        Location.counter += 1

    @classmethod
    def get_location(cls, location_id: int):
        for loc in locations:
            if loc['id'] == location_id:
                return loc
        return None

    @classmethod
    def get_available_locations(cls, date: datetime):
        event_ids_on_date = []
        for e in events:
            if e['start_datetime'] == date:
                event_ids_on_date.append(e['id'])

        taken_locations = []
        for eloc in event_locations:
            if eloc['event_id'] in event_ids_on_date:
                taken_locations.append(Location.get_location(eloc['location_id']))

        available_locations = locations.copy()
        for loc in taken_locations:
            available_locations.remove(loc)

        return available_locations
