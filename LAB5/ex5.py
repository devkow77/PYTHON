import json

car = {"mark": "audi", "model": "s3", "horsePower": 400}

# serialize
try:
    car_json = json.dumps(car)
    with open("car_file", "w") as file:
        file.write(car_json)
        print("data has been succesfully saved!")
except (TypeError, ValueError) as e:
    print(f"Error while saving: {e}")

# deserialize
try:
    with open("car_file", "r") as file:
        car_data = json.loads(file.read())
        print(car_data)
except FileNotFoundError as e:
    print("File not exist!")
    exit()

