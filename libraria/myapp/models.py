from typing import Callable

from flask_sqlalchemy import SQLAlchemy




def init_db(app) -> dict[str, Callable]:
    db = SQLAlchemy(app)
    
    # se declara una clase por cada tabla de la BD
    class Users(db.Model):
        __tablename__ = "users"

        id = db.Column("user_id", db.Integer, primary_key=True, autoincrement=True)
        name = db.Column("name", db.String)
        age = db.Column("age", db.Integer)
        sex = db.Column("sex", db.String)
        interactions = db.relationship("Interactions", backref="users", lazy=True)

    class Items(db.Model):
        __tablename__ = "items"

        id = db.Column("item_id", db.Integer, primary_key=True, autoincrement=True)
        tittle = db.Column("tittle", db.String)
        genres = db.Column("genres", db.String)
        authors = db.Column("authors", db.String)
        interactions = db.relationship("Interactions", backref="items", lazy=True)

        
        

    class Interactions(db.Model):
        __tablename__ = "interactions"

        id = db.Column("interactions_id", db.Integer, primary_key=True, autoincrement=True)
        user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = True)
        item_id = db.Column(db.Integer, db.ForeignKey("items.item_id"), nullable = True)

        

    
    def items_list(page: int = 1) -> list[Items]: 
        
        items_list = Items.query.order_by(Items.tittle).paginate(
            page=page, max_per_page=10 
        )   
        print(f"{items_list=}") 

        return items_list
    
    def users_list(page: int = 1) -> list[Users]: 
        
        users_list = Users.query.order_by(Users.name).paginate(
            page=page, max_per_page=10 
        )   
        print(f"{users_list=}") 

        return users_list
    

    def interactions_list(page: int = 1) -> list[Interactions]: 
        
        interactions_list = Interactions.query.filter_by(user_id = Users.id).filter_by(item_id = Items.id).paginate(
            page=page, max_per_page=10
        )
        
        return interactions_list


    def items_read(id: int) -> Items:
        return Items.query.get(id)
    def users_read(id: int) -> Users:
        return Users.query.get(id)
    def interactions_read(id: int) -> Interactions:
        return Interactions.query.get(id)

    def items_interactions(id: int, page: int = 1):
        return Interactions.query.filter_by(item_id=id).paginate(
            page=page, max_per_page=10
        )
    
    def users_interactions(id: int, page: int = 1):
        return Interactions.query.filter_by(user_id=id).paginate(
            page=page, max_per_page=10
        )
    
        
    

    # esta función void es la que hace el update sobre la base de datos
    def items_update(id: int, tittle: str, genres: str, authors: str):
        items = Items.query.get(id)
        items.tittle = tittle
        items.genres = genres
        items.authors = authors
        db.session.commit()

    def users_update(id: int, name: str, age: int, sex: str):
        users = Users.query.get(id)
        users.name = name
        users.age = age
        users.sex = sex
        db.session.commit()

    def items_delete(id: int):
        items = Items.query.get(id)
        db.session.delete(items)
        db.session.commit()

    def users_delete(id: int):
        users = Users.query.get(id)
        db.session.delete(users)
        db.session.commit()

    def interactions_delete(id: int):
        interactions = Interactions.query.get(id)
        db.session.delete(interactions)
        db.session.commit()

    def create_contact(tittle: str, genres: str, authors: str):
        contact = Items(tittle=tittle, genres=genres, authors=authors)
        
        db.session.add(contact)
        db.session.commit()

    def create_user(name: str, age: int, sex: str):
        user = Users(name=name, age=age, sex=sex)
        
        db.session.add(user)
        db.session.commit()

    def create_interactions(id: int, user_id: int, item_id: int):
        interactions = Interactions(id=id, user_id=user_id, item_id=item_id)
        
        db.session.add(interactions)
        db.session.commit()


    

    db.create_all()

    

    return { # aquí se publican las funciones internas de init_db, para poder llamarlas desde 
             # fuera de init_db
        "create": create_contact,
        "createU": create_user,
        "create_interactions": create_interactions,
        "items_list": items_list,
        "users_list": users_list,
        "interactions_list": interactions_list,
        "items_read": items_read,
        "users_read": users_read,
        "interactions_read": interactions_read,
        "items_interactions": items_interactions,
        "users_interactions": users_interactions,
        "items_update": items_update,
        "users_update": users_update,
        "items_delete": items_delete,
        "users_delete": users_delete,
        "interactions_delete": interactions_delete,
    }
    
