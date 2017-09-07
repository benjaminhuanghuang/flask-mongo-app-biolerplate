import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from flask.ext.script import Manager, Server

# Flask-Script is an extension that adds command line options to Flask

app = create_app('default')
manager = Manager(app)

manager.add_comment("runserver", Server(
    use_debugger=True,
    use_reload=True,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 5010))
))


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
