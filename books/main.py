"""Main module for the web app"""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from books.books_db import load_books_as_dicts
from books.resources.resource import static_path, get_html
from books.routes.api_routes import api_router
from books.routes.ui_routes import ui_router

app = FastAPI(title='Fake book DB', openapi_url='/openapi.json')
app.mount('/ui/assets', StaticFiles(directory=f'{static_path()}/assets'))
app.mount('/design/assets', StaticFiles(directory=f'{static_path()}/assets'))
app.mount('/assets', StaticFiles(directory=f'{static_path()}/assets'))


app.include_router(api_router)
app.include_router(ui_router)


tags_metadata = [
    {
        "name": "API",
        "description": "JSON API endpoints for application clients",
    },
    {
        "name": "UI",
        "description": "Endpoints for supporting the GUI",
        "externalDocs": {
            "description": "htmx external docs",
            "url": "https://htmx.org/",
        },
    },
]


@app.on_event("startup")
async def startup_event():
    print('Initializing...')
    load_books_as_dicts()
    print('Ready.')


@app.get('/', status_code=200, response_class=HTMLResponse)
async def root():
    return get_html('index')


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")

