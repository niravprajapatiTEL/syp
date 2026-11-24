
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Python API Server",
    description="Beginner FastAPI backend deployed on Render",
    version="1.0.0"
)

# Temporary in-memory data
students = [
    {"id": 1, "name": "Nirav", "course": "Python"},
    {"id": 2, "name": "Meet", "course": "AI"}
]

# Request data validation
class Student(BaseModel):
    name: str
    course: str


@app.get("/")
def home():
    return {
        "message": "Welcome to Python Backend API",
        "status": "success"
    }


@app.get("/about")
def about():
    return {
        "project": "Python API Server",
        "technology": "FastAPI",
        "developer": "Python Backend"
    }


@app.get("/contact")
def contact():
    return {
        "email": "info@example.com",
        "message": "Contact us for more information"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Server is running"
    }


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.post("/students")
def add_student(student: Student):
    new_student = {
        "id": max([s["id"] for s in students], default=0) + 1,
        "name": student.name,
        "course": student.course
    }

    students.append(new_student)

    return {
        "message": "Student added successfully",
        "student": new_student
    }
