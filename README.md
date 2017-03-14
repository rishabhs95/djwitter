# twitter clone - django sample app

Django application working as a twitter clone
Lets you follow, post and read to your newsfeed.

# How to Use
This project uses python3 and Postgresql.

Setup postgres on your system and run these commands:

`python3 manage.py makemigrations`
`python3 manage.py migrate`
`python3 manage.py runserver`

## Database
Postgresql needs prior setup and may hinder while running this project.
Switch to sqlite for easier demo of the project.

Go to `twitter/settings.py` and uncomment sqlite database part, while commenting the postgresql part.

This will serve your django application at localost:8000 by default.
