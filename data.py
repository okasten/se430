from datetime import date

events = [
    {
        'id': 0,
        'start_datetime': date(2021, 3, 18),
        'description': "Women's basketball game vs. Duke",
        'name': 'Basketball Game'
    },
    {
        'id': 1,
        'start_datetime': date(2021, 3, 19),
        'description': "Career Fair",
        'name': "Career Fair"
    },
]

users = [
    {
        'id': 0,
        'name': 'Mustafa Apaydin',
        'email': 'mustafa@depaul.edu',
        'password': 'password',
        'is_admin': True,
    },
    {
        'id': 1,
        'name': 'Jaimi Patel',
        'email': 'jaimi@depaul.edu',
        'password': 'password',
        'is_admin': True,
    },
    {
        'id': 2,
        'name': 'Olivia Kasten',
        'email': 'olivia@depaul.edu',
        'password': 'password',
        'is_admin': False,
    },
]

event_users = [
    {  # bball game, Olivia, not host
        'event_id': 0,
        'user_id': 2,
        'is_host': False,
    },
    {  # career fair, Olivia, is host
        'event_id': 1,
        'user_id': 2,
        'is_host': False,
    },
    {  # bball game, Mustafa, host
        'event_id': 0,
        'user_id': 1,
        'is_host': True,
    },
    {  # career fair, Jaimi, host
        'event_id': 1,
        'user_id': 1,
        'is_host': True,
    },
]

event_locations = [
    {  # bball game, gym
        'event_id': 0,
        'location_id': 0,
    },
    {  # career fair, room a
        'event_id': 1,
        'location_id': 1,
    },
]

locations = [
    {
        'id': 0,
        'address': '24 Center Ct',
        'name': 'Gymnasium'
    },
    {
        'id': 1,
        'address': '614 Main St',
        'name': 'Room A - Chrysler Building'
    },
]