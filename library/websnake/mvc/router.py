from http_request import HttpRequest
from http_request_parser import HttpRequestParser
from exceptions.routing_exception import RoutingException


class Router:
    def __init__(self, http_request: HttpRequest, http_request_parser: HttpRequestParser):
        self._http_request = http_request
        self._http_request_parser = http_request_parser
        self._controller_name = ""
        self._action_name = ""

    def find_route(self):
        parsed_params = self._http_request_parser.parse_path_as_list(self._http_request.get_path_info())
        if len(parsed_params) < 2:
            raise RoutingException()
        self._controller_name = parsed_params[0] + 'Controller'
        self._action_name = parsed_params[1] + '_action'

    def get_controller(self) -> str:
        return self._controller_name

    def get_action(self) -> str:
        return self._action_name
