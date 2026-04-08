import argparse

from database import SessionLocal
from models import Student, Teacher, Group, Subject

with SessionLocal() as session:


def create(model, name):
    obj = model(name=name)
    session.add(obj)
    session.commit()
    print(f"Created: {obj}")


def list_all(model):
    objects = session.query(model).all()
    for obj in objects:
        print(obj.id, obj.name)


def update(model, obj_id, name):
    obj = session.query(model).filter_by(id=obj_id).first()
    if obj:
        obj.name = name
        session.commit()
        print("Updated")
    else:
        print("Not found")


def remove(model, obj_id):
    obj = session.query(model).filter_by(id=obj_id).first()
    if obj:
        session.delete(obj)
        session.commit()
        print("Deleted")
    else:
        print("Not found")


MODELS = {
    "Student": Student,
    "Teacher": Teacher,
    "Group": Group,
    "Subject": Subject,
}


def main():
    parser = argparse.ArgumentParser(description="CLI for DB")

    parser.add_argument("-a", "--action", required=True,
                        choices=["create", "list", "update", "remove"])

    parser.add_argument("-m", "--model", required=True,
                        choices=MODELS.keys())

    parser.add_argument("--id", type=int)
    parser.add_argument("-n", "--name")

    args = parser.parse_args()

    model = MODELS[args.model]

    if args.action == "create":
        create(model, args.name)

    elif args.action == "list":
        list_all(model)

    elif args.action == "update":
        update(model, args.id, args.name)

    elif args.action == "remove":
        remove(model, args.id)


if __name__ == "__main__":
    main()
