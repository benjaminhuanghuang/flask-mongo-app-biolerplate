# Flask + Mongo RESTful project biolerplate


## Best Practice
  - Use mongodb and mongoose 
    - Split mongoose setup into a separate file

  - Use app factory pattern and manager for convenience of testing
  
  - Use different config and database for different environment: prod, dev, and testing.
    - Ues test_helper in unit test to reset and clear testing environment before testing.
  
  - log files
  
  