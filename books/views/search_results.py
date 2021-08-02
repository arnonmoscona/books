from typing import List

from jinja2 import Environment, PackageLoader, select_autoescape

from books.books_db import Book

env = Environment(
    loader=PackageLoader("views"),
    autoescape=select_autoescape()
)


# htmx docs: https://htmx.org/
# Jinja2 docs: https://jinja.palletsprojects.com/en/3.0.x/templates/#
# Bootstrap docs: https://getbootstrap.com/docs/4.0/getting-started/introduction/
#            or: https://getbootstrap.com/docs/5.0/getting-started/introduction/
# Bootstap studio: https://bootstrapstudio.io/


def render_search_results(results: List[Book]) -> str:
    template = env.get_template('_results.html')
    rendered = template.render(results=results)
    return rendered


def render_book_detail(book: Book) -> str:
    return env.get_template('_book_detail.html').render(book=book)
