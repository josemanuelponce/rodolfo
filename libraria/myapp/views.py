from math import floor, ceil
from typing import Callable

from flask import redirect, render_template, request


def init_views(app, db_access: dict[str, Callable]):
    @app.route("/", methods=["GET", "POST"])
    def index(): 
        
        

        return render_template( 

            "index.html"
        )
    
    @app.route("/indexL", methods=["GET", "POST"])
    def indexL(): 
        
        page = int(request.args.get("page", 1))
        

        items_list = db_access["items_list"] 

        items = items_list(page=page)        

        total_pages = ceil (items.total / 10)

        return render_template( 

            "indexL.html", items=items, pages=[i + 1 for i in range(total_pages)] 
        )
    
    @app.route("/indexU", methods=["GET", "POST"])
    def indexU(): 
        
        page = int(request.args.get("page", 1))
        

        users_list = db_access["users_list"]

        users = users_list(page=page)        

        total_pages = ceil (users.total / 10)

        return render_template( 

            "indexU.html", users=users, pages=[i + 1 for i in range(total_pages)] 
        )
    
    @app.route("/indexI", methods=["GET", "POST"])
    def indexI(): 
        
        page = int(request.args.get("page", 1))
        

        interactions_list = db_access["interactions_list"]

        interactions = interactions_list(page=page)        

        total_pages = ceil (interactions.total / 10)

        return render_template( 

            "indexI.html", interactions=interactions, pages=[i + 1 for i in range(total_pages)] 
        )
    
    
    @app.route("/create", methods=["GET", "POST"])
    def create():
        
        if request.method == "GET":
            return render_template("create.html")

        if request.method == "POST":
            create_contact = db_access["create"]
            create_contact(
                 tittle=request.form["tittle"],
                 genres=request.form["genres"],
                 authors=request.form["authors"],
             )
            return redirect("/")
        
    #Usuario
    @app.route("/createU", methods=["GET", "POST"])
    def createU():
        
        if request.method == "GET":
            return render_template("createU.html")

        if request.method == "POST":
            create_user = db_access["createU"]
            create_user(
                 name=request.form["name"],
                 age=int(request.form["age"]),
                 sex=request.form["sex"],
             )
            return redirect("/indexU")
        

    @app.route("/createI", methods=["GET", "POST"])
    def create_interactions():
        
        if request.method == "GET":
            return render_template("createI.html")

        if request.method == "POST":
            create_interactions = db_access["create_interactions"]
            create_interactions(
                 id=request.form["id"],
                 user_id=request.form["user_id"],
                 item_id=request.form["item_id"],
             )
            return redirect("/")
    



    @app.route("/items/<id>", methods=["GET", "POST"])
    def list_items_interactions(id: int):
        page = int(request.args.get("page", 1))

        items_interactions = db_access["items_interactions"]
        interactions = items_interactions(id, page)
        total_pages = ceil(interactions.total / 10)

        items_read = db_access["items_read"]
        items = items_read(id)

        if request.method == "POST": # el request tiene toda la información
            items_update = db_access["items_update"] # db_access está en los models.py
            print(f"{request.form=}") # estás para depurar, no va
            items_update( # se están asignando los valores en la base de datos
                id=id,
                tittle=request.form["tittle"],
                genres=request.form["genres"],
                authors=request.form["authors"],
            )
            return redirect("/")

        return render_template(
            "items.html",
            items=items,
            interactions=interactions,
            pages=[i + 1 for i in range(total_pages)],
        )
    
    @app.route("/users/<id>", methods=["GET", "POST"])
    def list_users_interactions(id: int):
        page = int(request.args.get("page", 1))

        users_interactions = db_access["users_interactions"]
        interactions = users_interactions(id, page)
        total_pages = ceil(interactions.total / 10)

        users_read = db_access["users_read"]
        users = users_read(id)

        if request.method == "POST": # el request tiene toda la información
            users_update = db_access["users_update"] # db_access está en los models.py
            print(f"{request.form=}") # estás para depurar, no va
            users_update( # se están asignando los valores en la base de datos
                id=id,
                name=request.form["name"],
                age=int(request.form["age"]),
                sex=request.form["sex"],
            )
            return redirect("/")

        return render_template(
            "users.html",
            users=users,
            interactions=interactions,
            pages=[i + 1 for i in range(total_pages)],
        )
    
    @app.route("/interactions/<id>", methods=["GET", "POST"])
    def list_interactions_interactions(id: int):
        page = int(request.args.get("page", 1))

        

        interactions_read = db_access["interactions_read"]
        interactions = interactions_read(id)

        if request.method == "POST": # el request tiene toda la información
            interactions_update = db_access["interactions_update"] # db_access está en los models.py
            print(f"{request.form=}") # estás para depurar, no va
            interactions_update( # se están asignando los valores en la base de datos
                id=id,
                users_id=int(request.form["users_id"]),
                item_id=int(request.form["item_id"]),
                
            )
            return redirect("/")

        return render_template(
            "interactions.html",
            interactions=interactions,
            
           
        )

    @app.route("/items/<items_id>/interactions/<int:interactions_id>/delete", methods=["GET"])
    def delete_items_interactions(items_id: int, interactions_id: int):
        interactions_delete = db_access["interactions_delete"]
        interactions_delete(interactions_id)

     

        return redirect(f"/items/{items_id}")

        

    @app.route("/items/<id>/delete", methods=["POST"])
    def items_delete(id: int):
        if request.method == "POST":
            items_delete = db_access["items_delete"]
            items_delete(id=id)
            return redirect("/")
        
    @app.route("/users/<id>/delete", methods=["POST"])
    def users_delete(id: int):
        if request.method == "POST":
            users_delete = db_access["users_delete"]
            users_delete(id=id)
            return redirect("/")
        
    
