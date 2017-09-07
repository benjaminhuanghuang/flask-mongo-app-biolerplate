## Skip test class or method
    ```
    @unittest.skip("skipping")
    
    @unittest.skipIf(mylib.__version__ < (1, 3), "not supported in this library version")
    
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    ```
## Expect exception
    ```
    
    ```
    
## Using testing database and clear db for each test
    ```
    class UserTest(unittest.TestCase):
        def create_app(self):
            return create_app('test')
    
        def setUp(self):
            self.flask_app = self.create_app()
            self.test_client = self.flask_app.test_client()
    
        def tearDown(self):
            db = _get_db()
            db.client.drop_database(db)
    
    ```
    
## Test flask app
    def setUp(self):
        self.flask_app = self.create_app()
        self.test_client = self.flask_app.test_client()
