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
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.username = document.username.lower()
        document.email = document.email.lower()
    ```