# seProject
[Django](https://www.djangoproject.com) web app for CS 4398 Texas State University.

## Requirements
- [python3](https://www.python.org/downloads/) - Programming language.
- [pip](https://pip.pypa.io/en/stable/installing/) - Python package manager.
- [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) - Isolated development environment.

## Pycharm Instructions
- Clone or download the repository.
- With pycharm file > open > where/ever/you/downloaded/seProject
- Create virtualenv
- Install requirements.txt
- Tools > Run manage.py Task...
    ```
    manage.py@seProject > makemigrations accounts resumes
    manage.py@seProject > migrate
    manage.py@seProject > runserver
    ```

## Command Line Setup (Unix)
```
$ git clone https://github.com/yebra06/seProject.git
$ cd seProject
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ ./manage.py makemigrations accounts resumes
$ ./manage.py migrate
$ ./manage.py runserver
```

## Testing
Using pytest
```
$ ./manage.py test
```

## Developers
- Michael Christenson
- Henderson Cooper
- Alfredo Yebra Jr.

## Tools
- PyCharm

## Notes
- User model derived from [here](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)
