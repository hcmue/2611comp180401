from fastapi import FastAPI, status
from fastapi.responses import JSONResponse, HTMLResponse
import json
from pydantic import BaseModel


app = FastAPI()


@app.get("/hello", response_class=HTMLResponse)
def hello(ten: str):
    return f"""<html><body><h1>{ten}</h1></body></html>"""

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

def read_students():
    try:
        with open("students.json", "r", encoding="utf8") as f:
            return json.load(f)
    except:
        return []
    
def write_students(data):
    try:
        with open("students.json", "w", encoding="utf8") as f:
            return json.dump(data, f)
    except:
        return None
        
@app.get("/students")
def get_all_students():
    return read_students()

def find_student_by_id(id: int, data: list):
    for item in data:
        if item["id"] == id:
            return item
    return None

@app.get("/students/{id}")
def get_student_by_id(id: int):
    data = read_students()
    item = find_student_by_id(id, data)
    if item is not None:
        return item
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=f"Not found {id}"
    )

class Student(BaseModel):
    id: int
    name: str
    gpa: float

@app.post("/students")
def add_student(model: Student):
    data = get_all_students()
    # Kiem tra id co chua
    existed_item = find_student_by_id(model.id, data)
    if existed_item is None:
        data.append(model)
        write_students(data)
        return model
    else:
        return {
            "success": False,
            "message": f"Can't create student {model.id}"
        }