from http_response import HttpResponse
from http_request import HttpRequest
from http_request_parser import HttpRequestParser
from controller import Controller
from index_controller import IndexController #  temporary bypass


class ControllerFactory:
    @staticmethod
    def create(controller_name: str, http_request: HttpRequest, http_response: HttpResponse,
               http_request_parser: HttpRequestParser) -> Controller:
        controller_class = globals()[controller_name]
        controller = controller_class(http_request, http_response, http_request_parser)
        return controller