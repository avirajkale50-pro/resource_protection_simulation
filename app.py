documents = [
    {"id": 1, "owner": "userA", "content": "A's secret"},
    {"id": 2, "owner": "userB", "content": "B's secret"}
]

users = {
    "userA": "user",
    "userB": "user",
    "admin": "admin"
}

username = input("Enter your username: ")
doc_id = int(input("Enter document ID: "))

role = users.get(username)

if role is None:
    print("Unknown user")
    exit()

found_doc = None

for doc in documents:
    if doc["id"] == doc_id:
        found_doc = doc
        break

if found_doc is None:
    print("Document not found")
elif found_doc["owner"] == username or role == "admin":
    print("Content:", found_doc["content"])
else:
    print("Access Denied")
