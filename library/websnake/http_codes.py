class HttpCodes:
    _http_codes = {
        200: '200 OK',
        301: '301 Moved Permanently',
        302: '302 Found',
        307: '307 Temporary Redirect',
        404: '404 Not Found',
        500: '500 Internal Server Error'
    }

    @classmethod
    def get_http_codes(cls):
        return cls._http_codes