# api/router.py
from fastapi import APIRouter
from api.routes import books, v1_books  # Import both route modules

api_router = APIRouter()

# Existing endpoints (for example, available under /books)
api_router.include_router(books.router, prefix="/books", tags=["books"])

# Include v1_books with prefix "/v1"
# With main.py adding its prefix (e.g., "/api"), the final route becomes /api/v1/{book_id}
api_router.include_router(v1_books.router, prefix="", tags=["books"])
