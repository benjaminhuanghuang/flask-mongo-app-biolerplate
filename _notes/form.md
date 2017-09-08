## Dependency
    ```
    $ pip install Flask-WTF
    ```
    
    code
    ```
    git://github.com/lepture/flask-wtf.git
    ```

## Validation
    ```
    first_name = StringField('First Name', [validators.DataRequired()])
    last_name = StringField('Last Name', [validators.DataRequired()])
    email = EmailField('Email address', [
        validators.DataRequired(),
        validators.Email()
    ]
    ```


