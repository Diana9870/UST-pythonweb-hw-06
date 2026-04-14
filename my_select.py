from sqlalchemy import func, desc
from sqlalchemy.orm import Session

from models import Student, Group, Teacher, Subject, Grade


def select_1(session: Session):
    return (
        session.query(
            Student.id,
            Student.name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .join(Grade, Grade.student_id == Student.id)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )


def select_2(session: Session, subject_id: int):
    return (
        session.query(
            Student.id,
            Student.name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(1)
        .first()
    )


def select_3(session: Session, subject_id: int):
    return (
        session.query(
            Group.id,
            Group.name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id, Group.name)
        .all()
    )


def select_4(session: Session):
    return session.query(func.round(func.avg(Grade.grade), 2)).scalar()


def select_5(session: Session, teacher_id: int):
    return (
        session.query(Subject.id, Subject.name)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )


def select_6(session: Session, group_id: int):
    return (
        session.query(Student.id, Student.name)
        .filter(Student.group_id == group_id)
        .all()
    )


def select_7(session: Session, group_id: int, subject_id: int):
    return (
        session.query(
            Student.name,
            Grade.grade,
            Grade.date_received
        )
        .join(Grade, Grade.student_id == Student.id)
        .filter(
            Student.group_id == group_id,
            Grade.subject_id == subject_id
        )
        .order_by(Student.name)
        .all()
    )


def select_8(session: Session, teacher_id: int):
    return (
        session.query(
            func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )


def select_9(session: Session, student_id: int):
    return (
        session.query(Subject.id, Subject.name)
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )


def select_10(session: Session, student_id: int, teacher_id: int):
    return (
        session.query(Subject.id, Subject.name)
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(
            Grade.student_id == student_id,
            Subject.teacher_id == teacher_id
        )
        .distinct()
        .all()
    )