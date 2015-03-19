class HttpRequest:
    def __init__(self, environment: dict):
        self._environment = environment
   
    def get_request_body(self) -> str:
        return str(self._environment['wsgi.input'].read())

    def get_query_string(self) -> str:
        return self._environment.get('QUERY_STRING')
   
    def get_request_method(self) -> str:
        return self._environment.get('REQUEST_METHOD')
  
    def get_path_info(self) -> str:
        return self._environment.get('PATH_INFO')

    def get_http_host(self) -> str:
        return self._environment.get('HTTP_HOST')

    def get_document_root(self) -> str:
        return self._environment.get('DOCUMENT_ROOT')

    def get_remote_address(self) -> str:
        return self._environment.get('REMOTE_ADDR')

    def get_cookies_string(self) -> str:
        cookie_string = self._environment.get('HTTP_COOKIE')
        if cookie_string is not None:
            return cookie_string
        else:
            return ''

    def get_http_referer(self) -> str:
        if 'HTTP_REFERER' in self._environment:
            return self._environment.get('HTTP_REFERER')
        else:
            return ''

    def get_environment(self) -> dict:
        return self._environment

