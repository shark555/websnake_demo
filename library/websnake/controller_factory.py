from http_response import HttpResponse
from http_request import HttpRequest
from http_request_parser import HttpRequestParser
from controller import Controller
import importlib
import re


class ControllerFactory:
    @staticmethod
    def create(controller_name: str, http_request: HttpRequest, http_response: HttpResponse,
               http_request_parser: HttpRequestParser) -> Controller:
        controller_filename = ControllerFactory._controller_name_to_filename(controller_name)
        globals()[controller_name] = importlib.import_module(controller_filename).IndexController
        controller_class = globals()[controller_name]
        controller = controller_class(http_request, http_response, http_request_parser)
        return controller

    @staticmethod
    def _controller_name_to_filename(controller_name: str) -> str:
        resp = re.search('(.*)Controller', controller_name)
        filename = resp.group(1).lower()
        return filename + '_controller'

