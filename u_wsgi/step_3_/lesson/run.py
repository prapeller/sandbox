from simba_framework.main import Framework
from urls import routes

# Создаем объект WSGI-приложения
app = Framework(routes)
app.run()


