import json

book = {"title": "Arthur Lox", "author": "Magic Forest", "pageCount": 350}
book_json = json.dumps(book)

# change object to json
with open("book_json.json", "w") as file:
    file.write(book_json)
with open("book_json.json", "r") as file:
    book_data = json.loads(file.read())
print(book_data)