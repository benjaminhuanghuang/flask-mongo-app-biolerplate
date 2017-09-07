import os
from app import create_app
from flask.ext.script import Manager
# Flask-Script is an extension that adds command line options to Flask

app = create_app('default')
manager = Manager(app)

@manager.command
def test():
    from subprocess import call
    call(['nosetests', '-v',
          '--with-coverage', '--cover-package=app', '--cover-branches',
          '--cover-erase', '--cover-html', '--cover-html-dir=cover'])


@manager.command
def adduser(email, username, admin=False):
    """Register a new user."""
    from getpass import getpass
    password = getpass()
    password2 = getpass(prompt='Confirm: ')
    if password != password2:
        import sys
        sys.exit('Error: passwords do not match.')

    # save user

    print('User {0} with password {1} was registered successfully.'.format(username, password))


if __name__ == "__main__":
    manager.run()

# usage:
# (venv) $ python manage.py runserver
