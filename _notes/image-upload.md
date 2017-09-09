## Dependencies
    Install lib on linux 
    sudo apt-get install imagemagick libmagickcore-dev
    
    pip install Wand

## Usage
```
    python manage.py shell
    >>> form wand.image import Image
    >>> with Image(filename='static/assets/batman_logo.png') as img:
    >>>    print(img.size)
    
```
## View/routes, Form and template
    - Routes of /edit
    ```
    ```
    
    - From
    ```
    from flask_wtf.file import FileField, FileAllowed
    
    class EditForm(BaseUserForm):
        image = FileField('Profile image', validators=[
            FileAllowed(['jpg', 'jpeg', 'png', 'gif'],
            'Only JPEG, PNG and GIFs allowed')
            ])
    ```
    - In template, allow sending files through html form
    ```
    <form method="POST" action="{{ url_for('.edit')}}" role="form" enctype="multipart/form-data">
    ```
## User avatar
    - user model

## Image Utilities
    thumbnail_process
    
    
    
    