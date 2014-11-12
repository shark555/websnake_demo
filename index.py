import sys
sys.path.insert(0, '/srv/http/Prywatne/modwsgi/library/websnake') ##potrzebne by móc ładować lokalne moduły
sys.dont_write_bytecode = True  # wyłączenie bytecode'u - być może przydatne na devie
from wsgi_connector import WsgiConnector

application = WsgiConnector
