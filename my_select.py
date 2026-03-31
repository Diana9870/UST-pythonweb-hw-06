from sqlalchemy import func
from db import session
from models import Student, Grade, Subject, Group, Teacher


def select_1():
    return session.query(Student.name, func.avg(Grade.grade).label('avg')) \
        .join(Grade) \
        .group_by(Student.id) \
        .order_by(func.avg(Grade.grade).desc()) \
        .limit(5).all()


def select_2(subject_id):
    return session.query(Student.name, func.avg(Grade.grade)) \
        .join(Grade) \
        .filter(Grade.subject_id == subject_id) \
        .group_by(Student.id) \
        .order_by(func.avg(Grade.grade).desc()) \
        .first()


def select_3(subject_id):
    return session.query(Group.name, func.avg(Grade.grade)) \
        .join(Student, Student.group_id == Group.id) \
        .join(Grade, Grade.student_id == Student.id) \
        .filter(Grade.subject_id == subject_id) \
        .group_by(Group.id).all()


def select_4():
    return session.query(func.avg(Grade.grade)).scalar()


def select_5(teacher_id):
    return session.query(Subject.name) \
        .filter(Subject.teacher_id == teacher_id).all()


def select_6(group_id):
    return session.query(Student.name) \
        .filter(Student.group_id == group_id).all()


def select_7(group_id, subject_id):
    return session.query(Student.name, Grade.grade) \
        .join(Grade) \
        .join(Subject) \
        .filter(Student.group_id == group_id, Subject.id == subject_id).all()


def select_8(teacher_id):
    return session.query(func.avg(Grade.grade)) \
        .join(Grade.subject) \
        .filter(Subject.teacher_id == teacher_id).scalar()


def select_9(student_id):
    return session.query(Subject.name) \
        .join(Grade) \
