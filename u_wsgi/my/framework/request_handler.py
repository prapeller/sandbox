import quopri


class Parser:
    @staticmethod
    def parse_input_string(query_string) -> dict:
        return {k: v for k, v in (params.split('=') for params in query_string.split('&'))} if query_string else {}
        # result_dict = {}
        # if query_string:
        #     params = query_string.split('&')
        #     for k, v in params.split('='):
        #         result_dict[k] = v
        # return result_dict

    @staticmethod
    def parse_wsgi_input_data(data) -> dict:
        data_str = data.decode('utf-8')
        return Parser.parse_input_string(data_str)


class GetRequests(Parser):
    @staticmethod
    def get_get_request_params(environ) -> dict:
        query_string = environ['QUERY_STRING']
        return GetRequests.parse_input_string(query_string)


class PostRequests(Parser):
    @staticmethod
    def get_post_request_params(environ) -> dict:
        data = PostRequests.get_wsgi_input_data(environ)
        return PostRequests.parse_wsgi_input_data(data)

    @staticmethod
    def get_wsgi_input_data(environ) -> bytes:
        wsgi_input_data = environ['wsgi.input']
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        return wsgi_input_data.read(content_length) if content_length else b''
