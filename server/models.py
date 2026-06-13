import os

from pymongo import MongoClient
from werkzeug.security import check_password_hash, generate_password_hash

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/***REMOVED***")
client = MongoClient(MONGO_URI)
db = client.get_database()


class User:
    def __init__(self, email, password_hash):
        self.email = email
        self.password_hash = password_hash

    @classmethod
    def find_by_email(cls, email):
        user = db.users.find_one({'email': email})
        if user:
            return cls(user['email'], user['password'])
        return None

    @classmethod
    def create(cls, email, password):
        """Yeni kullanici olustur; sifre hashlenerek saklanir."""
        password_hash = generate_password_hash(password)
        return cls(email, password_hash)

    def check_password(self, password):
        """Duz metin sifreyi saklanan hash ile dogrula."""
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)

    def save(self):
        db.users.insert_one({
            'email': self.email,
            'password': self.password_hash
        })
