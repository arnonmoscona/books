from http import HTTPStatus
from typing import Dict, List

from fastapi import APIRouter, HTTPException

from books import books_db

api_router = APIRouter(prefix='/api/V1')


# https://fastapi.tiangolo.com/tutorial/path-params/
@api_router.get("/book/{title}", status_code=200)
def get_book_by_title(title: str) -> Dict:
    try:
        book = books_db.get_by_title(title)
        return book.dict()
    except Exception as ex:
        if hasattr(ex, 'http_response_code'):
            raise HTTPException(status_code=ex.http_response_code, detail='Book not found')
        else:
            raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR)


@api_router.get("/books/titles/{title}", status_code=200)
def find_books_by_partial_title(title: str) -> List[Dict]:
    try:
        books = books_db.find_by_title(title)
        return [book.dict() for book in books]
    except Exception as ex:
        if hasattr(ex, 'http_response_code'):
            raise HTTPException(status_code=ex.http_response_code, detail='Error while searching')
        else:
            raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
