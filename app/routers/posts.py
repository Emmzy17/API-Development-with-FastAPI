from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List, Optional
from sqlalchemy import func 
#import sys
import oauth2
#sys.path.append('../..')

import  models, schema
from sqlalchemy.orm import Session
from database import get_db

router =  APIRouter(
    prefix='/posts',
    tags=["Post"]
)

@router.get('/', response_model=List[schema.PostOut]) 
#@router.get('/') 
def get_posts(limit:int = 10, skip:int = 0, search :Optional[str] = "",db: Session = Depends(get_db)):

    #cursor.execute(""" SELECT * FROM posts """)
    ##posts = cursor.fetchall()
    #print(posts)
    
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, 
                        models.Vote.post_id == 
                        models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    

    return  results

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.Post)
def create_posts(post:schema.PostCreate, db: Session = Depends(get_db), current_user:int =  Depends(oauth2.get_current_user)):
    #cursor.execute(""" INSERT INTO posts (title, content) VALUES (%s, %s) RETURNING * """, (post.title, post.content) )
    #new_post = cursor.fetchone()
    #conn.commit()
    new_post = models.Post(**post.dict(), owner_id=current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return  new_post 

@router.get('/sqlalchemy')
def test_posts(db: Session = Depends(get_db)):
    return{'status': 'sucess'}

@router.get('/{id}', response_model=schema.Post)
def get_post(id: int, db : Session = Depends(get_db), current_user:int =  Depends(oauth2.get_current_user)):
    #cursor.execute(""" SELECT * from posts WHERE id = %s""", str(id))
    #test_post = cursor.fetchone()
    #post =  find_post(id)
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    return post

@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
def delete_posts(id: int, db: Session = Depends(get_db), current_user:int =  Depends(oauth2.get_current_user)):
    #cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    #deleted_post = cursor.fetchone()
    #index = find_index_post(id)#

    #conn.commit()#
    post = db.query(models).filter(models.Post.id == id)
    deleted_post = post.first()
    
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exit")
    
    if deleted_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"You are not authorised to perform the required action")

    post.delete(synchronize_session=False)

    
    return Response(status_code=status.HTTP_204_NO_CONTENT) 

@router.put('/{id}', response_model=schema.Post, status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, update_post: schema.PostCreate, db: Session = Depends(get_db), current_user:int =  Depends(oauth2.get_current_user)):
    #cursor.execute(""" UPDATE posts SET title = %s, content = %s WHERE id = %s RETURNING * """, (post.title, post.content, str(id)))
    #updated_post = cursor.fetchone()
    #conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exit")
    if updated_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"You are not authorised to perform the required action")
    post.update(update_post.dict(), synchronize_session=False)
    db.commit()
    
    return updated_post