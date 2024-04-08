# main.py
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb+srv://boggulavinaykumar649:<password>@cluster0.jexp6dy.mongodb.net/")
db = client.library_management_system

# Define API endpoints
@app.get("/")
async def read_root():
    return {"message": "Welcome to Library Management System"}

@app.get("/books")
async def get_books():
    books = db.books.find({})
    return {"books": list(books)}

# Other endpoints can be added similarly for CRUD operations on books, students, loans, etc.

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)