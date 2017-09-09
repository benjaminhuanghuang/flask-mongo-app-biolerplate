##  Flask application factory, 
    - as explained here: http://flask.pocoo.org/docs/patterns/appfactories/


## Flask script
    ```
    python manage.py shell
    >>> from app.user.models import User
    >>> user = User.objects.first()
    >>> user.to_json()
    >>> from flask import render_template
    >>> body_html = render_template('mail/user/register.html', user=user)
    >>> print(body_html)
    
    ```