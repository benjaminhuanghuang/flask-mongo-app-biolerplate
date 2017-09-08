## Use mongod.conf
    ```
    systemLog:
       destination: file
       path: "/home/ubuntu/log/mongod.log"
       logAppend: true
    storage:
       journal:
          enabled: false
       dbPath: "/home/ubuntu/data"
    processManagement:
       fork: true
    net:
       bindIp: 0.0.0.0
       port: 27017
       http:
          enabled: true
          RESTInterfaceEnabled: true
    ```
## PyMongo Config
    - https://flask-pymongo.readthedocs.io/en/latest/
    
    - MONGO_URI
    - MONGO_HOST
    - MONGO_PORT

## Flask-mongoengine config
    http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
    
    
## mongod restart script
    ```
    rm -fr ~/data/mongod.lock
    mongod -f mongod.conf
    ```
    
## Mongo model design
   - create model
    ```
    from app import db

    class User(db.Document):
        username = db.StringField(db_field="u", required=True, unique=True)

    ```
   - pre save hook 
    ```
    # Signal support is provided by the excellent blinker library.
    from mongoengine import signals

    class User(db.Document):
        @classmethod
        def pre_save(cls, sender, document, **kwargs):
            document.username = document.username.lower()
            document.email = document.email.lower()
    
    
    signals.pre_save.connect(User.pre_save, sender=User)
    ```
        - troubleshooting 
            In test cases(unit-testing), Django pre_save signal can not be caught


   - add index
   ```
   meta = {
        'indexes': ['username', 'email', '-created']
    }
    
   ```