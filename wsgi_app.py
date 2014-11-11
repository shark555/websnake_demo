#-*- coding: utf-8 -*-
import sys

#def init(environ):
#    return content(environ)

#def content(environ):
    #global user_headers 
    #user_headers = [('Country', 'Poland')] #W ten sposób ustawiamy nagłówki użytkownika
    #user_headers = [('Set-Cookie', 'ciastko=suchar')] #W ten sposób ustawiamy ciastko
    #user_headers = [('Location', 'http://google.pl')] #W ten sposób możemy zrobić przekierowanie - działa z odpowiednimi kodami HTTP(301,302,307 itp)

    #return environ.get('QUERY_STRING') ## W ten sposób dostajemy GET'a
    #return environ.get('PATH_INFO') ## a w ten ścieżkę - na podstawie tego można zbudować routing
    #return environ.get('REQUEST_URI') ## a w ten jedno i drugie
    #return environ.get('HTTP_HOST') ##a w ten nazwę hosta
    #return environ.get('REQUEST_METHOD')  ## a w ten metodę - na podstawie tego można zbudować testy isPost(), isGet() itp...
    #return repr(environ['wsgi.input'].read()) ## w ten sposób można dostać surowy request HTTP -- na tej podstawie można sobie zbudować POSTa
    #return environ.get('HTTP_USER_AGENT') ## w ten sposób(HTTP_*) pobieramy nagłówki, np. "User Agent"
    #return environ.get('HTTP_COOKIE') ## Przyklad z Cookie
    #return environ.get('HTTP_REFERER') ## Przyklad z Refererem
    #if 'HTTP_X_REQUESTED_WITH' in environ:
    #    return environ.get('HTTP_X_REQUESTED_WITH') ## Przyklad sprawdzający czy to Ajax
    ##return environ.get('REMOTE_ADDR') ## w ten sposób pobieramy adres klienta
    ##return environ.get('DOCUMENT_ROOT') ## w ten sposób pobieramy Docroot
    ##environ['wsgi.errors'].write('Dupa!!') ##W ten sposób możemy rzucać błędami(zapisują się w logach serwera)
    #return 'Ala ma kota'

####Framework Class

class HttpResponse:
    ## environment - WSGI environment dictionary
    def __init__(self, environment):
        self._environment = environment
        self._response_headers = []
        self._response_code = 200

    ## returns string
    def get_output(self):
        return self.get_request_method()
   
    ###Metody pomocnicze

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

class PreparedHttpResponse(HttpResponse):
    ##Wysokopoziomowe metody(słowniki):
    ## get_url_params()
    ## get_query_fields()
    ## get_form_fields()
    ## get_cookies()
    ## get_cookie(name)
    ## set_cookie(name, value)
    ## redirect(url, code = 301)
    ##
    pass

####WSGI MAGIC#####

class Http:
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
        http_response = PreparedHttpResponse(self._environ)
        output = http_response.get_output()
        user_headers = http_response.get_response_headers()
        user_response_code = http_response.get_response_code()
        if(user_response_code != ''):
            self._response_code = self._http_codes[user_response_code]
        self._start(self._response_code, self._default_headers + user_headers)
        yield output.encode(self._default_encoding)

application = Http

