from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
async def read_item(department: str = None, term: str = None, year: str = None, course: str = None):
    return {"department": department, "term": term, "year": year, "course": course}