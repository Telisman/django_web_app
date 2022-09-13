# django_web_app
This web application is intended for interaction between two types of users, it contains messaging, adding posts, editing profiles and more.

Setup:

The first thing to do is to clone the repository:

        $ git clone https://github.com/Telisman/django_web_app.git
        $ cd django_web_app

Create a virtual environment to install dependencies in and activate it:

        $ virtualenv --no-site-packages env
        $ source env/bin/activate

Then install the dependencies:

        (env)$ pip install -r requirements.txt

Once pip has finished downloading the dependencies:

        (env)$ python manage.py runserver
        And navigate to http://127.0.0.1:8000/Housemaster/


This application consists of two parts:

        1.Housemaster page: which contains web pages for sing-up and sing-in forms.As well as the home page with information about registration and are dashboard
        
                After logging in to our site, the user will have created his own dashboard page.
                Depending on which user you selected, the dashboard will give you certain options depending on the user.
        
        2.Dashboard page:allows posting ads, exchanging messages between users, and viewing all users and ads.
                  Depending on which user you selected, the dashboard will give you certain options depending on the user
                  
                  
Demo websites can be found at:
        https://majstor.cloud-petkovic.com/Housemaster/
      
 THANKS FOR VISITING
