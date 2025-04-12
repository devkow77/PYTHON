import pickle

class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
    def __repr__(self):
        return f"Car (mark: {self.mark} model: {self.model} year: {self.year})"

toyota = Car("toyota", "supra", "2002")

with open("toyota_in_bytes.pickle", "wb") as file:
    pickle.dump(toyota, file)
with open("toyota_in_bytes.pickle", "rb") as file:
    data_loaded = pickle.load(file)
print(data_loaded)