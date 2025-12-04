from pymongo import MongoClient
import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/crypto_forcast")
client = MongoClient(MONGO_URI)
db = client.get_database()

client = MongoClient('mongodb://localhost:27017')
db = client['crypto_forcast']

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def find_by_email(cls, email):
        user = db.users.find_one({'email': email})
        if user:
            return cls(user['email'], user['password'])
        return None

    def save(self):
        db.users.insert_one({
            'email': self.email,
            'password': self.password
        })