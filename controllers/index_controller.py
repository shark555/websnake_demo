from controller import Controller


class IndexController(Controller):
    def index_action(self):
        self._http_response.set_output('Witaj!!!')
        self._http_response.set_response_header('Framework', 'WebSnake')
