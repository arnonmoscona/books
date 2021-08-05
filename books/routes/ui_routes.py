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
    """
    Search the book DB
    :param input_search_term: A complete or partial title (case insensitive)
    :return: A book results partial HTML
    """
    results = find_by_title(input_search_term) if len(input_search_term) >= 2 else []
    return render_search_results(results)


@ui_router.get("/book/{title}", status_code=200, response_class=HTMLResponse)
def book_detail(title: str = '') -> str:
    """
    Render book details
    :param title: the exact title of the book
    :return: a book detail partial HTML
    """
    book = get_by_title(title)
    return render_book_detail(book)


@ui_router.get("/show/{tag_id}", status_code=200, response_class=HTMLResponse)
def show(tag_id: str = '') -> str:
    """
    Used to switch tags in the UI
    :param tag_id: the tag ID
    :return: the content identified by the tag ID (partial HTML)
    """
    return render_static_tag_id(tag_id)
