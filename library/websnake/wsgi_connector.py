from http_request import HttpRequest
from http_response import HttpResponse


class WsgiConnector:
    def __init__(self, environ, start_response):
        self._environ = environ
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
        http_response = HttpResponse(self._environ)
        http_request = HttpRequest(self._environ)
       
        #Tutaj wchodzi dispatcher budowany z http_request 
        #dispatcher = Dispatcher(http_request)
        #dispatcher.dispatch()
        #controller = dispatcher.get_controller()
        #action = dispatcher.get_action()
        #
        #controller.init(http_request, http_response) ##przydałby się też dostęp do sesji
        #controller.action()
        #http_response = controller.get_http_response()

        output = http_response.get_output()
        user_headers = http_response.get_response_headers()
        user_response_code = http_response.get_response_code()
        if user_response_code != '':
            self._response_code = self._http_codes[user_response_code]
        self._start(self._response_code, self._default_headers + user_headers)
        yield output.encode(self._default_encoding)


