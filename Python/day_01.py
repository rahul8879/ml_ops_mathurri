import json
import uuid

data = {}

def create_user(name, age):
    user_id = str(uuid.uuid4())
    data[user_id] = {"name": name, "age": age}
    with open("data.json", "w") as f:
        json.dump(data, f)
    return user_id


def search_user(user_id):
    with open("data.json", "r") as f:
        data = json.load(f)
    return data[user_id]



# create_user("John", 30)



# print(data)
# print(data['b941bce3-e953-4e15-98db-2eeb4dd766e2'])