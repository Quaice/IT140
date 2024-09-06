# Object.py

class Object:
    objects = []

    def __init__(self, id, name , description):
        self.id = id
        self.name = name
        self.description = description
        Object.objects.append(self)

    def describe(self):
        print(self.description)