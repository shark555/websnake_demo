class HttpResponse:
    ## environment - WSGI environment dictionary
    def __init__(self, environment):
        self._environment = environment
        self._response_headers = []
        self._response_code = 200

    ## returns string
    def get_output(self):
        return 'Ala ma kota!!!!!' ##Tu powinien być jakiś dispatch i zwrócenie kodu użytkownika

    ## message - string
    def set_error(self, message):
        self._environment['wsgi.errors'].write(message)

    ## name - string
    ## value - string
    def set_response_header(self, name, value):
        self._response_headers = self._response_headers + [(name, value)]

    ## returns list
    def get_response_headers(self):
        return self._response_headers

    ## code - int
    def set_response_code(self, code):
        self._response_code = code  

    ## returns int 
    def get_response_code(self):
        return self._response_code
