from faker import Faker
import random
from db import SessionLocal
from models import Group, Student, Teacher, Subject, Grade

fake = Faker()
session = SessionLocal()

groups = [Group(name=f"Group-{i}") for i in range(1, 4)]
session.add_all(groups)

teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)

session.commit()

subjects = []
for _ in range(7):
    subject = Subject(
        name=fake.word(),
        teacher=random.choice(teachers)
    )
    subjects.append(subject)

session.add_all(subjects)
session.commit()

students = []
for _ in range(40):
    student = Student(
        name=fake.name(),
        group=random.choice(groups)
    )
    students.append(student)

session.add_all(students)
session.commit()

for student in students:
    for subject in subjects:
        for _ in range(random.randint(5, 20)):
            grade = Grade(
                grade=random.randint(60, 100),
                student=student,
                subject=subject
            )
            session.add(grade)

session.commit()
session.close()
