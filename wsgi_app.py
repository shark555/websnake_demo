#-*- coding: utf-8 -*-
import sys

user_headers = []

def init(environ):
    return content(environ)

def content(environ):
    #global user_headers 
    #user_headers = [('Country', 'Poland')] #W ten sposób ustawiamy nagłówki użytkownika
    #user_headers = [('Set-Cookie', 'ciastko=suchar')] #W ten sposób ustawiamy ciastko

    #return environ.get('QUERY_STRING') ## W ten sposób dostajemy GET'a
    #return environ.get('PATH_INFO') ## a w ten ścieżkę - na podstawie tego można zbudować routing
    #return environ.get('REQUEST_URI') ## a w ten jedno i drugie
    #return environ.get('HTTP_HOST') ##a w ten nazwę hosta
    #return environ.get('REQUEST_METHOD')  ## a w ten metodę - na podstawie tego można zbudować testy isPost(), isGet() itp...
    return repr(environ['wsgi.input'].read()) ## w ten sposób można dostać surowy request HTTP -- na tej podstawie można sobie zbudować POSTa
    #return environ.get('HTTP_USER_AGENT') ## w ten sposób(HTTP_*) pobieramy nagłówki, np. "User Agent"
    #return environ.get('HTTP_COOKIE') ## Przyklad z Cookie
    #if 'HTTP_X_REQUESTED_WITH' in environ:
    #    return environ.get('HTTP_X_REQUESTED_WITH') ## Przyklad sprawdzający czy to Ajax
    ##return environ.get('REMOTE_ADDR') ## w ten sposób pobieramy adres klienta
    ##return environ.get('DOCUMENT_ROOT') ## w ten sposób pobieramy Docroot
   
    return 'Ala ma kota'

####WSGI MAGIC#####

def wsgi_app(environ, start_response):
    global user_headers
    status = '200 OK'
    output = init(environ)
    headers = [ ('Content-type', 'text/html'), ('Content-Length', str(len(output)))] + user_headers
    start_response(status, headers)
    yield output.encode('utf-8')

# mod_wsgi need the *application* variable to serve our small app
application = wsgi_app
