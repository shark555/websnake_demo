from http_request import HttpRequest
from http_request_parser import HttpRequestParser
from http_response import HttpResponse
from http_codes import HttpCodes
from mvc.router import Router
from mvc.controller_factory import ControllerFactory
from mvc.action_factory import ActionFactory
from exceptions.routing_exception import RoutingException
from exceptions.no_action_exception import NoActionException
from exceptions.no_controller_exception import NoControllerException
from exceptions.no_view_exception import NoViewException


class WsgiConnector:
    def __init__(self, environment, start_response):
        self._environment = environment
        self._start = start_response
        self._http_codes = HttpCodes.get_http_codes()
        self._response_code = self._http_codes[200]
        self._default_headers = [('Content-type', 'text/html')]
        self._default_encoding = 'utf-8'

    def __iter__(self):
        http_response = HttpResponse(self._environment)
        http_request = HttpRequest(self._environment)
        http_request_parser = HttpRequestParser()
        controller_name, action_name = self._get_controller_and_action_name(http_request, http_request_parser)
        controller, action = self._create_controller_and_action(controller_name, action_name, http_request,
                                                                http_response, http_request_parser)
        if action is not None and controller is not None:
            http_response = self._execute_action(action, controller)
        else:
            http_response.set_output("404 Error")
            http_response.set_response_code(404)

        response_code = http_response.get_response_code()
        if response_code != '':
            self._response_code = self._http_codes[response_code]
        self._start(self._response_code, self._default_headers + http_response.get_response_headers())
        yield http_response.get_output().encode(self._default_encoding)

    def _get_controller_and_action_name(self, http_request: HttpRequest, http_request_parser: HttpRequestParser):
        router = Router(http_request, http_request_parser)
        try:
            router.find_route()
        except RoutingException:
            return ["", ""]
        controller_name = router.get_controller()
        action_name = router.get_action()
        return controller_name, action_name

    def _create_controller_and_action(self, controller_name: str, action_name: str, http_request: HttpRequest,
                                      http_response: HttpResponse, http_request_parser: HttpRequestParser):
        try:
            controller = ControllerFactory.create(controller_name, http_request, http_response, http_request_parser)
            action = ActionFactory.create(action_name, controller)
        except (NoControllerException, NoActionException) as e:
            controller = None
            action = None
        return [controller, action]

    def _execute_action(self, action, controller) -> HttpResponse:
        try:
            action(controller)
            http_response = controller.get_http_response()
        except (NoViewException) as e:
            http_response = controller.get_http_response()
            http_response.set_output("500 Error")
            http_response.set_response_code(500)
        return http_response


