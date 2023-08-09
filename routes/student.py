# Importing the required libraries
from fastapi import APIRouter, HTTPException
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

# Creating the router object
student_router = APIRouter()

# Creating the end point for hello world
@student_router.get('/helloworld')
async def Hello_world():
    return {"Hello World"}

# Finding all the students
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())

# Finding a student by id
@student_router.get('/students/{id}')
async def find_student_by_id(id: str):
    # Checking if the student exists and then returning the student
    student = connection.local.student.find_one({"_id": ObjectId(id)})
    if student:
        return studentEntity(student)
    # If the student does not exist, then raise an exception
    else:
        raise HTTPException(status_code=404, detail=f"Student with id {id} not found")

# Creating a student
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())

# Updating a student
@student_router.put('/students/{id}')
async def update_student(id: str, student: Student):
    # Checking if the student exists and then updating the student
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(id)}, 
        {"$set": dict(student)}
    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(id)}))

# Deleting a student
@student_router.delete('/students/{id}')
async def delete_student(id: str):
    # Checking if the student exists and then deleting the student
    deleted_student = connection.local.student.find_one({"_id": ObjectId(id)})
    if deleted_student:
        connection.local.student.delete_one({"_id": ObjectId(id)})
        return listOfStudentEntity(connection.local.student.find())
    # If the student does not exist, then raise an exception
    else:
        raise HTTPException(status_code=404, detail=f"Student with id {id} not found")