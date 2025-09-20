"""
User DAO (Data Access Object)
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
from bson import ObjectId
from models.user import User

class UserDAOMongo:
    def __init__(self):
            load_dotenv(find_dotenv())
          
          
            db_host = os.getenv("MONGODB_HOST")
            db_name = os.getenv("MYSQL_DB_NAME")
            db_user = os.getenv("DB_USERNAME")
            db_pass = os.getenv("DB_PASSWORD")    
            # Par exemple
            self.client = MongoClient (host=db_host, username=db_user, password=db_pass)
            self.db = self.client[db_name]
            self.col = self.db["users"]
        
    def select_all(self):
        """ Select all users from MySQL """
        docs = list(self.col.find({}, {"name": 1, "email": 1}))
        return [User(str(d["_id"]), d.get("name", ""), d.get("email", "")) for d in docs]
    
    def insert(self, user):
        """ Insert given user into MySQL """
        res = self.col.insert_one({"name": user.name, "email": user.email})
        return str(res.inserted_id)

    def update(self, user):
     
     if not user.id:
        raise ValueError("user.id est requis pour update()")
     oid = ObjectId(user.id) 
     res = self.col.update_one(
        {"_id": oid},
        {"$set": {"name": user.name, "email": user.email}}
     )
     return res.modified_count 

    def delete(self, user_id):
     
     oid = ObjectId(user_id)
     res = self.col.delete_one({"_id": oid})
     return res.deleted_count 
 
    def delete_all(self): #optional
        """ Empty users table in MySQL """
        self.col.delete_many({})
        
    def close(self):
        self.cursor.close()
        self.conn.close()
