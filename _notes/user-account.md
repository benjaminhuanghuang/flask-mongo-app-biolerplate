## Forget password
    - Login View + forget password link 
    - Forget password view + Reset password button, send email to user and display message on view
    - Password reset confirm email +  confirm code 
    - Password reset view, input new password
    - password reset complete view + login link
      
## Change password
    - Use password_reset.html template
    - Add link on nav bar
    
## Avatar
    placehold.it
    ```
    <img class="img-thumbnail" src="//placehold.it/200x200" width="200" heigh="200" alt="{{ user.username }}">
    ```
   
    avatar
    ```
    <img class="img-thumbnail" src="{{ user.profile_imgsrc('xlg') }}" width="200" height="200" alt="{{ user.username }}">
    ```