from datetime import datetime
from sqlalchemy.orm import Session
from . import models, schemas

def create_blog(db: Session, blog: schemas.BlogCreate):
    db_blog = models.Blog(
        title=blog.title,
        summary = blog.summary,
        content=blog.content,
        author=blog.author,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog



def update_blog(db: Session, blog_id: int, blog: schemas.BlogUpdate):
    db_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if db_blog:
        db_blog.title = blog.title
        db_blog.content = blog.content
        db_blog.author = blog.author
        db_blog.summary = blog.summary
        db_blog.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_blog)
        return db_blog
    return None


def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Blog).offset(skip).limit(limit).all()

def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()

def delete_blog(db: Session, blog_id: int):
    db_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if db_blog:
        db.delete(db_blog)
        db.commit()
        return db_blog
    return None
