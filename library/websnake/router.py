from http_request import HttpRequest


class Router:
    def __init__(self, http_request: HttpRequest):
        self._http_request = http_request

    def find_route(self):
        pass

    def get_controller(self) -> str:
        return 'IndexController'

    def get_action(self) -> str:
        return 'index_action'
