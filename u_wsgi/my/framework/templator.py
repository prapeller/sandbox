from jinja2 import FileSystemLoader, Environment
from components.settings import STATIC_URL

def render(template_name, folder='templates', **kwargs):
    env = Environment()
    env.loader = FileSystemLoader(folder)
    env.globals['static_url'] = STATIC_URL
    template = env.get_template(template_name)
    return template.render(**kwargs)


#/static/new_app/my_image.jpg

#{% load staticfiles %}
#src = "{% static "new_app/my_image.jpg" %}"