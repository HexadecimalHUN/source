# Programming Project Hand-IN

A basic Django Project which is capable to store different text entries.

## Main Functionality

- Log-In System
- New User Login System
- Password Modification System
- Log-out System
- Storing Different types of text entries
- User and SuperUser roles
- Language Selection

## Later Development Plan
- See the owner of different entries (User model is done, but could not be implemented because of time limitation)
- 3rd User Role
- Timestamps for Entries
- A static page, to replace the double if part in the code. 

## Basic Usage
1) After starting the server the user has to log-in or create a new account:
    - Existing Profile: user1@example.com PW: administration
2) To edit and add entries goto: localhost:8000/index
3) To exit from User-Role goto: localhost:8000

## SuperUser Role:
- localhost:8000/admin
- UN: superuser
- PW: superuserpassword

## FunFacts:
- After Analyzing the code, you can see that lot of things are still in progress. First of all, an AbstractBaseUser modell is about to be implemented in the models.py file linked to the Index page. The reason behind that, this User Role would be referenced, while linking the events to the author. 
- Buttons are missing, to make it possible to navigate between the Profile and Task page. Will be implemented soon. 

## Used Ones:
- Django Framework
- HTML
- CSS
- Bootstrap 