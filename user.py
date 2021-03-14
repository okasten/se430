from datetime import datetime
from event import EventUser
from .data import users, event_users


def logout():
    exit()

class User:
    counter = 0

    def __init__(self, name, email, password, is_admin, events):
        self.events = events
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.id = User.counter
        User.counter += 1

    @classmethod
    def login(cls, email, password):
     for user in users:
     	if user.email == email:
     		if user.password == password:
                print("login successfully")
                return True:
            else:
                print("wrong password")
                return False
     print("enter correct email id")
     return False
     
    def join_event(self, events):
        if self.events.id == 0 or 1:
            events.join()

    def create_event(self, start_datetime=datetime, description=str, name=str):
        for e in self.events:
            if e['id'] == self.id:
                e['start_datetime'] = start_datetime
                e['description'] = description
                e['name'] = name
            return self.events.create(e)

    def get_all_hosted(self,events):
        for el in self.events:
            if el['is_host']:
                return event_users.get_event_users(el['event_users'])
            else:
                return False

    def is_host(self, event_id):
        event_user = EventUser.get_eu(self.id, event_id)
        if event_user['is_host']:
            for e in self.events:
                if e['id'] == self.id:
                    return e
        else:
            return False

    def cancel_rsvp(self):
        if self.id != 0 or 1:
             clear()

    @classmethod
    def get_user(cls, user_id):
        for user in users:
            if user['id'] == user_id:
                return user
        return None
