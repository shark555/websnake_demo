import re


class HttpRequestParser:
    def parse_query_string(self, query_string: str) -> dict:
        fields = query_string.split('&')
        split_fields = (field_text.split('=') for field_text in fields)
        prepared_fields = {field[0]: (field[1] if len(field) == 2 else '') for field in split_fields}
        if '' in prepared_fields:
            prepared_fields = {}
        return prepared_fields

    def parse_path_as_dictionary(self, path_info: str, start: int=0) -> dict:
        names = path_info.split('/')
        non_empty_names = []
        for name in names:
            if name:
                non_empty_names.append(name)
        result = {}
        for key, name in enumerate(non_empty_names):
            if key >= start:
                if key == len(non_empty_names) - 1:
                    value = ""
                else:
                    value = non_empty_names[key + 1]
                if key % 2 == 0:
                    result[name] = value

        return result

    def parse_path_as_list(self, path_info: str) -> list:
        names = path_info.split('/')
        non_empty_names = []
        for name in names:
            if name:
                non_empty_names.append(name)
        return non_empty_names

    #TODO: Obsłużyć również "application/x-www-form-urlencoded" oraz plik w multiparcie
    #Content-Type:multipart/form-data; boundary=----WebKitFormBoundarygpMMpBxkBA0wUCzx
    #Content-Type:application/x-www-form-urlencoded
    def parse_request_body(self, request_body: str) -> dict:
        request_body_lines = request_body.split('\\r\\n')
        request_body_data = request_body_lines[1:len(request_body_lines)-2]
        request_body_separated_data = {}
        for key, field in enumerate(request_body_data):
            if key % 4 == 0:
                request_body_separated_data[field] = request_body_data[key+2]
        result = {}
        for key, field in request_body_separated_data.items():
            label_expression_result = re.search('name="(.*)"', key)
            label = label_expression_result.group(1)
            result[label] = field
        return result
