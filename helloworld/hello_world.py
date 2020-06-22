from pymongo import MongoClient
from pprint import pprint

uri = "localhost:27017"
client = MongoClient(uri)
pprint(client)

db = client["eshop"]
user_coll = db["users"]

new_user = {
    "username": "Topsong",
    "password": "****",
    "email": "123456@sina.com"
}
result = user_coll.insert_one(new_user)
pprint(result)

result = user_coll.find_one({
    "username": "Topsong"
})
pprint(result)

result = user_coll.update_one(
    {
        "username": "Topsong"},
    {
        "$set": {"phone": "123456789"}
    }
)

result = user_coll.find_one({"username": "Topsong"})
pprint(result)
