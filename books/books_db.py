import csv
from pathlib import Path
from typing import List, Dict, Union, Sequence

from pydantic import BaseModel

from books.exceptions import NotFoundException

BOOKS = tuple()


class Book(BaseModel):
    Title: str
    Author: str
    Genre: str
    Height: str
    Publisher: str


def read_csv_as_dicts(file_path: Path, materialize=True, csv_model=None) -> List[Union[Dict[str, str], BaseModel]]:
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
    if csv_model:
        book_data = (csv_model(**dict(zip(rows[0], row))) for row in rows[1:])
    else:
        book_data = (dict(zip(rows[0], row)) for row in rows[1:])
    return list(book_data) if materialize else book_data


def load_books_as_dicts() -> Sequence[Dict[str, str]]:
    global BOOKS
    if BOOKS:
        return BOOKS
    csv_data = Path(__file__, '..', '..', 'books.csv').resolve()
    BOOKS = read_csv_as_dicts(csv_data, materialize=True, csv_model=Book)
    return BOOKS


if __name__ == '__main__':
    data = load_books_as_dicts()


def get_by_title(title: str) -> Book:
    result = [book for book in BOOKS if book.Title.lower() == title.lower()]
    if not result:
        raise NotFoundException
    return result[0]


def find_by_title(title: str) -> List[Book]:
    return [book for book in BOOKS if title.lower() in book.Title.lower()]
