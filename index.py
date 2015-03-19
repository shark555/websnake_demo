import sys
#TODO: Przerobić loading tak, żeby podpinać tutaj tylko katalog library
sys.path.insert(0, '/srv/http/Prywatne/modwsgi/library/websnake')  # potrzebne by móc ładować lokalne moduły
sys.path.insert(0, '/srv/http/Prywatne/modwsgi/library/mailer')  # potrzebne by móc ładować lokalne moduły
sys.path.insert(0, '/srv/http/Prywatne/modwsgi/controllers')
sys.dont_write_bytecode = True  # wyłączenie bytecode'u - być może przydatne na devie
from wsgi_connector import WsgiConnector

application = WsgiConnector
