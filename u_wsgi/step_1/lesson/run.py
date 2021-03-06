from wsgiref.simple_server import make_server
from simba_framework.main import Framework
from urls import routes

# Создаем объект WSGI-приложения
application = Framework(routes)

with make_server('', 8080, application) as server:
    print("Запуск на порту 8080...")
    server.serve_forever()
