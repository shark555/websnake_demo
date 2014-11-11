class HttpRequest:
    ## environment - WSGI environment dictionary
    def __init__(self, environment):
        self._environment = environment
   
    ## returns string
    def get_request_body(self):
        return str(self._environment['wsgi.input'].read())

    ## returns string
    def get_query_string(self):
        return self._environment.get('QUERY_STRING')
   
    ## returns string
    def get_request_method(self):
        return self._environment.get('REQUEST_METHOD')
  
    ## returns string
    def get_path_info(self):
        return self._environment.get('PATH_INFO')

    ## returns string
    def get_http_host(self):
        return self._environment.get('HTTP_HOST')

    ## returns string
    def get_document_root(self):
        return self._environment.get('DOCUMENT_ROOT')

    ## returns string
    def get_remote_address(self):
        return self._environment.get('REMOTE_ADDR')

    ## returns string
    def get_cookies_string(self):
        return self._environment.get('HTTP_COOKIE')

    ## returns string
    def get_http_referer(self):
        if 'HTTP_REFERER' in self._environment:
            return self._environment.get('HTTP_REFERER')
        else:
            return ''

