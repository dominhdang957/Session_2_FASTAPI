from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

courses = [
    {
        "id": 1,
        "code": "PY101",
        "name": "Python Basic",
        "level": "beginner",
        "price": 1500000
    },
    {
        "id": 2,
        "code": "FA101",
        "name": "FastAPI Basic",
        "level": "beginner",
        "price": 2000000
    }
]

@app.get("/health")
def check_system():
    return {"message": "API is running"}


@app.get("/courses")
def get_all_courses():
    return courses

@app.get("/courses/{course_id}")
def get_course(course_id : int):
    if course_id <= 0:
        raise HTTPException(status_code=400,detail="Course id must be greater than 0")
    
    for course in courses:
        if course["id"] == course_id:
            return course
    raise HTTPException(status_code=404,detail="Course not found")
