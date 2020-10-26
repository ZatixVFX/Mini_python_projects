import pymongo

"""
mongo_uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(mongo_uri)
database = client["fullstack"]
collection = database["students"]

students = collection.find({})
students_list = [student["mark"] for student in students]
print(students_list)
print(database["posts"].find_one({"_id": ObjectId("5f92953f9e46f653f84fe182")}))
"""


class Database:
    def __init__(self):
        self.database = None
    URI = "mongodb://127.0.0.1:27017"

    def connect(self):
        client = pymongo.MongoClient(Database.URI)
        self.database = client["fullstack"]

    def find(self, collection, query):
        return self.database[collection].find(query)

    def find_one(self, collection, query):
        return self.database[collection].find_one(query)

    def insert(self, collection, data):
        return self.database[collection].insert_one(data)


db = Database()
db.connect()

users = db.find("users", {})
# print(db.find_one("posts", {"_id": "5f92953f9e46f653f84fe182"}))

# print([user for user in users])
"""
print(db.insert("users", {
    "user": "JohnDoe",
    "email": "JohnDoe@example.com",
    "password": "JohnDoe123"
}))
"""
