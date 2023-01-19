from typing import Callable # para agregar anotaciones a las clases

from flask_sqlalchemy import SQLAlchemy


def init_db(app) -> dict[str, Callable]:
    db = SQLAlchemy(app)

    # esta clase gestionará la tabla, hay que pasarle la clase base de
    # todos los modelos de Flask alchemy que es db.Model
    class Contact(db.Model):
        
        __tablename__ = "contacts" # nombre de la tabla creada en SQLite3
        # esto es para que la tabla no tome el nombre por defecto de la clase
        # en minúsculas

        # declarar campos de la tabla "contacts"
        uid = db.Column("id", db.Integer, primary_key=True)
        nick = db.Column(db.String(16))
        first_name = db.Column(db.String(128))
        last_name = db.Column(db.String(128))
        phone = db.Column(db.Integer())

        # __str__ es un método especial para que al hacer un print del objeto nos devuelva 
        # el id, nombre y apellido 
        def __str__(self): 
            return f"[{self.uid}] {self.first_name} {self.last_name}"

        # utilizar el decorador  property para crear una propiedad (atributo) de la clase
        # al que es posible referirse para directamente obtener los atributos nombre y apellido de una vez 
        @property
        def fullname(self) -> str:
            return f"{self.first_name} {self.last_name}"

    # ------------- métodos que operan sobre el contenido la tabla -----------
    def create_contact(nick: str, first_name: str, last_name: str, phone: int):
        contact = Contact(
            nick=nick, first_name=first_name, last_name=last_name, phone=phone
        )
        print("hola")
        db.session.add(contact)
        db.session.commit()

    def read_contact(uid: int) -> Contact:
        return Contact.query.get(uid)

    def update_contact(
        uid: int, nick: str, first_name: str, last_name: str, phone: int
    ):
        contact = Contact.query.get(uid)
        contact.nick = nick
        contact.first_name = first_name
        contact.last_name = last_name
        contact.phone = phone
        db.session.commit()

    def delete_contact(uid: int):
        contact = Contact.query.get(uid)
        db.session.delete(contact)
        db.session.commit()

    def list_contacts() -> list[Contact]:
        contacts = Contact.query.all()
        return [contact for contact in contacts]

    # create_all es un método de Flask-alchemy que crea la tabla con sus campos
    db.create_all()

    return {
    	# estos alias serán usados para llamar a los métodos de la clase, por ejemplo db_access["create"]
    	# invoca al método create_contact
        "create": create_contact,
        "read": read_contact,
        "update": update_contact,
        "delete": delete_contact,
        "list": list_contacts,
    }


# a = contacts(
#     nick="iderator", first_name="Roberto", last_name="Becerra", phone=657365440
# )

# db.session.add(a)
# db.session.commit()