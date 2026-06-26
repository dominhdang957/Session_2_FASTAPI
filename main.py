from fastapi import FastAPI
from pydantic import BaseModel, Field

class StudentSchemaRequest(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "Nguyễn văn A"})
    age: int = Field(..., ge=18, le=100 json_schema_extra={"example": 20})

class StudentSchemaRespond(BaseModel):
    id:int
    name:str
    age:int
    status:str


tags_metadata = [
    {
        "name":"students",
        "description":"Các api liên quan đến quản lý sinh viên"
    }
]


app = FastAPI(
    title="Hệ thống quản lý sinh viên minh đặng",
    description="API này giúp quản lý sinh viên Minh Đặng",
    version="1.0.0",
    contact={"name":"Bộ phận quản lý pháp lý","email":"suporteudd.vnsd"},
    openapi_tags=tags_metadata,
    docs_url="/api/v1/swagger-docs",
    redoc_url="/api/v1/áoefsef"
)

@app.get("/")
def get_root():
    return {"message":"Tôi tên là Đỗ"}

@app.get("/students")
def get_students():
    print("lấy danh sách sinh viên")
    return [{
        "id":1,
        "name":"Đỗ Minh đặng"
    }]

@app.post("/students")
def create_students():
    print("Thêm mới sinh viên")

    return{"message":"Thêm mới thành công"}

@app.put("/students/{student_id}")
def update_student(student_id: int):
    print(f"Cập nhật sinh viên có id là: {student_id}")
    
    return {"message": f"Đã cập nhật thành công sinh viên có id {student_id}"}

@app.patch("/students/{student_id}")
def patch_student(student_id: int):
    print(f"Đã cập nhật một phần dữ liệu của sinh viên có id là {student_id}")

@app.delete("/students/{student_id}")
def delete_student(student_id):
    print(f"Đã xóa thành công sinh viên có id là {student_id}")