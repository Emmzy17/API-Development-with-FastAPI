from http.client import HTTPException
from fastapi import APIRouter, Depends, status, Response 
from app import schema, models, database, oauth2
from sqlalchemy.orm import Session
router = APIRouter(
    prefix='/vote',
    tags=['Vote']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: schema.Vote, db: Session =  Depends(database.get_db), current_user: int= Depends(oauth2.get_current_user)):
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = f"user {current_user.id} has already posted on post {vote.post_id}")
        new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {'message': 'Successfully updated vote'}

    else:
        if not found_vote:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "Vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {'message': 'Successfully deleted post'}