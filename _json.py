import json

file_path = "./demo.json"

# read file
with open(file_path, "r") as fp:
    data = json.load(fp)

# Accessing the data
books = data['books']
authors = data['authors']
users = data['users']

# Print out the data to verify
print("Books:")
for book in books:
    print(book)

print("\nAuthors:")
for author in authors:
    print(author)

print("\nUsers:")
for user in users:
    print(user)

print(json.dumps(users, indent = 4, sort_keys = False))