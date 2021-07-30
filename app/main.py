from fastapi import FastAPI
from data.model import Category, MyEmployee
from typing import Optional

app = FastAPI()

fake_employees = [{"first_name": "Danilo", "last_name": "Jakob", "age": 19}, {"first_name": "Nico", "last_name": "Jakob", "age": 18}]
employees = []

@app.get("/")
async def root():
    return {"data": "hello world"}

@app.get("/products/{product_id}")
async def get_product_by_id(product_id: int):
    return {"product_id": product_id}

@app.get("/categories/{category_name}")
async def get_category_by_name(category_name: Category):
    if category_name == Category.LAPTOP:
        return {"message": "We're selling laptops"}
    elif category_name == Category.KITCHEN:
        return {"message": "We're selling kitchen stuff"}
    elif category_name == Category.ELECTRONICS:
        return {"message": "We're selling electronics"}
    else:
        return {"message": "We're not selling {}".format(category_name)}

@app.get("/employee/")
async def get_employee_by_id(employee_id: int = 0, name: Optional[str] = None):
    if name != None:
        for employee in fake_employees:
            if employee.get("first_name") == name:
                return employee
        return {"message": "No Employee Found"}
    else:
        return fake_employees[employee_id]

@app.post("/employee/")
async def create_employee(employee: MyEmployee):
    employees.append(employee)
    return employee

@app.get("/employee/all")
async def get_all_employees():
    return employees
