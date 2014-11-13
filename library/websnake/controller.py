from http_response import HttpResponse
from http_request import HttpRequest
from http_request_parser import HttpRequestParser
from abc import ABCMeta


class Controller:
    __metaclass__ = ABCMeta
    PARAM_START = 2

    def __init__(self, http_request: HttpRequest, http_response: HttpResponse, http_request_parser: HttpRequestParser):
        self._http_request = http_request
        self._http_response = http_response
        self.__http_request_parser = http_request_parser

    def get_method_object(self, name):
        return self.__class__.__dict__[name]

    def get_http_response(self) -> HttpResponse:
        return self._http_response

    def get_query_fields(self):
        return self.__http_request_parser.parse_query_string(self._http_request.get_query_string())

    def get_url_params(self):
        return self.__http_request_parser.parse_path(self._http_request.get_path_info(), self.PARAM_START)
