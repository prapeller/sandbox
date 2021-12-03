from framework.templator import render


class TemplateView:
    template_name = 'dummy_template.html'
    context = {}
    # objs_lst_name = 'dummy_objects_lst_name'
    # objs_lst = []

    def get_context_data(self):
        return self.context

    def get_template_name(self):
        return self.template_name

    def render_template(self):
        template_name = self.get_template_name()
        context = self.get_context_data()
        return '200 OK', render(template_name, **context)

    def __call__(self, request):
        return self.render_template()


class ListView(TemplateView):

    # def get_objs_lst(self):
    #     return self.objs_lst
    #
    # def get_objs_lst_name(self):
    #     return self.objs_lst_name
    pass


class CreateView(TemplateView):
    template_name = 'dummy_create.html'

    @staticmethod
    def get_request_data(request):
        return request['data']

    def create_obj(self, data):
        pass

    def __call__(self, request):
        if request['method'] == 'POST':
            data = self.get_request_data(request)
            self.create_obj(data)
            return self.render_template()

        return super().__call__(request)
