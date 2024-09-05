# Object.py

class Object:
    def __init__(self, id, name , description):
        self.id = id
        self.name = name
        self.description = description

    def describe(self):
        print(self.description)