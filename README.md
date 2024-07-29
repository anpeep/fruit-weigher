# Fruit Weigher Project

## Overview

This project allows users to sign up, log in, and add weights to fruits declared by the admin. The admin can manage the list of fruits, and users can log in to input weights for these fruits.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- **Pip**

### Clone the Repository

Clone this repository to your local machine:
```bash
git clone https://github.com/anpeep/fruit-weigher.git
cd fruit-weigher/src
```
## Install Python (on Linux)
Install the necessary Python packages:
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10 python3.10-venv python3.10-dev
```
## Set Up the Environment (on Linux/Mac)

Create a Virtual Environment (recommended)
Create a virtual environment to isolate your project dependencies:
```bash
python3.10 -m venv myenv
source myenv/bin/activate
```
## Install Django (on Linux)
Install the necessary Python packages:
```bash
pip install Django==5.0.7
pip install django-allauth
```
## Database Migrations

Set up the database schema by running:
```bash
python manage.py makemigrations
python manage.py migrate
```
## Run the Development Server
```bash
python manage.py runserver
```
Open your browser and go to http://127.0.0.1:8000 to view the application.

## User Guide

### Sign Up and Log In
#### Sign Up

- **Navigate to the sign-up page.**
- **Provide a username, password (must be at least 8 characters long, include uppercase, lowercase, and digits), and complete the registration.**
#### Log In

- **Navigate to the login page.**
- **Enter your username and password to access the user dashboard.**

### User Dashboard
Once logged in, you can:

- **Add Weight: Select a fruit from the list declared by the admin and enter the weight.**

## Admin Guide

### Admin Credentials
Username: test@gmail.com
Password: Parool1!

## Admin Panel
### Add New Fruits

- **Log in with the admin credentials.**
- **Navigate to the admin page.**
Enter a new fruit name to add it to the list of fruits that users can input weights for.
### Manage Fruits

- **View and manage the list of fruits.**
- **Users will be able to select these fruits to add weights.**

