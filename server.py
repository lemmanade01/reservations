"""Server for Melon Tasting Reservation Scheduler"""

from flask import Flask, render_template, request, flash, session, redirect, jsonify, url_for
from model import connect_to_db
from datetime import datetime
from jinja2 import StrictUndefined

import crud
import helper_functions
import os

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def show_homepage():
    """Show login page."""
    
    return render_template("login.html")


@app.route("/handle-login", methods=["POST"])
def handle_login():
    """Check to see if username and password match."""
    
    # Get user's input
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Get user by entered username
    user = crud.get_user_by_username(username)
    
    # If no user exists by that username 
    # Or the password does not match the username
    if not user or user.password != password:
        # Flash message saying username and email do not match
        flash("Username and Password do not match. Please enter a valid combination.")
        return render_template("login.html")
    
    else:
        # User exists and password matches username
        # Get user's user id
        user_id = user.user_id
        
        # Store user id in session
        session["user_id"] = user_id
        user_in_session = session["user_id"]
        
        # Get user's username to pass to HTML template for display
        username = user.username
        
        return render_template("book_reservations.html", username=username)


@app.route("/search-reservations.json", methods=["POST"])
def search_appointments():
    """Get user's search input from the client side
    
    Check if that user has already schedule a reservation for that date OR if that time slot is already scheduled.
    """
    
    date = request.json.get("date")
    start_time_str = request.json.get("start")
    end_time_str = request.json.get("end")
    
    start_time = int(start_time_str)
    end_time = int(end_time_str)
    
    # dt = date_input + " " + start_time
    # date_time = dt.strptime(dt, "%Y-%m-%d %H:%M")
    
    # Get user id of user in session
    user_id = session.get("user_id")
    
    # Check to see if a reservation already exists for the user on this date
    reservation = crud.does_res_date_exist(date, user_id)

    # If yes, send a response to client side a reservation already exists
    if reservation:
        return jsonify({"exists": "yes", "date": date})
    
    # If no, AND no start or end time is specified, query all available reservations for this date
    
    # Check to see if a reservation alreadys exists in this time slot on this date
    booked_times = crud.does_res_time_exist(date, start_time, end_time)
    
    # All the possible time slots for one day
    rsrvtn_times = {0:'00:00', 1:'12:00am', 2:'12:30am', 3:'1:00am', 4:'1:30am', 5:'2:00am', 6:'2:30am', 7:'3:00am', 8:'3:30am',
    9:'4:00am', 10:'4:30am', 11:'5:00am', 12:'5:30am', 13:'6:00am', 14:'6:30am', 15:'7:00am', 16:'7:30am', 17:'8:00am', 18:'8:30am', 19:'9:00am',
    20:'9:30am', 21:'10:00am', 22:'10:30am', 23:'11:00am', 24:'11:30am', 25:'12:00pm', 26:'12:30pm', 27:'1:00pm', 28:'1:30pm', 29:'2:00pm', 30:'2:30pm',
    31:'3:00pm', 32:'3:30pm', 33:'4:00pm', 34:'4:30pm', 35:'5:00pm', 36:'5:30pm', 37:'6:00pm', 38:'6:30pm', 39:'7:00pm', 40:'7:30pm', 41:'8:00pm', 42:'8:30pm', 43:'9:00pm',
    44:'9:30pm', 45:'10:00pm', 46:'10:30pm', 47:'11:00pm', 48:'11:30pm'}
            
    for booked_time in booked_times:
        if booked_time.start_time in rsrvtn_times:
            rsrvtn_times.pop(booked_time.start_time)
    return jsonify({"date": date, "times": rsrvtn_times})
    

@app.route("/book-reservations.json", methods=["POST"])
def book_reservation():
    
    # Get user id of user in session
    user_id = session.get("user_id")
    
    date = request.json.get("date")
    start_time_str = request.json.get("time")
    
    start_time = int(start_time_str)
    end_time = start_time + 1
    
    # Check to see if a reservation alreadys exists in this time slot on this date
    crud.does_res_time_exist(date, start_time, end_time)
    
    crud.create_reservation(date, start_time, end_time, user_id)
    
    return jsonify({"time": start_time_str})
    
    
@app.route("/schedule")
def schedule_appointments():
    
    # Get user id of user in session
    user_id = session.get("user_id")
    
    user = crud.get_user_by_id(user_id)
    
    username = user.username
    
    return render_template("book_reservations.html", username=username)


@app.route("/all-reservations")
def show_appointments():
    
    # Get user id of user in session
    user_id = session.get("user_id")
    
    reservations = crud.get_all_scheduled_res_by_user_id(user_id)
    
    return render_template("all_reservations.html", reservations=reservations)
    
    

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="localhost", debug=True)
    
    
    
     
        
        # if start_time_int == 0 and end_time_int == 0:
        #     reservations = crud.get_all_scheduled_res_by_date(date)
        #     for res in reservations:
        #         if res.start_time in rsrvtn_times:
        #             rsrvtn_times.pop(res.start_time)
        #     return jsonify({"date": date, "times": rsrvtn_times})
        
        
        
        
        # elif start_time != 0 or end_time != 0:
        #     rsrvtns = crud.get_all_scheduled_res_by_date(date)
        #     for res in rsrvtns:
        #         if res.start_time in rsrvtn_times

        #     if start_time in reservation_times:
        #         reservation_times.remove(start_time)
                
    
    
    
    # date = datetime.strptime(date_input, '%Y-%m-%d')
    # return jsonify({"success": date, "start": start_time, "end": end_time})
    # print(date)
    # print("****************")
   
    # reservation = crud.does_res_date_exist(date, user_id)
    # res_date_time = reservation.date_time
    # print(res_date_time)
    # print("*"*50)
    
    # return jsonify({"Yay!": date})
       
    # if reservation:
    #     return jsonify({"exists": "yes", "date": date})
    
    # else:
        
    #     return jsonify({"exists": "no", "date": date})
        
        
        
        # crud.create_reservation(date, user_id)
        # flash("You already have a reservation scheduled for this date. Please select another date.")
        # return render_template("book_reservation")