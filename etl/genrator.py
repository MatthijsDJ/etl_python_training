import asyncio
import httpx

# https://randomuser.me/api/

# def call_random_user():
#     url = 'https://randomuser.me/api/'
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         return data
#     else:
#         print('Could not fetch data.')

async def random_name():

    while True:
        url = 'https://randomuser.me/api/'
        response = await httpx.get(url)
        data = response.json()
        if data:
            first_name = data['results'][0]['name']['first']
            last_name = data['results'][0]['name']['last']
            return (first_name, last_name)

#Person = collections.namedtuple('Person', 'first_name last_name')

def names(count=10):
    people = []
    for index, person in enumerate(random_name()):
        people.append(person)
        #first_name, last_name = person
        
        if index > count:
            break
    return people

def names_as_dict():
    for item in random_name():
        p = Person(item)
        print(p.first_name)


def write_random_names(filename, count):
    with open(filename, 'w') as f:
        for index, person in enumerate(random_name()):
            first_name, last_name = person
            f.write(f'{first_name}, {last_name}\n')
            if index > count:
                break

#write_random_names('names.csv', 20)


async def main():
    for task_count in range(10):
        task = asyncio.create_task(random_name())
        await task

asyncio.run(main())