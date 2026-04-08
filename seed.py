from faker import Faker
import random

from database import SessionLocal
from models import Student, Group, Teacher, Subject, Grade

fake = Faker()
session = SessionLocal()

groups = [Group(name=f"Group-{i}") for i in range(1, 4)]
session.add_all(groups)

teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)

subjects = [
    Subject(name=fake.word(), teacher=random.choice(teachers))
    for _ in range(7)
]
session.add_all(subjects)

students = [
    Student(name=fake.name(), group=random.choice(groups))
    for _ in range(40)
]
session.add_all(students)

session.commit()

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
