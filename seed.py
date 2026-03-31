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
