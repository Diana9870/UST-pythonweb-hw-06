import argparse
from database import SessionLocal
from models import Student, Teacher, Group, Subject

MODELS = {
    "Student": Student,
    "Teacher": Teacher,
    "Group": Group,
    "Subject": Subject
}


def create(session, model, name):
    obj = model(name=name)
    session.add(obj)
    session.commit()


def list_all(session, model):
    results = session.query(model).all()
    for r in results:
        print(r.id, r.name)


def update(session, model, obj_id, name):
    obj = session.query(model).filter_by(id=obj_id).first()
    if obj:
        obj.name = name
        session.commit()


def remove(session, model, obj_id):
    obj = session.query(model).filter_by(id=obj_id).first()
    if obj:
        session.delete(obj)
        session.commit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", required=True)
    parser.add_argument("-m", "--model", required=True)
    parser.add_argument("--id", type=int)
    parser.add_argument("-n", "--name")

    args = parser.parse_args()

    model = MODELS.get(args.model)

    with SessionLocal() as session:
        if args.action == "create":
            create(session, model, args.name)
        elif args.action == "list":
            list_all(session, model)
        elif args.action == "update":
            update(session, model, args.id, args.name)
        elif args.action == "remove":
            remove(session, model, args.id)


if __name__ == "__main__":
    main()
