from fastapi import FastAPI

app = FastAPI()
student = [ 
    {"id":1,"name":"Đặng"},
    {"id":2, "name":"Tân"},
    {"id":3,"name":"Lan"}
    ]


@app.get("/student")
def get_student():
    return student

#endpoin hiện tại trong source code là /student
#vì get /students lại bị not found 404 là khong tìm thấy đường dẫn 
#vì bạn chuyền vào vị trí của sinh viên đầu tiên nên nó chỉ hiện 1 sinh viên
#/student

