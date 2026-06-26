from fastapi import FastAPI

app = FastAPI()
student = [ 
    {"name":"Đặng"},
    {"name":"Tân"},
    {"name":"Lan"}
    ]
#luồng xử lý nó sẽ trả về một chuỗi json
#Vì nếu trả về string thì nó khó đọc 
#lỗi tên khong được là động từ

@app.get("/student")
def get_student():
    return student 

