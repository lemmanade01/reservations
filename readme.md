# Take Home Challenge: Melon Tasting Scheduler

* [Setup]

    * [Install Python dependencies]
    * [Initialized the database]
    * [Run Flask Server]

Prior to setup, install:

- Python 3.0
- PostgreSQL

- Create a virtual environment --> virtualenv env
- Activate the environment --> source env/bin/activate 
- Install dependencies from 'requirements.txt' --> pip3 install -r requirements
- Initialize the database and title it reservations --> createdb reservations
- Run the flask server --> python3 server.py

# System Design
### Architecture

#### Flask Server
- Ideal for quickly building features and easily deployable which is fitting for the time constraint for this project
- Integrated support for unit testing

#### PostgreSQL
- Support complex queries which enables ease when filter user's search results

#### Javascript
- Speed and versatility to enhance user experience and increase response time
- Increases maintainability and readability

# Future To-Dos
- Due to the time constraint and lack of familiarity with datetime, I would like to refactor my code so I can utilize Python's DateTime library. It will create cleaner code, more efficiency and better readability. As an alternative, I utilized strings for my dates and integers for my start and end times within my reservations table to make my queries functionable and to get results within specified time ranges.
- I would like to enable user's to cancel reservations upon booking, as well as the option to cancel reservations on their reservations page
- Creating tests will allow me to catch bugs and ensure the app is functioning as intended and cross check query results
- I would also like to include a helper functions file to separate out the logic within my routes in my server.py for better maintainability and easier readability
