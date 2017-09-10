## Base template

 derive base template for bootstrap/base.html. It will involve bootstrap css file 
    
    ```
    {% extends "bootstrap/base.html" %}
    {% block title %}This is an example page{% endblock %}
    
    {% block navbar %}
    <div class="navbar navbar-fixed-top">
      <!-- ... -->
    </div>
    {% endblock %}
    
    {% block content %}
      <h1>Hello, Bootstrap</h1>
    {% endblock %}
    ```
## Reuse  component and Template macro  
    ```
    {% macro render_field(field) %}
  
    {% endmacro %}
    ```
    using macro
    ```
    {% from "_formhelpers.html" import render_field %}
      
    {{ render_field(form.username, class='form-control') }}
     
    ```
    
    ```
    {% extends "base.html" %}
    {% from "user/_rel_button.html" import rel_button, rel_js %}
    ```

## Show message and error
    Create message and error in views/routes
    ```
    render_template("user/edit.html", form=form, error=error, message=message)
    ```
    
    Display 
    ``
    {% if error %}
    <div class="alert alert-danger" role="alert">{{ error }}</div>
    {% endif %}

    {% if message %}
    <div class="alert alert-success" role="alert">{{ message }}</div>
    {% endif %}

    ```
## Test by using flask script
    ```
    python manage.py shell
    >>> from user.models import User
    >>> user = User.object.first()
    >>> from flask import render_template
    >>> body_html = render_template('/user/register.html', user=user)
    ```
    
