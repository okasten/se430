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

    def test_login(self):
        assert not User.login('abcd@gmail.com', 'password')

    def test_good_login(self):
        assert User.login('olivia@depaul.edu', 'password')

    def test_bad_password(self):
        assert not User.login('olivia@depaul.edu', '')

    def test_join_event(self):
        og_length = len(event_users)
        user = User('new user', 'new@gmail.com', 'password', False)
        user.join_event(0)

        assert event_users[-1]['event_id'] == 0
        assert event_users[-1]['user_id'] == user.id
        assert not event_users[-1]['is_host']
        assert len(event_users) == og_length + 1

    def test_create_event(self):
        user = User('new user', 'new@gmail.com', 'password', False)
        og_event_length = len(events)
        user.create_event(date.today(), 'New Event', 'Event C')

        assert len(events) == og_event_length + 1
        assert events[-1]['start_datetime'] == date.today()
        assert events[-1]['description'] == 'New Event'
        assert events[-1]['name'] == 'Event C'

        assert event_users[-1]['user_id'] == user.id
        assert event_users[-1]['event_id'] == events[-1]['id']
        assert event_users[-1]['is_host']

    def test_get_all_hosted_admin(self):
        user = User('new user', 'new@gmail.com', 'password', True)
        hosted = user.get_all_hosted()
        assert len(hosted) == len(events)

    def test_get_all_hosted_single(self):
        user = User('new user', 'new@gmail.com', 'password', False)
        user.create_event(date.today(), 'New Event', 'Event D')

        hosted = user.get_all_hosted()
        assert len(hosted) == 1

    def test_is_not_host(self):
        user = User('new user', 'new@gmail.com', 'password', False)
        e = Event(date(2021, 3, 10), 'desc', 'name')
        user.join_event(e.id)

        assert not user.is_host(e.id)

    def test_is_host_admin(self):
        user = User('new user', 'new@gmail.com', 'password', True)
        e = Event(date(2021, 3, 10), 'desc', 'name')
        assert user.is_host(e.id)

    def test_is_host(self):
        user = User('new user', 'new@gmail.com', 'password', False)
        user.create_event(date.today(), 'desc', 'name')

        assert user.is_host(events[-1]['id'])

    def test_cancel_rsvp(self):
        user = User('new user', 'new@gmail.com', 'password', False)
        e = Event(date(2021, 3, 10), 'desc', 'name')
        user.join_event(e.id)

        og_eu_len = len(event_users)

        user.cancel_rsvp(e.id)
        assert len(event_users) == og_eu_len - 1
        assert not EventUser.get_eu(e.id, user.id)


if __name__ == '__main__':
    unittest.main()
