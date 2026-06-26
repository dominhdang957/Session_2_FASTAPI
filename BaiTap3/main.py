from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "An", "status": "active"},
    {"id": 2, "name": "Binh", "status": "inactive"},
    {"id": 3, "name": "Cuong", "status": "active"},
    {"id": 4, "name": "Dung", "status": "pending"}
]



@app.get("/student/active")
def get_student_active():
    result = []
    for i in range(len(students)):
        if students[i]["status"] == "active":
            result.append(students[i])
    return {
                "message":"Danh sách sinh viên đang học",
                "data" : result
            }

# 1. Input của bài toánDanh sách dữ liệu thô ban đầu gồm nhiều sinh viên.Mỗi sinh viên là một đối tượng chứa
# 3 thông tin định danh: mã số (id), tên (name), và trạng thái hoạt động (status).
# 2. Output mong muốnMột phản hồi (Response) dạng JSON chứa danh sách các sinh viên đã được lọc.
# Cấu trúc phản hồi phải linh hoạt, thay đổi dựa trên kết quả tìm kiếm thực tế để thông báo rõ ràng cho người dùng.
# 3. Điều kiện xác định sinh viên đang họcHệ thống căn cứ vào trường dữ liệu status của từng sinh viên.
# Sinh viên được coi là đang học khi và chỉ khi giá trị của trường status bằng chính xác chuỗi ký tự "active".