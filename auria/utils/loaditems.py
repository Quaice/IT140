#loaditems.py

import json
from auria.objects.item import Item

def loadItems():
    items = []
    with open('items.json', 'r') as file:
        item_pool = json.load(file)

    for entry in item_pool:
        for item in entry['item']:
            for x in item:
                entry[x] = item[x]

        _id = entry['id']
        name = entry['name']
        description = entry['description']
        items.append(Item(_id, name, description))

    return items