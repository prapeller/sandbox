from framework.main import Framework
from views import routes
from components import settings

if __name__ == '__main__':
    app = Framework(settings, routes)
    app.run()