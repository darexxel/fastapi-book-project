from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from api.db.database import db  # Make sure to import the shared database instance
from api.db.schemas import Book

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    db.add_book(book)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content=book.model_dump()
    )

@router.get("/", response_model=dict, status_code=status.HTTP_200_OK)
async def get_books() -> dict:
    return db.get_books()

# Add the missing GET endpoint for a single book:
@router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def get_single_book(book_id: int) -> Book:
    book = db.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book: Book) -> Book:
    updated_book = db.update_book(book_id, book)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=updated_book.model_dump(),
    )

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int) -> None:
    db.delete_book(book_id)
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)

# This is a test comment to trigger the CI pipeline.
