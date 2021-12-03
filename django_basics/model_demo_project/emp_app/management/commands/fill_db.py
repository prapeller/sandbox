from django.core.management import BaseCommand
from django.db import connection
from emp_app.models import Employee


class Command(BaseCommand):
    def handle(self, *args, **options):
        c = connection.cursor()
        c.execute("""
        TRUNCATE emp_app_employee;
        
        BEGIN;
        SELECT setval(pg_get_serial_sequence('"emp_app_employee"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "emp_app_employee";
        COMMIT;
        """)
        for i in range(3):
            Employee.objects.create(first_name=f'first_{i}', last_name=f'last_{i}', salary=10000+i)

# python manage.py dbshell
# udemy_django_db=# \d
#                         List of relations
#  Schema |               Name                |   Type   |  Owner
# --------+-----------------------------------+----------+----------
# ...
#  public | emp_app_employee                  | table    | postgres
#  public | emp_app_employee_id_seq           | sequence | postgres
# (21 rows)

# udemy_django_db=# select * from emp_app_employee;
#  id | first_name | last_name |    email     | salary
# ----+------------+-----------+--------------+--------
#   2 | first2     | last2     | test@mail.ru |  30000
#   3 | first3     | last3     | test@mail.ru |  40000
#   4 | first4     | last4     | test@mail.ru |  50000
#   1 | pavel      | mirosh    | test@mail.ru |  20000
# (4 rows)

# python manage.py shell
# from emp_app.models import Employee
# qs = Employee.objects.all()
# emp = Employees.objects.get(id=1)
# emps = Employee.objects.filter(id__gt=1)
# emps = Employee.objects.filter(id__gte=1)
# emps = Employee.objects.filter(id__lt=1)
# emps = Employee.objects.filter(id__lte=1)
# print(emps.query)
# emps = Employee.objects.filter(first_name__contains='pav')
# emps = Employee.objects.filter(first_name__startswith='pa') | Employee.objects.filter(last_name__startswith='ololo')
# emps = Employee.objects.filter(first_name__startswith='pa') & Employee.objects.filter(last_name__startswith='ololo')
# from django.db.models import Q
# emps = Employee.objects.filter(Q(first_name__startswith='pa') | Q(last_name__startswith='ololo'))
# emps = Employee.objects.filter(Q(first_name__startswith='pa' & last_name__startswith='ololo'))
# emps.values_list('first_name', 'salary')
# emps.only('first_name', 'salary')

# from django.db.models import Avg, Sum, Max, Min, Count
#  avg = Employee.objects.all().aggregate(Avg('salary'))
# >>> avg = Employee.objects.all().aggregate(Sum('salary'))
# >>> val = Employee.objects.all().aggregate(Max('salary'))
# >>> val = Employee.objects.all().aggregate(Min('salary'))
# >>> val = Employee.objects.all().aggregate(Count('salary'))

# python manage.py sqlsequencereset emp_app | psql -U postgres -d DATABASE