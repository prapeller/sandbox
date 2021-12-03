class MiddleWareLifeCycle:
    def __init__(self, get_response):
        print('init')
        self.get_response = get_response

    def __call__(self, request):
        print('before the view\'s response')
        response = self.get_response(request)
        print('after the view\'s response')
        return response


from django.http import HttpResponse

class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, reuqest, exception):
        print('AAAAAAAAAA MAZAFUCKAAAA ALLL DROOOOOOOOOOOOOOPED!!!!')
        print(exception)
        return HttpResponse('<h1>some issue happened, pls come back few minutes later</h1>')