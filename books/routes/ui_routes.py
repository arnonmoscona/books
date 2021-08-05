"""Routes for serving htmx UI"""
from typing import Optional

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from books.books_db import find_by_title, get_by_title
from books.resources import resource
from books.views.search_results import render_search_results, render_book_detail, render_static_tag_id

ui_router = APIRouter(prefix='/ui')


@ui_router.get("/books", status_code=200, response_class=HTMLResponse)
def books() -> str:
    return resource.get_html('books')


@ui_router.get("/search", status_code=200, response_class=HTMLResponse)
def search(input_search_term: Optional[str] = '') -> str:
    results = find_by_title(input_search_term) if len(input_search_term) >= 2 else []
    return render_search_results(results)


@ui_router.get("/book/{title}", status_code=200, response_class=HTMLResponse)
def book_detail(title: str = '') -> str:
    book = get_by_title(title)
    return render_book_detail(book)


@ui_router.get("/show/{tag_id}", status_code=200, response_class=HTMLResponse)
def show(tag_id: str = '') -> str:
    return render_static_tag_id(tag_id)
