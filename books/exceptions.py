from http import HTTPStatus


class NotFoundException(Exception):
    http_response_code = HTTPStatus.NOT_FOUND
