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
        'name': 'Iberostar Quetzal',
        'country': 'Mexico',
        'stars': 5,
        'price': 690,
        'start_date': '15.06.2022',
        'duration': 10,
        'board': 'All Inclusive'
    },
    {
        'name': 'Imperial Laguna by Faranda',
        'country': 'Mexico',
        'stars': 3,
        'price': 320,
        'start_date': '15.06.2022',
        'duration': 14,
        'board': 'All Inclusive'
    },
   {
        'name': 'Playacalida',
        'country': 'Spain',
        'stars': 5,
        'price': 600,
        'start_date': '15.06.2022',
        'duration': 7,
        'board': 'All Inclusive'
    },
    {
        'name': 'Palia Puerto del Sol',
        'country': 'Spain',
        'stars': 3,
        'price': 240,
        'start_date': '15.06.2022',
        'duration': 10,
        'board': 'All Inclusive'
    },
    {
        'name': 'Playa Real Resort',
        'country': 'Spain',
        'stars': 4,
        'price': 380,
        'start_date': '15.06.2022',
        'duration': 14,
        'board': 'All Inclusive'
    },
    {
        'name': 'Sea Gull',
        'country': 'Egypt',
        'stars': 3,
        'price': 270,
        'start_date': '15.06.2022',
        'duration': 7,
        'board': 'All Inclusive'
    },
    {
        'name': 'Continental Hurghada',
        'country': 'Egypt',
        'stars': 4,
        'price': 360,
        'start_date': '15.06.2022',
        'duration': 10,
        'board': 'All Inclusive'
    },
    {
        'name': 'Sharm Grand Plaza',
        'country': 'Egypt',
        'stars': 5,
        'price': 620,
        'start_date': '15.06.2022',
        'duration': 14,
        'board': 'All Inclusive'
    },
    {
        'name': 'Ikaros Hotel',
        'country': 'Grecce',
        'stars': 3,
        'price': 220,
        'start_date': '15.06.2022',
        'duration': 7,
        'board': 'All Inclusive'
    },
    {
        'name': 'Labranda Sandy Beach Resort',
        'country': 'Grecce',
        'stars': 5,
        'price': 580,
        'start_date': '15.06.2022',
        'duration': 10,
        'board': 'All Inclusive'
    },
    {
        'name': 'Lida Corfu',
        'country': 'Grecce',
        'stars': 4,
        'price': 310,
        'start_date': '15.06.2022',
        'duration': 14,
        'board': 'All Inclusive'
    },
    {
        'name': 'Mytt Beach Hotel',
        'country': 'Tailand',
        'stars': 5,
        'price': 720,
        'start_date': '15.06.2022',
        'duration': 10,
        'board': 'All Inclusive'
    },
    {
        'name': 'Novotel Rayong',
        'country': 'Tailand',
        'stars': 4,
        'price': 410,
        'start_date': '15.06.2022',
        'duration': 7,
        'board': 'All Inclusive'
    },
    {
        'name': 'Cholchan Pattaya Resort',
        'country': 'Tailand',
        'stars': 3,
        'price': 290,
        'start_date': '15.06.2022',
        'duration': 10,
        'board': 'All Inclusive'
    },
]

DURATIONS_TO_DISPLAY = [7,10,14]

def get_input_number():
    user_input = input()
    if user_input.isnumeric():
        return int(user_input)  
    else: 
        print('Your value is not number') 
        return -1

def get_random_trip_by_duration(duration):
    trips_by_duration = [trip for trip in trips if trip['duration'] == duration]
    return trips_by_duration[r.randint(0, len(trips_by_duration) - 1)]

trips_to_display = list(map(get_random_trip_by_duration, DURATIONS_TO_DISPLAY))


def display_offers():
    for trip in trips_to_display:
        print('------------------------------------------')
        print('Name',trip['name'])
        print('Country',trip['country'])
        print('Stars',trip['stars'])
        print('Adult price',trip['price'])
        print('Start date',trip['start_date'])
        print('Duration',trip['duration'])
        print('Board',trip['board'])

display_offers()    

print('Which tour do you prefer? Select a number from 1 to 3')

picked_trip_number = get_input_number()
while picked_trip_number > 3 or picked_trip_number < 1:
    print('Wrong option. Select a number from 1 to 3')
    picked_trip_number = get_input_number()

print('Good job, you picked option')
picked_trip = trips_to_display[picked_trip_number - 1]

adults = 0
childrens = 0

print('How many adults')

adults = get_input_number()

while adults < 0:
    print('Wrong option.')
    adults = get_input_number()


print('How many childrens')

childrens = get_input_number()

while childrens < 0:
    print('Wrong option.')
    childrens = get_input_number()


print('Full price')
trip_price = picked_trip['price']
full_price = trip_price * adults + (trip_price / 2) * childrens
print(full_price)

