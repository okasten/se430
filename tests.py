import unittest
from .event import *
from .data import *


class MyTestCase(unittest.TestCase):
    def test_get_event(self):
        assert Event.get_event(0) == events[0]

    def test_get_attendees(self):
        e = Event(date(2021, 3, 19), 'Career Fair', 'Career Fair')
        EventUser(e.id, 2, True)
        EventUser(e.id, 1, True)
        assert e.get_attendees() == [
            {
                'id': 2,
                'name': 'Olivia Kasten',
                'email': 'olivia@depaul.edu',
                'password': 'password',
                'is_admin': False,
            },
            {
                'id': 1,
                'name': 'Jaimi Patel',
                'email': 'jaimi@depaul.edu',
                'password': 'password',
                'is_admin': True,
            },
        ]

    def test_update_event(self):
        e = Event(date(2021, 3, 10), 'desc', 'name')
        e.update_event(date(2021, 4, 1), 'desc1', 'name1')

        updated = Event.get_event(e.id)
        assert updated['start_datetime'] == date(2021, 4, 1)
        assert updated['description'] == 'desc1'
        assert updated['name'] == 'name1'

    def test_delete_event(self):
        e = Event(date(2021, 3, 10), 'desc', 'name')
        eu = EventUser(e.id, 2, True)
        e.delete_event(2)

        event_ids = {e['id'] for e in events}
        assert e.id not in event_ids

    def test_add_location(self):
        e = Event(date(2021, 3, 10), 'desc', 'name')
        e.add_location(1)

        assert e.get_event_location() == Location.get_location(1)

    def test_get_available_locations(self):
        assert Location.get_available_locations(date(2021, 3, 18)) == [
            {
                'id': 1,
                'address': '614 Main St',
                'name': 'Room A - Chrysler Building'
            },
        ]


if __name__ == '__main__':
    unittest.main()
