# api/routes/v1_books.py
from fastapi import APIRouter, HTTPException, status
from api.db.database import db
from api.db.schemas import Book

router = APIRouter()

@router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def get_book(book_id: int) -> Book:
    """
    Retrieve a book by its ID.
    Returns:
      - 200: JSON representation of the book if found.
      - 404: {"detail": "Book not found"} if the book does not exist.
    """
    book = db.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
