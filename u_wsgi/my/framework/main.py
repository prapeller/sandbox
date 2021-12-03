import os
import quopri
from wsgiref.simple_server import make_server
from request_handler import GetRequests, PostRequests
from views import PageNotFound404
from components.content_types import CONTENT_TYPES_MAP


class Framework:
    def run(self, host='127.0.0.1', port=8080):
        with make_server(host=host, port=port, app=self) as httpd:
            print(f'http://{host}:{port}')
            httpd.serve_forever()

    def __init__(self, settings, routes):
        self.settings = settings
        self.routes = routes

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        path = f'{path}/' if not path.endswith('/') else path

        method = environ['REQUEST_METHOD']
        request = {'method': method}

        if method == 'GET':
            request_params = GetRequests.get_get_request_params(environ)
            request['request_params'] = request_params
            print(f'server received from user get request params {request_params}')

        elif method == 'POST':
            data_params = PostRequests.get_post_request_params(environ)
            request['data'] = data_params
            decoded_data_params = Framework.decode_params(data_params)
            print(f'server received from user data {decoded_data_params}')

        if path in self.routes:
            view = self.routes[path]
            content_type = self.get_content_type(path)
            code, body = view(request)
            body = body.encode('utf-8')

        elif path.startswith(self.settings.STATIC_URL):
            file_path = path[len(self.settings.STATIC_URL):-1] # /static/images/logo.jpg/ - > images/logo.jpg
            print(f'file path: {file_path}')
            content_type = self.get_content_type(file_path)
            print(f'content type: {content_type}')
            code, body = self.get_code_body_of_static(self.settings.STATIC_FILES_DIR, file_path) # get_static('static_files', 'images/logo.jpg')

        else:
            view = PageNotFound404()
            content_type = self.get_content_type(path)
            code, body = view(request)
            body = body.encode('utf-8')

        start_response(code, [('Content-Type', content_type)])

        # view = self.routes[path] if path in self.routes else PageNotFound404()
        # code, body = view(request)
        # start_response(code, [('Content-Type', 'text/html')])
        # return [body.encode('utf-8')]

        return [body]



    @classmethod
    def decode_params(cls, params):
        return {k: quopri.decodestring(bytes(v.replace('%', '=').replace('+', ' '), 'utf-8')).decode('utf-8')
                for k, v in params.items()}

    @staticmethod
    def get_content_type(path, content_types_map=CONTENT_TYPES_MAP):
        file_name = os.path.basename(path).lower() # styles.css
        extension = os.path.splitext(file_name)[1] #.css
        print(extension)
        return content_types_map.get(extension, 'text/html')


    @staticmethod
    def get_code_body_of_static(static_dir, file_path):
        path = os.path.join(static_dir, file_path)
        with open(path, 'rb') as f:
            body = f.read()
        code = '200 OK'
        return code, body
