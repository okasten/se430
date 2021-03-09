from .data import users


class User:
    counter = 0

    def __init__(self, name, email, password, is_admin):
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.id = User.counter
        User.counter += 1

    @classmethod
    def login(cls, email, password):
        pass

    def logout(self):
        pass

    def join_event(self, event_id):
        pass

    def create_event(self):
        pass

    def is_host(self, event_id):
        pass

    def get_all_hosted(self):
        pass

    def cancel_rsvp(self, event_id):
        pass

    @classmethod
    def get_user(cls, user_id):
        for user in users:
            if user['id'] == user_id:
                return user
        return None
