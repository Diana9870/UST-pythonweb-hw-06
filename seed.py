from faker import Faker
import random
from database import SessionLocal
from models import Group, Teacher, Student, Subject, Grade

fake = Faker()


def seed():
    with SessionLocal() as session:
        groups = [Group(name=f"Group {i}") for i in range(1, 4)]
        session.add_all(groups)

        teachers = [Teacher(name=fake.name()) for _ in range(5)]
        session.add_all(teachers)

        subjects = []
        for _ in range(7):
            subject = Subject(name=fake.word(), teacher=random.choice(teachers))
            subjects.append(subject)
        session.add_all(subjects)

        students = []
        for _ in range(40):
            student = Student(name=fake.name(), group=random.choice(groups))
            students.append(student)
        session.add_all(students)

        for student in students:
            for _ in range(random.randint(10, 20)):
                grade = Grade(
                    student=student,
                    subject=random.choice(subjects),
                    grade=random.randint(60, 100)
                )
                session.add(grade)

        session.commit()


if __name__ == "__main__":
    seed()