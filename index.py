# Import FastAPI
from fastapi import FastAPI
from routes.student import student_router

# Create the app object
app = FastAPI()

# Register the router object
app.include_router(student_router)