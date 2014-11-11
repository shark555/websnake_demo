#-*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, '/srv/http/Prywatne/modwsgi/library/websnake') ##potrzebne by móc ładować lokalne moduły
os.environ["PYTHONDONTWRITEBYTECODE"] = "1" ##wyłączenie bytecode'u - przydatne na devie
from wsgi_connector import WsgiConnector

application = WsgiConnector
