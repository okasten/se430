from .data import users, event_users, events


class User:
    counter = 2

    def __init__(self, name, email, password, is_admin):
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.id = User.counter
        User.counter += 1

    @classmethod
    def login(cls, email, password):
        for user in users:
            if user['email'] == email:
                if user['password'] == password:
                    print("login successfully")
                    return True
                else:
                    print("wrong password")
                    return False
        print("enter correct email id")
        return False

    def join_event(self, event_id):
        from .event import EventUser
        EventUser(event_id, self.id, False)

    def create_event(self, start_datetime, description, name):
        from .event import EventUser, Event
        e = Event(start_datetime, description, name)
        EventUser(e.id, self.id, True)

    def get_all_hosted(self):
        from .event import Event
        hosted_events = []
        if self.is_admin:
            return events
        for eu in event_users:
            if eu['user_id'] == self.id and eu['is_host']:
                hosted_events.append(Event.get_event(eu['event_id']))
        return hosted_events

    def is_host(self, event_id):
        from .event import EventUser
        if self.is_admin:
            return True
        event_user = EventUser.get_eu(event_id, self.id)
        if event_user:
            return event_user['is_host']
        return False

    def cancel_rsvp(self, event_id):
        for eu in event_users:
            if eu['user_id'] == self.id and eu['event_id'] == event_id:
                event_users.remove(eu)

    @classmethod
    def get_user(cls, user_id):
        for user in users:
            if user['id'] == user_id:
                return user
        return None
