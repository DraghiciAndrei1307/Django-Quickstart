# Django-Quickstart

## Description

This project is just a tutorial that I tried to complete in order to understand how to work with Django REST Framework.
I simply followed the steps described in this quickstart guide: 
https://www.django-rest-framework.org/tutorial/quickstart/

As the tutorial says, this API allows admin users to view and edit the users and groups in the system. 


## How to use

In order to use this project, you have to clone it onto your machine/VM, using the following command:

```commandline
git clone https://github.com/DraghiciAndrei1307/Django-Quickstart.git
```

After you successfully managed to clone it locally, you have to perform the following steps(check also the quickstart 
tutorial) :

1) Create a virtual environment to isolate the Python packages used by this project

```commandline
cd Django-Quickstart

python3 -m venv .venv

source .venv/bin/activate
```

2) Install Django and Django REST into the virtual environment

```commandline
pip install djangorestframework
```

3) Sync your database for the first time

```commandline
python manage.py migrate
```

4) Create the super user that will allow you to view and edit the other users

```commandline
python manage.py createsuperuser --username admin --email admin@example.com
```

5) This is a step that is not part of the tutorial documentation, but it was useful to me as I run the appication on a
designated private VM on my local network. What I did was to open the default port 8000 that the django server app uses.
To do that, I used the following:

- Check if the firewalld is active

```commandline
sudo systemctl status firewalld
```

- If firewalld is not active, start and make it auto-start when the server boots

```commandline
sudo systemctl start firewalld
sudo systemctl enable firewalld=
```

- Open the port TCP 8000

```commandline
sudo firewall-cmd --permanent --add-port=8000/tcp
```

- Reload the firewall configurations

```commandline
sudo firewall-cmd --reload
```

6) Run the Django REST server app

```commandline
python manage.py runserver 0.0.0.0:8000
```

## The logic under the hood

All of this infrastructure works using this flow:

Request > urls.py (router) > UserViewSet (ModelViewSet) > QuerySet (ORM -> SQLite) > Serializer > Response

The router (check the `urls.py` script) basically links the URL and the UserViewSet. It automatically creates these:
    
    - GET /users/
    - GET /users/1/
    - POST /users/
    - PUT /users/1/

The UserViewSet interrogates the database and returns a queryset which is transformed in a dictionary by the serializer.