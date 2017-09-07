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