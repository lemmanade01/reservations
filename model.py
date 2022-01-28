"""Establish the data model and its relationships through object orientation"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    
    """A user."""
    
    __tablename__ = "users"
    
    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    
    reservations = db.relationship("Reservation", backref="users")
    
    def __repr__(self):
        return f"<User user_id={self.user_id} username={self.username} password={self.password}>"


class Reservation(db.Model):
    
    """A reservation."""
    
    __tablename__ = "reservations"
    
    reservation_id = db.Column(db.Integer,
                               autoincrement=True,
                               primary_key=True)
    date = db.Column(db.String, nullable=False)
    start_time = db.Column(db.Integer, nullable=False)
    end_time = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    # date_time = db.Column(db.DateTime, nullable=False)
    # end_time = db.Column(db.String)
    # time = db.Column(db.)
    # interval = db.Column(db.)
    
    def __repr__(self):
        return f"<Reservation reservation_id={self.reservation_id} date_time={self.date_time} user_id={self.user_id}>"
    
    
# class 
    
def connect_to_db(flask_app, db_uri="postgresql:///reservations", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)