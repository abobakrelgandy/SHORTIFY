#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
from core.db import DBStorage
from sqlalchemy import inspect
from core.models import URL
# import string
# import random

storage = DBStorage()
storage.reload()


def show_tables(storage):
    inspector = inspect(storage._DBStorage__engine)
    tables = inspector.get_table_names()
    print("Tables in the database:", tables)
    
# def generate_short_code(length=6):
#     characters = string.ascii_letters + string.digits
#     print(characters)
#     short_code = ''.join(random.choice(characters) for _ in range(length))
#     return 'Code_Alpha/' + (short_code)

show_tables(storage)
# x = generate_short_code()
# print(x)
print ("Done")
