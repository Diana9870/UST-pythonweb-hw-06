import argparse
from db import SessionLocal
from models import Teacher, Group, Student, Subject

session = SessionLocal()


def create(model, name):
    obj = model(name=name)
    session.add(obj)
    session.commit()
    print("Created:", obj)


def list_all(model):
    for obj in session.query(model).all():
        print(obj.id, obj.name)


def update(model, obj_id, name):
    obj = session.get(model, obj_id)
    if obj:
        obj.name = name
        session.commit()
        print("Updated")


def remove(model, obj_id):
    obj = session.get(model, obj_id)
    if obj:
        session.delete(obj)
        session.commit()
        print("Deleted")


models = {
    "Teacher": Teacher,
    "Group": Group,
    "Student": Student,
    "Subject": Subject
}


parser = argparse.ArgumentParser()

parser.add_argument("-a", "--action", required=True)
parser.add_argument("-m", "--model", required=True)
parser.add_argument("--id", type=int)
parser.add_argument("-n", "--name")

args = parser.parse_args()

model = models.get(args.model)

if args.action == "create":
    create(model, args.name)

elif args.action == "list":
    list_all(model)

elif args.action == "update":
    update(model, args.id, args.name)

elif args.action == "remove":
    remove(model, args.id)
