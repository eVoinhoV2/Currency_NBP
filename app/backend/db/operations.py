
from sqlalchemy import select
from app.backend.db.session import SessionLocal


class Operations:
    def __init__(self, objType, session_factory=SessionLocal):
        self.objType = objType
        self.session_factory = session_factory

    def create(self, obj):
        with self.session_factory() as session:
            with session.begin():
                session.add(obj)
                session.flush()
                session.refresh(obj)
            return obj

    def delete(self, _id) -> bool:
        with self.session_factory() as session:
            with session.begin():
                db_obj = session.get(self.objType, _id)
                if db_obj is None:
                    return False

                session.delete(db_obj)
            return True

    def update(self, data: dict, _id: int):
        if not data:
            raise ValueError("No fields provided for update")

        with self.session_factory() as session:
            with session.begin():
                db_obj = session.get(self.objType, _id)
                if db_obj is None:
                    return None

                allowed_fields = {
                    column.key
                    for column in self.objType.__table__.columns
                    if not column.primary_key
                }

                for key, value in data.items():
                    if key not in allowed_fields:
                        raise ValueError(f"Invalid field: {key}")
                    setattr(db_obj, key, value)

                session.flush()
                session.refresh(db_obj)
            return db_obj

    def get_all(self):
        with self.session_factory() as session:
            stmt = select(self.objType)
            return session.scalars(stmt).all()

    def get_by_query(self, query: dict):
        with self.session_factory() as session:
            stmt = select(self.objType).filter_by(**query)
            return session.scalars(stmt).all()

    def get(self, _id):
        with self.session_factory() as session:
            return session.get(self.objType, _id)
