## Dependency
    flask-bootstrap
    - https://pythonhosted.org/Flask-Bootstrap/
    
    ```
    pip install flask-bootstrap
    ```
## Usage
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
    
    Register flask_bootstrap to app
    ```
    from flask import Flask
    from flask_bootstrap import Bootstrap
    
    def create_app():
      app = Flask(__name__)
      Bootstrap(app)
    
      return app
    ```