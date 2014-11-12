class HttpResponse:
    def __init__(self, environment: str):
        self._environment = environment
        self._response_headers = []
        self._response_code = 200

    def set_output(self, output: str):
        pass

    def get_output(self) -> str:
        return 'Hello Web Snake!'

    def set_error(self, message: str):
        self._environment['wsgi.errors'].write(message)

    def set_response_header(self, name: str, value: str):
        self._response_headers = self._response_headers + [(name, value)]

    def get_response_headers(self) -> str:
        return self._response_headers

    def set_response_code(self, code: int):
        self._response_code = code

    def get_response_code(self) -> int:
        return self._response_code
