from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop Dell XPS", "price": 25000000, "category": "Electronics", "stock": 15},
    {"id": 2, "name": "iPhone 15 Pro", "price": 28000000, "category": "Electronics", "stock": 0},
    {"id": 3, "name": "Bàn làm việc gỗ", "price": 15000000, "category": "Furniture", "stock": 5}
]

@app.get("/products")
def get_all_products():
    return {
        "message": "Lấy danh sách sản phẩm thành công",
        "data": products
    }

@app.get("/products/detail")
def get_product_detail():
    return {
        "message": "Lấy chi tiết sản phẩm thành công",
        "data": products[0]
    }

@app.post("/products")
def create_product():
    return {
        "message": "Thêm mới sản phẩm thành công",
        "data": {"id": 4, "name": "Sản phẩm mới", "price": 0, "category": "None", "stock": 0}
    }

@app.put("/products/update")
def update_product():
    return {
        "message": "Cập nhật thông tin sản phẩm thành công",
        "data": {"id": 1, "name": "Laptop Dell XPS (Đã cập nhật)", "price": 24000000, "category": "Electronics", "stock": 10}
    }

@app.delete("/products/delete")
def delete_product():
    return {
        "message": "Xóa sản phẩm thành công",
        "data": None
    }

@app.get("/products/statistics")
def get_products_statistics():
    return {
        "message": "Lấy thống kê sản phẩm thành công",
        "data": {
            "total_products": 3,
            "total_categories": 2,
            "out_of_stock_count": 1
        }
    }

@app.get("/products/out-of-stock")
def get_out_of_stock_products():
    return {
        "message": "Lấy danh sách sản phẩm hết hàng thành công",
        "data": [products[1]]
    }

@app.get("/products/top-expensive")
def get_top_expensive_products():
    return {
        "message": "Lấy danh sách sản phẩm đắt nhất thành công",
        "data": [products[1]]
    }