import random
from datetime import datetime

r = random.SystemRandom()

# Use values from https://zaliczenie.aherman.pl/travel
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
        'start_date': '15.06.2022',
        'duration': 10,
        'board': 'All Inclusive'
    },
    {
        'name': 'Cancun Bay Resort',
        'country': 'Mexico',
        'stars': 4,
        'price': 450,
        'start_date': '15.06.2022',
        'duration': 14,
        'board': 'All Inclusive'
    },
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
        'start_date': '15.06.2022',
        'duration': 10,
        'board': 'All Inclusive'
    },
    {
        'name': 'Cancun Bay Resort',
        'country': 'Mexico',
        'stars': 4,
        'price': 450,
        'start_date': '15.06.2022',
        'duration': 14,
        'board': 'All Inclusive'
    },
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
        'start_date': '15.06.2022',
        'duration': 10,
        'board': 'All Inclusive'
    },
    {
        'name': 'Cancun Bay Resort',
        'country': 'Mexico',
        'stars': 4,
        'price': 450,
        'start_date': '15.06.2022',
        'duration': 14,
        'board': 'All Inclusive'
    },
]

DURATIONS_TO_DISPLAY = [7,10,14]

def get_random_trip_by_duration(duration):
    trips_by_duration = [trip for trip in trips if trip['duration'] == duration]
    return trips_by_duration[r.randint(0, len(trips_by_duration) - 1)]

trips_to_display = list(map(get_random_trip_by_duration, DURATIONS_TO_DISPLAY))

# 'Please print values from array printed above in human readable format'
print(trips_to_display)

print('Which tour do you prefer? Select a number from 1 to 3')

picked_trip_number = int(input())
while picked_trip_number > 3 or picked_trip_number < 1:
    print('Wrong option. Select a number from 1 to 3')
    picked_trip_number = int(input())

print('Good job, you picked option')
picked_trip = trips_to_display[picked_trip_number - 1]

adults = 0
childrens = 0

print('How many adults')

adults = int(input())

while not isinstance(adults, int):
    print('Wrong option.')
    adults = int(input())


print('How many childrens')

childrens = int(input())

while not isinstance(childrens, int):
    print('Wrong option.')
    childrens = int(input())


print('Full price')
trip_price = picked_trip['price']
full_price = trip_price * adults + (trip_price / 2) * childrens
print(full_price)

