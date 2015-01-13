from jinja2 import Template
import os
from exceptions.no_view_exception import NoViewException


#TODO: Seperate from Jinja
class View:
    def __init__(self, controller):
        self._controller = controller

    def render(self, view_name, **variables):
        view_path = self._find_view_file_path(view_name)
        view_source = self._read_view_file(view_path)
        template = Template(view_source)
        return template.render(**variables)

    def _read_view_file(self, view_path):
        view_content = ''
        with open(view_path) as f:
            for line in f:
                view_content += line
        return view_content

    #TODO: Application path should be handled globally
    def _find_view_file_path(self, view_name):
        application_path = os.getcwd()
        controller_name = self._controller.__class__.__name__
        normalized_controller_name = controller_name.replace('Controller', '').lower()
        view_path = application_path + '/../views/'+normalized_controller_name+'/'+view_name+'.phtml'
        if not os.path.isfile(view_path):
            raise NoViewException
        return view_path
