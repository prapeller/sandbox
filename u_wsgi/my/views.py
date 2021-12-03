from framework.templator import render
from components.models import Engine, MapperRegistry
from datetime import date
from components.decorators import AppRoute
from components.cbv import ListView, CreateView
from components.unit_of_work import UnitOfWork


site = Engine()
routes = {}
UnitOfWork.new_current()
UnitOfWork.get_current().set_mapper_registry(MapperRegistry)


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '<h1>404 page not found</h1>'


@AppRoute(routes=routes, url='/')
class Index:
    def __call__(self, request):
        return '202 OK', render('index.html', categories=site.categories)


@AppRoute(routes=routes, url='/create-category/')
class CreateCategory:
    def __call__(self, request):
        if request['method'] == 'POST' and request.get('data'):
            data = request['data']
            category_name_encoded = data['name']
            category_name = site.decode_value(category_name_encoded)
            category = site.create_category(category_name)
            site.categories.append(category)
            print(f'created category: {category_name}')
            print(site.categories)
            return '202 OK', render('index.html', categories=site.categories)

        return '202 OK', render('create_category.html')


@AppRoute(routes=routes, url='/category-list/')
class CategoryList:
    def __call__(self, request):
        return '202 OK', 'category list body'


@AppRoute(routes=routes, url='/course-list/')
class CourseList:
    def __call__(self, request):
        category_id = int(request['request_params']['id'])
        category = site.get_category_by_id(category_id)
        courses = category.courses
        return '202 OK', render('course_list.html', category=category, courses=courses)


@AppRoute(routes=routes, url='/create-course/')
class CreateCourse:
    category_id = 0

    def __call__(self, request):
        request_params = request.get('request_params', {})
        category_id = int(request_params.get('id', self.category_id))
        category = site.get_category_by_id(category_id)
        self.category_id = category_id
        courses = category.courses if category else []

        if request['method'] == 'POST' and request.get('data'):
            data = request['data']
            course_name = site.decode_value(data['name'])
            course = site.create_course('record', course_name, category)
            site.courses.append(course)
            return '202 OK', render('course_list.html', category=category, courses=courses)

        return '202 OK', render('create_course.html', category=category)


@AppRoute(routes=routes, url='/about/')
class About:
    def __call__(self, request):
        return '202 OK', render('about.html')


@AppRoute(routes=routes, url='/study-programs/')
class StudyPrograms:
    def __call__(self, request):
        return '202 OK', render('study-programs.html', date=date.today())


@AppRoute(routes=routes, url='/student-list/')
class StudentListView(ListView):
    template_name = 'student_list.html'
    objs_name = 'students'
    mapper = MapperRegistry.get_current_mapper('student')
    objs_lst = mapper.all()
    context = {objs_name: objs_lst}


@AppRoute(routes=routes, url='/create-student/')
class StudentCreateView(CreateView):
    template_name = 'create_student.html'
    def create_obj(self, data):
        name = site.decode_value(data['name'])
        new_student = site.create_user('student', name)
        site.students.append(new_student)
        new_student.mark_new()
        UnitOfWork.get_current().commit()


@AppRoute(routes=routes, url='/add-student/')
class AddStudentByCourseCreateView(CreateView):
    template_name = 'add_student.html'
    context = {
        'courses': site.courses,
        'students': site.students
    }

    def create_obj(self, data):
        course_name = site.decode_value(data['course_name'])
        course = site.get_course(course_name)
        student_name = site.decode_value(data['student_name'])
        student = site.get_student(student_name)
        course.add_student(student)
