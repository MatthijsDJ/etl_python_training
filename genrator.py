import collections
import requests


# https://randomuser.me/api/

def call_random_user():
    url = 'https://randomuser.me/api/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Could not fetch data.')

def generator():

    while True:
        data = call_random_user()
        if data:
            first_name = data['results'][0]['name']['first']
            last_name = data['results'][0]['name']['last']
            yield (first_name, last_name)


# for name in generator():
#     print(name)
#     input('next')

Person = collections.namedtuple('Person', 'first_name last_name')


def names_as_dict():
    for item in generator():
        p = Person(item)
        print(p.first_name)

def write_random_names(filename, count):
    
    with open(filename, 'w') as f:
        for index, person in enumerate(generator()):
            first_name, last_name = person
            f.write(f'{first_name}, {last_name}\n')
            if index > count:
                break

write_random_names('names.csv', 20)