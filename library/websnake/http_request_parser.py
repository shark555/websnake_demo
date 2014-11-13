class HttpRequestParser:
    def parse_query_string(self, query_string: str) -> dict:
        fields = query_string.split('&')
        split_fields = (field_text.split('=') for field_text in fields)
        prepared_fields = {field[0]: (field[1] if len(field) == 2 else '') for field in split_fields}
        if '' in prepared_fields:
            prepared_fields = {}
        return prepared_fields

    def parse_path(self, path_info: str, start: int=0) -> dict:
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