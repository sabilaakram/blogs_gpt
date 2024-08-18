from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, create_db_and_tables
from fastapi.openapi.utils import get_openapi
from .settings import NGROK_URL

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Dependency to get the database session
def get_session():
    with Session(engine) as session:
        yield session


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI",
        version="0.1.0",
        description="Your API description",
        routes=app.routes,
    )
    openapi_schema["servers"] = [{"url": NGROK_URL}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi



@app.post("/blogs/", response_model=schemas.Blog)
async def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_session)):
    return crud.create_blog(db=db, blog=blog)

@app.get("/blogs/", response_model=List[schemas.Blog])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    return crud.get_blogs(db=db, skip=skip, limit=limit)

@app.get("/blogs/{blog_id}", response_model=schemas.Blog)
def read_blog(blog_id: int, db: Session = Depends(get_session)):
    blog = crud.get_blog(db=db, blog_id=blog_id)
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@app.put("/blogs/{blog_id}", response_model=schemas.Blog)
async def update_blog(blog_id: int, blog: schemas.BlogUpdate, db: Session = Depends(get_session)):
    updated_blog = crud.update_blog(db=db, blog_id=blog_id, blog=blog)
    if updated_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return updated_blog

@app.delete("/blogs/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(get_session)):
    deleted_blog = crud.delete_blog(db=db, blog_id=blog_id)
    if deleted_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"detail": "Blog deleted"}
