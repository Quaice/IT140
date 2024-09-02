#loadlevels.py
import json

from auria.objects.room import Room

def loadLevels():
    levels = []

    with open('rooms.json', 'r') as file:
        rooms = json.load(file)

    for room in rooms:
        for setting in room['settings']:
            for x in setting:
                room[x] = setting[x]

        _id = room['id']
        name = room['name']
        description = room['description']
        short_description = room['short_description']
        items = room['items']
        exits = room['exits']
        levels.append(Room(_id, name, description, short_description, items, exits))

    return levels