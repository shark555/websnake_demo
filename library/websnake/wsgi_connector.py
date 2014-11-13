from http_request import HttpRequest
from http_request_parser import HttpRequestParser
from http_response import HttpResponse
from router import Router
from controller_factory import ControllerFactory


class WsgiConnector:
    def __init__(self, environment, start_response):
        self._environment = environment
        self._start = start_response
        self._http_codes = {
            200: '200 OK',
            301: '301 Moved Permanently',
            302: '302 Found',
            307: '307 Temporary Redirect',
            404: '404 Not Found',
            500: '500 Internal Server Error'
        }
        self._response_code = self._http_codes[200]
        self._default_headers = [('Content-type', 'text/html')]
        self._default_encoding = 'utf-8'

    def __iter__(self):
        http_response = HttpResponse(self._environment)
        http_request = HttpRequest(self._environment)

        controller_name, action_name = self._get_controller_and_action_name(http_request)

        controller = ControllerFactory.create(controller_name, http_request, http_response, HttpRequestParser())
        action = controller.get_method_object(action_name)
        action(controller)

        http_response = controller.get_http_response()

        user_response_code = http_response.get_response_code()
        if user_response_code != '':
            self._response_code = self._http_codes[user_response_code]
        self._start(self._response_code, self._default_headers + http_response.get_response_headers())
        yield http_response.get_output().encode(self._default_encoding)

    def _get_controller_and_action_name(self, http_request: HttpRequest):
        router = Router(http_request)
        router.find_route()
        controller_name = router.get_controller()
        action_name = router.get_action()
        return controller_name, action_name
