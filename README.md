

## Setup
- To start MongoDB - brew services start mongodb/brew/mongodb-community 
- Install FastAPI Uvicorn for MongoDB - pip3 install pymango fastapi uvicorn 


## Starting FastAPI Server
- Create your index.py file.
	- from fastapi import FastAPI
	- Create the app object: app = FastAPI() 
- Start the FastAPI Server - uvicorn <index_filename>:<appname> --reload 
	- Example:  uvicorn index:app --reload . 
	- For this, ensure that the index.py  file is already available. Also, ensure that you are in the directory where the file is, while running the command.


## Creating connections, models and routes
- Create the below:
	- config/database.py 
		- has database connections
	- models/student.py 
		- from pydantic import BaseModel 
		- Create the class Student with the schema.
	- routes/student.py 
		1. from fastapi import APIRouter
		2. Import class Student from models.student 
		3. Import variable connection from config/database.py 
		4. Create student_router 
			- Create the endpoint for the router
			- Create the function which does the compute, in async mode to parallelize.
		5. Include the above student_router in index.py .
			- Import the router - from routes.student import student_router 
			- Register the router  using app.include_router(student_router) 
			- Now, refresh the swagger UI at http://127.0.0.1:8000/docs 
				- The request URL would be `http://127.0.0.1:8000/<string after VERB>`
	- schemas/student.py



## Schema creation and implementing converter
- Schemas help to serialize and convert the MongoDB format JSON to UI required JSON
- Under schemas.student.py , create the below functions
	- studentEntity
		- Function for passing an item (document) to the Database (MongoDB in this case) and returning the document objects (fields) as a dictionary.
	- listOfStudentEntity
		- Function to pass a list of items, and return the above schema for multiple documents.
- Import the above functions to the routes file routes.student.py 
	- from schemas.student import studentEntity, listOfStudentEntity
	- Add the listOfStudentEntity to the router /students  connection so that all students are passed when the API is called.
```
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())
```


## Implement a create API
- All done in the routes.student.py file. 
	- Just create more and more routes, if you are using the same router. This will get automatically reflected in the Fast API as the rest of the set ups are the same.