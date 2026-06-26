from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1, "title": "Python Basic", "quantity": 12},
    {"id": 2, "title": "FastAPI Beginner", "quantity": 3},
    {"id": 3, "title": "Clean Code", "quantity": 5},
    {"id": 4, "title": "Database Design", "quantity": 0},
    {"id": 5, "title": "Web API Design", "quantity": 20}
]

@app.get("/books/low-stock")
def get_book_low_stock():
    result = []
    message = ""
    for i in range(len(books)):
        if "quantity"  in books[i]:
            if 0 <= books[i]["quantity"] <= 5:
                result.append(books[i])
    message = "Không có sách nào sắp hết hàng" if not result else "Các sách hết hàng!"
    return {
    "message": message,
    "data": result
}
            