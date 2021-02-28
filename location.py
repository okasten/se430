class Location:
    counter = 0

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.id = Location.counter
        Location.counter += 1

    @classmethod
    def get_location(cls, id):
        pass

    @classmethod
    def get_available_locations(cls, date):
        pass
