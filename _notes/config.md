## Reference
    - https://damyanon.net/flask-series-configuration/
    
## File based config
    config.py
    ```
    SECRET_KEY = 'you-will-never-guess'
    DEBUG=True
    MONGODB_DB = 'flaskbook'
    ```
    
    in app, the config can be overwritten
    ```
    def create_app(**config_overrides):
        app.config.from_pyfile('config.py')
        app.config.update(config_overrides)
    ```
    
    We can overwrite config in testing
    ```
    return create_app(
            MONGODB_SETTINGS={'DB': self.db_name},
            TESTING=True,
            WTF_CSRF_ENABLED=False,
            SECRET_KEY='mySecret',
            )
    
    ```

## Object based config
    In app
    ```
    from config import config
    
    app.config.from_object(config[config_name])
    
    app.config.update(dict())
    ```
    
    In config.py
    ```
    config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
    
        'default': DevelopmentConfig
    }
    ```
    Using object object, we can derive config from base config
    ```
    class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY')
        MAIL_SERVER = 'smtp.googlemail.com'
        
    class DevelopmentConfig(Config):

    ```
    
    we can use testing config in testing
    ```
    return create_app('test')
    
    ```
    
## Env vars based config
    ```
    app.config.from_envvar('FLASK_CONFIG_FILE')
    ```