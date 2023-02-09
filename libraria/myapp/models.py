from typing import Callable

from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy import desc


def init_db(app) -> dict[str, Callable]:
    db = SQLAlchemy(app)
    
    # se declara una clase por cada tabla de la BD
    class Users(db.Model):
        __tablename__ = "users"

        id = db.Column("user_id", db.BigInteger, primary_key=True)
        age = db.Column("age", db.Integer)
        sex = db.Column("sex", db.String)
        interactions = db.relationship("Interactions", backref="user", lazy=True)

    class Items(db.Model):
        __tablename__ = "items"

        id = db.Column("item_id", db.BigInteger, primary_key=True)
        tittle = db.Column("tittle", db.String)
        genres = db.Column("genres", db.String)
        authors = db.Column("authors", db.String)
        interactions = db.relationship("Interactions", backref="items", lazy=True)

        def __str__(self): 
            return f"[{self.id}] {self.tittle} {self.genres} {self.authors}"
        

    class Interactions(db.Model):
        __tablename__ = "interactions"

        id = db.Column("interactions_id", db.BigInteger, primary_key=True)
        user_id = db.Column(db.BigInteger, db.ForeignKey("users.user_id"))
        item_id = db.Column(db.BigInteger, db.ForeignKey("items.item_id"))

        def __str__(self): 
            return f"[{self.id}] {self.user_id} {self.item_id}"



    # las funciones que operan sobres los datos, al final se retornan de la función init_db para poder usarlos fuera de ella
    def items_list(page: int = 1) -> list[Items]: # se pasa como parámetro la página, por defecto es página 1
        # Ordenamiento en el motor de base de datos
        items_list = Items.query.order_by(Items.genres).paginate(
            page=page, max_per_page=10 # divide en páginas de 10 elementos y devuelve solamente los 10 (o menos si es la última)
        )  # Ordenamiento Ascendente   # del número de página que se ha pasado como parámetro 
        print(f"{items_list=}") # esto es para debug, no va
        # items_list = Items.query.order_by(desc(Items.genres)).all()   # Ordenamiento Descendente

        # return [sp for sp in items_list]
        return items_list
    


    def items_read(id: str) -> Items:
        return Items.query.get(id)

    def items_interactions(id: str, page: int = 1):
        return Interactions.query.filter_by(item_id=id).paginate(
            page=page, max_per_page=10
        )
    # esta función void es la que hace el update sobre la base de datos
    def items_update(id: int, tittle: str, genres: str, authors: str):
        items = Items.query.get(id)
        items.tittle = tittle
        items.genres = genres
        items.authors = authors
        db.session.commit()

    def items_delete(id: str):
        items = Items.query.get(id)
        db.session.delete(items)
        db.session.commit()

    def interactions_delete(id: int):
        interactions = Interactions.query.get(id)
        db.session.delete(interactions)
        db.session.commit()

    def items_create(tittle: str, genres: str, authors: str):
        item = Items(tittle=tittle, genres=genres, authors=authors)
        
        db.session.add(item)
        db.session.commit()

    db.create_all()

    return { # aquí se publican las funciones internas de init_db, para poder llamarlas desde 
             # fuera de init_db
        "items_create": items_create,
        "items_list": items_list,
        "items_read": items_read,
        "items_interactions": items_interactions,
        "items_update": items_update,
        "items_delete": items_delete,
        "interactions_delete": interactions_delete,
    }
