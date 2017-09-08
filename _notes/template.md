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
## Template macro
    ```
    {% macro render_field(field) %}
  
    {% endmacro %}
    ```
    using macro
    ```
    {% from "_formhelpers.html" import render_field %}
      
    {{ render_field(form.username, class='form-control') }}
     
    ```