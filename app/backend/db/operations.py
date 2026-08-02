import json
from app.backend.db.session import get_session

SessionLocal = get_session()

class Operations:
    def __init__(self, objType):
        self.objType = objType

    def create(self, obj):
        with SessionLocal() as session:
            session.add(obj)
            session.commit()
            session.refresh(obj)
            return obj

    def delete(self, _id) -> bool:
        with SessionLocal() as session:
            db_obj = session.query(self.objType).get(_id)
            if db_obj:
                session.delete(db_obj)
                session.commit()
                return True
            return False

    def update(self, data: dict, id_attribute_name: str, _id: int):
        with SessionLocal() as session:
            result = session.query(self.objType).filter_by(**{id_attribute_name: _id}).update(data)
            session.commit()
            if result > 0:
                return session.query(self.objType).get(_id)
            else:
                return None

    def get_all(self):
        with SessionLocal() as session:
            return session.query(self.objType).all()

    def get_by_query(self, query: dict):
        with SessionLocal() as session:
            return session.query(self.objType).filter_by(**query).all()

    def get(self, _id):
        with SessionLocal() as session:
            return session.query(self.objType).get(_id)

    def jsonToObject(self, json_obj):
        obj_in_data = json.loads(json_obj)
        db_obj = self.objType(**obj_in_data)
        return db_obj