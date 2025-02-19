import sqlite3
import os
from flask import g

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")

def get_db():
   connection = g.get("db", None)
   print('Database Path:', db_path)
   if connection is None:
      g.db = sqlite3.connect(db_path)
      g.db.row_factory = sqlite3.Row
      return g.db
   else:
      return connection
