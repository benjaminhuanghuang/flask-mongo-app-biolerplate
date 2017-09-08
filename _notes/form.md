## Dependency
    ```
    $ pip install Flask-WTF
    ```
    
    - Resources
    ```
    https://flask-wtf.readthedocs.io/en/stable/
    git://github.com/lepture/flask-wtf.git
    ```
## BaseFrom
    ```
    class BaseUserForm(FlaskForm):
    
        
    class RegisterForm(BaseUserForm):
    ```
## Validation
    ```
    from wtforms import validators
    from wtforms.validators import ValidationError
    
    
    first_name = StringField('First Name', [validators.DataRequired()])
    last_name = StringField('Last Name', [validators.DataRequired()])
    email = EmailField('Email address', [
        validators.DataRequired(),
        validators.Email()
    ]
    ```
    
## Custom validators
    - http://wtforms.readthedocs.io/en/latest/validators.html
    ```
    class MyForm(Form):
        name = StringField('Name', [InputRequired()])
        
        def validate_name(form, field):
            if len(field.data) > 50:
                raise ValidationError('Name must be less than 50 characters')
    ```
    
    Use function
    ```
    def my_length_check(form, field):
    if len(field.data) > 50:
        raise ValidationError('Field must be less than 50 characters')

    class MyForm(Form):
        name = StringField('Name', [InputRequired(), my_length_check])
    ```
##  Display validation error message
    
