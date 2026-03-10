from fastapi import FastAPI 
from contextlib import asynccontextmanager
from app.db.database import engine, Base
from app.routers import products, categories, carts, users, auth, accounts

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Import models to ensure they are registered
    from app import models
    # Create tables on startup
    Base.metadata.create_all(bind=engine)
    yield

description = """
Welcome to the E-commerce Management System API! 🚀

This API provides a comprehensive set of functionalities for managing your e-commerce platform.

Key features include:

- **Crud**
	- Create, Read, Update, and Delete endpoints.
- **Search**
	- Find specific information with parameters and pagination.
- **Auth**
	- Verify user/system identity.
	- Secure with Access and Refresh tokens.
- **Permission**
	- Assign roles with specific permissions.
	- Different access levels for User/Admin.
- **Validation**
	- Ensure accurate and secure input data.


For any inquiries, please contact:

* Github: https://github.com/ashwani-199/Ecommerce_Backend_FastApis
"""
app = FastAPI(
    description=description,
    title="E-commerce Management System API",
    version="1.0.0",
    contact={
        "name": "Ashwani Kumar",
        "url": "https://github.com/ashwani-199/Ecommerce_Backend_FastApis"
    },
    swagger_ui_parameters={
        "syntaxHighlight.theme": "monokai",
        "layout": "BaseLayout",
        "filter": True,
        "tryItOutEnabled": True,
        "onComplete": "Ok"
    },
    lifespan=lifespan
)

@app.get("/")
async def welcome():
    return {"message": "Welcome to the E-commerce Management System API! Visit /docs for API documentation."}

app.include_router(auth.router)
app.include_router(accounts.router)
app.include_router(users.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(carts.router)


