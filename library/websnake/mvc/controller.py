from mvc.view import View
from http_response import HttpResponse
from http_request import HttpRequest
from http_request_parser import HttpRequestParser


class Controller:
    _PARAM_START = 2

    def __init__(self, http_request: HttpRequest, http_response: HttpResponse, http_request_parser: HttpRequestParser):
        self.__http_request_parser = http_request_parser
        self._http_request = http_request
        self._http_response = http_response
        self._view = View(self)

    def get_http_response(self) -> HttpResponse:
        return self._http_response

    def _get_query_fields(self):
        return self.__http_request_parser.parse_query_string(self._http_request.get_query_string())

    def _get_url_params(self):
        return self.__http_request_parser.parse_path_as_dictionary(self._http_request.get_path_info(),
                                                                   self._PARAM_START)

    def _get_post_fields(self):
        return self.__http_request_parser.parse_request_body(self._http_request.get_request_body())

    def _render(self, view_name, **variables):
        rendered_view = self._view.render(view_name, **variables)
        self._http_response.set_output(rendered_view)

