from mvc.controller import Controller
from mailer import Mailer


class IndexController(Controller):
    def index_action(self):
        post_data = self._get_post_fields()
        if 'mail' in post_data:
            self._send_mail(post_data['mail'])
        self._render('index', post_data=post_data)

    def hello_action(self):
        get = self._get_query_fields()
        params = self._get_url_params()
        self._http_response.set_response_header('Cookie', 'ciastko=nowe')
        data = self._http_request.get_environment()['HTTP_USER_AGENT']
        data2 = self._http_request.get_remote_address()
        self._render('hello', get=get, params=params, data=data, data2=data2)

    @staticmethod
    def _send_mail(recipient_address):
        mailer = Mailer()
        mailer.set_subject('Hello!')
        mailer.set_message('Witaj. Ważny mail testowy z aplikacji pythonowej :)')
        mailer.set_recipient_address(recipient_address)
        mailer.send()
