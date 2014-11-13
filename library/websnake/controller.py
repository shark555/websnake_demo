from http_response import HttpResponse
from http_request import HttpRequest

###to powinna być klasa abstrakcyjna


class Controller:
    def __init__(self, http_request: HttpRequest, http_response: HttpResponse):
        self._http_request = http_request
        self._http_response = http_response

    def get_method_object(self, name):
        return self.__class__.__dict__[name]

    def get_http_response(self) -> HttpResponse:
        return self._http_response
