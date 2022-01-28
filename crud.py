"""CRUD operations"""

from model import db, User, Reservation
from datetime import datetime
from sqlalchemy import delete, update, extract


def create_user(user_id, username, password):
    """Create and return a mock user."""
    
    user = User(user_id=user_id,
                username=username,
                password=password)
    
    db.session.add(user)
    db.session.commit()
    
    return user


def get_user_by_username(username):
    """Get and return a user by username"""
    
    user = User.query.filter(User.username==username).first()

    return user


def get_user_by_id(user_id):
    """Get and return a user by id"""
    
    user = User.query.filter(User.user_id==user_id).first()
    
    return user


def create_reservation(date, start_time, end_time, user_id):
    """Create a user's reservation."""
    
    res = Reservation(date=date,
                      start_time=start_time,
                      end_time=end_time,
                      user_id=user_id)
    
    db.session.add(res)
    db.session.commit()
    
    return res


def get_all_scheduled_reservations():
    """Get and return all scheduled reservations."""
    
    reservations = Reservation.query.all()
    
    return reservations


def get_all_scheduled_res_by_user_id(user_id):
    """Get and return all scheduled reservations for user."""
    
    reservations = Reservation.query.filter(Reservation.user_id==user_id).order_by(Reservation.date).all()
    
    return reservations

def get_all_scheduled_res_by_date(date):
    """Get and return all scheduled reservations by date"""
    
    res = Reservation.query.filter(Reservation.date==date).all()
    
    return res


# def get_reservations_by_search_input(user_id):
#     """Get and return all reservations associated with a user."""
    
    
def does_res_date_exist(date, user_id):
    """Check if a reservation already exists
    for logged in user on selected date."""
    
    exist = Reservation.query.filter(Reservation.date==date, Reservation.user_id==user_id).first()
    
    return exist
    
    
def does_res_time_exist(date, start_time, end_time):
    """Check if a reservation already exists on this date
    between the selected start and end times"""
    
    # exist = Reservation.query.filter(Reservation.date_time >= start_time, Reservation.date_time <= end_time).order_by(date_time.asc()).all()
    
    exist = Reservation.query.filter(Reservation.date==date, Reservation.start_time >= start_time, Reservation.end_time <= end_time).all()
    
    return exist
    
    # exist = Reservation.query.filter(Reservation.date==date, Reservation.start_time.between(start_time, end_time).order_by(date_time.asc()).all()
    
# def get_reservations_by_search_input(user_id, date, start_time):
    
# def get_reservations_by_search_input(user_id, date, end_time):
    
# def get_reservations_by_search_input(user_id, date, start_time, end_time):


if __name__ == '__main__':
    from server import app
    connect_to_db(app)