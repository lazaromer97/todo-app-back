# TODO APP BACK

## Getting Started

First clone the repository from Github and switch to the new directory:

    # SSH
    $ git clone git@github.com:lazaromer97/todo-app-back.git

    # HTTPS
    $ git clone https://github.com/lazaromer97/todo-app-back.git

    $ cd todo-app-back
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply make and apply the migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver