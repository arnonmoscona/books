from pathlib import Path


def get_html(name: str) -> str:
    resource_base_path = Path(__file__).resolve()
    resource_path = Path(resource_base_path.parent, f'{name}.html')
    if resource_path.exists():
        with open(resource_path, 'r') as html:
            return html.read()
    raise FileNotFoundError(str(resource_path))


def static_path() -> str:
    resource_base_path = Path(__file__).resolve()
    location = Path(resource_base_path.parent, '..', '..', 'design').resolve()
    return str(location)
