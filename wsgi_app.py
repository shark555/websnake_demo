#-*- coding: utf-8 -*-
import sys

user_headers = []

def init(environ):
    return content(environ)

def content(environ):
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

    return 'Ala ma kota'

####WSGI MAGIC#####

def wsgi_app(environ, start_response):
    global user_headers
    status = '200 OK'
    #status = '404 Not Found' #404
    #status = '301 Moved Permanently'
    #status = '302 Found'
    #status = '307 Temporary Redirect'
    output = init(environ)
    headers = [ ('Content-type', 'text/html'), ('Content-Length', str(len(output)))] + user_headers
    start_response(status, headers)
    yield output.encode('utf-8')

# mod_wsgi need the *application* variable to serve our small app
application = wsgi_app
