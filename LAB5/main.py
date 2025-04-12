import pickle
import json

# OBJECT

person = {"name": "Kacper", "surname": "Kowalski"}

# (1) serialise to string of bytes
person_in_bytes = pickle.dumps(person)
print(person_in_bytes)

# (2) write serialised object to file (wb = write binary)
with open("person_in_bytes.pickle", "wb") as file:
    pickle.dump(person, file)

# (3) read serialised object in file as normal object (rb = read binary)
with open("person_in_bytes.pickle", "rb") as file:
    data_loaded = pickle.load(file)
print(data_loaded)

# (4) serialise in json
with open("person_in_bytes.json", "w") as file:
    json.dump(person, file, indent=4)

# (5) read serialised object in file as normal object (deserialise)
with open("person_in_bytes.json", "r") as file:
    data_loaded2 = json.load(file)
print(data_loaded2)

# CLASS

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __repr__(self):
        return f"Person(name: {self.name} surname: {self.surname} age: {self.age})"

john = Person("John", "Smith", 21)

# serialize and deserialize with pickle
with open("john_in_bytes.pickle", "wb") as file:
    pickle.dump(john, file)
with open("john_in_bytes.pickle", "rb") as file:
    data_loaded3 = pickle.load(file)

# serialize and deserialize with json (have to use __dict__)
with open("john_in_bytes.json", "w") as file:
    json.dump(john.__dict__, file)
with open("john_in_bytes.json", "r") as file:
    data_loaded4 = json.load(file)

print(data_loaded3)
print(data_loaded4)