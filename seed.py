"""Drops, creates and automatically populates the database with data"""

import os
import model
import server
import crud

from datetime import datetime

os.system("dropdb reservations")
os.system("createdb reservations")

model.connect_to_db(server.app)
model.db.create_all()

# Create 3 mock users
for n in range(1,4):
    user_id = n
    username = f"user{n}"
    password = f"enter{n}"
    
    user = crud.create_user(user_id, username, password)

# Creat mock reservations for each mock user
# for x in range(27-32):
#     for n in range(1,4):
#         dt = f"2022-01-{x} 17:30:00"
#         date_time = dt.strftime('%Y-%m-%d %H:%M:%S')
#         user_id = n
        
#         reservation = crud.create_reservation(date_time, user_id)
        
# def func():
#     for x in range(27-32):
#         for n in range(1,4):
#             dt = f"2022-01-{x} 17:30:00"
#             print(dt)
#             date_time = dt.strftime('%Y-%m-%d %H:%M:%S')
#             print(date_time)
#             user_id = n
#             print(user_id)