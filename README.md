<!-- ABOUT THE PROJECT -->
## Django Client-Organization management system

This is an application built using Python/Django from scratch with the default startproject command.

### Installation

1. Clone the repo, get into the project folder
   ```sh
   git clone https://github.com/SolarDrill/ot-management.git
   ```
2. Install pipenv for the environment
   ```sh
   pip install pipenv
   ```
3. Install the packages
   ```sh
   pipenv install
   ```
4. Run the virtual environment
   ```sh
   pipenv shell
   ```
5. Apply the migrations
   ```sh
   python manage.py migrate
   ```
6. Create a superuser
   ```sh
    python manage.py createsuperuser
   ```
7. Run the Development Server
   ```sh
   python manage.py runserver
   ```
### Description
   This is a Back-End REST API using DRF to manage Clients and Organizations, where multiple Clients can belong to an Organization, a Client could have multiple addresses and an Organization X number of Branches.
   
   Url for the API documentation: http://127.0.0.1:8000/api/v1/docs/
   
### How to run Unit Tests
   ```sh
   python manage.py test
   ```
   
## REMINDER
Check .env.example to know which .envs are needed and the format of the DB URL.   

In addition, there's the possibility to set a Sentry_DNS to keep track of any issue that might occur



