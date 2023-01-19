from typing import Callable

from flask import redirect, render_template, request

# init_views inicializa la clase de las vistas
# app es un objeto flask creado en app.py (en app.py: app = Flask(__name__)
# db_access es el objeto que devuelve init_db para gestionar la base de datos (en app.py: db_access = init_db(app))
# ambos pasan como parámetros a init_views

def init_views(app, db_access: dict[str, Callable]): 
    # definición de las acciones a realizar para lanzar cada vista
    # nótese que el código de "/" no pregunta si se ha hecho una petición, así que deberá ejecutarse al inicializar
    # en el caso de los demás tienen sentencias IF para que el código se ejecute solo si haya una petición
    @app.route("/", methods=["GET", "POST"])
    def index():
    	# invoca a la clase contact que está implementada en models.py con el método "list"
    	# y luego lanza la vista "index.html"
        list_contacts = db_access["list"] 
        contacts = list_contacts() # para mostrar al inicio los contactos que ya están en la BD
        return render_template("index.html", contacts=contacts)

    @app.route("/create", methods=["GET", "POST"])
    def create():
        if request.method == "GET":
            return render_template("create.html")

        if request.method == "POST":
            create_contact = db_access["create"]
            create_contact(
                nick=request.form["nick"],
                first_name=request.form["first_name"],
                last_name=request.form["last_name"],
                phone=int(request.form["phone"]),
            )
            return redirect("/")

    @app.route("/update/<int:uid>", methods=["GET", "POST"])
    def update(uid: int):
        if request.method == "GET":
            read_contact = db_access["read"]
            contact = read_contact(uid)
            return render_template("update.html", contact=contact)

        if request.method == "POST":
            update_contact = db_access["update"]
            update_contact(
                uid=uid,
                nick=request.form["nick"],
                first_name=request.form["first_name"],
                last_name=request.form["last_name"],
                phone=int(request.form["phone"]),
            )
            return redirect("/")

    @app.route("/delete/<int:uid>", methods=["GET", "POST"])
    def delete(uid: int):
        if request.method == "GET":
            read_contact = db_access["read"]
            contact = read_contact(uid)
            return render_template("delete.html", contact=contact)

        if request.method == "POST":
            delete_contact = db_access["delete"]
            delete_contact(
                uid=uid,
            )
            return redirect("/")