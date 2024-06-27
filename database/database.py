import pymongo
import os
from config import DB_URI, DB_NAME

dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

user_data = database['users']

async def present_user(user_id: int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int, username: str, name: str):
    user_data.insert_one({'_id': user_id, 'username': username, 'name': name})
    return

async def full_userbase():
    user_docs = user_data.find()
    users = []
    for doc in user_docs:
        users.append({'user_id': doc['_id'], 'username': doc.get('username'), 'name': doc.get('name')})
    return users

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return
