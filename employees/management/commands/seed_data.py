from django.core.management.base import BaseCommand
from employees.models import Employee, Department
from attendance.models import Attendance, Performance
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with fake employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        departments = ['HR', 'Engineering', 'Marketing', 'Finance']
        dept_objs = []

        for dept in departments:
            obj, _ = Department.objects.get_or_create(name=dept)
            dept_objs.append(obj)

        for _ in range(50):
            emp = Employee.objects.create(name=fake.name(),email=fake.unique.email(),phone=fake.phone_number(),address=fake.address(),doj=fake.date_between(start_date='-3y', end_date='today'),dept=random.choice(dept_objs))

            for _ in range(5):
                Attendance.objects.create(employee=emp,date=fake.date_this_year(),status=random.choice(['Present', 'Absent', 'Late']))
                Performance.objects.create(employee=emp,rating=random.randint(1, 5),review_date=fake.date_this_year())

        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))
