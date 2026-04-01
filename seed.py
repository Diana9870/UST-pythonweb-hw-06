<<<<<<< HEAD
from faker import Faker
import random

from database import SessionLocal
from models import Student, Group, Teacher, Subject, Grade

fake = Faker()
session = SessionLocal()

# Групи
groups = [Group(name=f"Group-{i}") for i in range(1, 4)]
session.add_all(groups)

# Викладачі
teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)

# Предмети
subjects = [
    Subject(name=fake.word(), teacher=random.choice(teachers))
    for _ in range(7)
]
session.add_all(subjects)

# Студенти
students = [
    Student(name=fake.name(), group=random.choice(groups))
    for _ in range(40)
]
session.add_all(students)

session.commit()

# Оцінки
for student in students:
    for subject in subjects:
        for _ in range(random.randint(5, 10)):
            grade = Grade(
                student=student,
                subject=subject,
                grade=random.randint(60, 100),
            )
            session.add(grade)

session.commit()
session.close()
=======
from faker import Faker
import random
from db import session
from models import Group, Student, Teacher, Subject, Grade

fake = Faker()

groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)

teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)

session.commit()

subjects = []
for _ in range(7):
    subject = Subject(
        name=fake.word(),
        teacher_id=random.choice(teachers).id
    )
    subjects.append(subject)

session.add_all(subjects)
session.commit()

students = []
for _ in range(40):
    student = Student(
        name=fake.name(),
        group_id=random.choice(groups).id
    )
    students.append(student)

session.add_all(students)
session.commit()

for student in students:
    for subject in subjects:
        for _ in range(random.randint(5, 20)):
            grade = Grade(
                student_id=student.id,
                subject_id=subject.id,
                grade=random.randint(60, 100),
                date_received=fake.date_time_this_year()
            )
            session.add(grade)

session.commit()
>>>>>>> 29c00f345e2b584ca4c8ef0f68fe35b6a658dd1f
