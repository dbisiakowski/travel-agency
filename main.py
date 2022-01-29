import random
from datetime import datetime

r = random.SystemRandom()

trips = [
    {
        'name': 'Cancun Bay Resort',
        'country': 'Mexico',
        'stars': 4,
        'price': 450,
        'start_date': '15.06.2022',
        'duration': 7,
        'board': 'All Inclusive'
    },
    {
        'name': 'Cancun Bay Resort',
        'country': 'Mexico',
        'stars': 4,
        'price': 450,
        'duration': 7,
        'board': 'All Inclusive'
    },
    {
        'name': 'Cancun Bay Resort',
        'country': 'Mexico',
        'stars': 4,
        'price': 450,
        'duration': 7,
        'board': 'All Inclusive'
    },
    {
        'name': 'Cancun Bay Resort',
        'country': 'Meksyk',
        'stars': 4,
        'price': 450,
        'duration': 7,
        'board': 'All Inclusive'
    }
]

random_trips = []

OFFERS_TO_DISPLAY = 3

for offer_number in range(OFFERS_TO_DISPLAY):
    while len(random_trips) ==  offer_number:
        random_trip = r.randint(0, len(trips) - 1)
        if not random_trip in random_trips:
            random_trips.append(random_trip)



datetime_object = datetime.strptime('2005.01.22', '%Y.%m.%d')

print(datetime_object)



print(random_trips)

