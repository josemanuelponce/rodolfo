from math import floor, ceil
from typing import Callable

from flask import redirect, render_template, request


def init_views(app, db_access: dict[str, Callable]):
    @app.route("/", methods=["GET", "POST"])
    def index(): 
        
        page = int(request.args.get("page", 1))
        

        items_list = db_access["items_list"] 

        items = items_list(page=page)        

        total_pages = ceil (items.total / 10)

        


        return render_template( 

            "index.html", items=items, pages=[i + 1 for i in range(total_pages)] 
        )
    
    @app.route("/create", methods=["GET", "POST"])
    def create():
        
        if request.method == "GET":
            return render_template("create.html")

        if request.method == "POST":
            print("holaaaaaaaaaaaaaaaa")
            # create_contact = db_access["create"]
            # create_contact(
            #     tittle=request.form["tittle"],
            #     genres=request.form["genres"],
            #     authors=request.form["authors"],
            # )
            return redirect("/")



    @app.route("/items/<uid>", methods=["GET", "POST"])
    def list_items_interactions(uid: str):
        page = int(request.args.get("page", 1))

        items_interactions = db_access["items_interactions"]
        interactions = items_interactions(uid, page)
        total_pages = ceil(interactions.total / 10)

        items_read = db_access["items_read"]
        items = items_read(uid)

        if request.method == "POST": # el request tiene toda la información
            items_update = db_access["items_update"] # db_access está en los models.py
            print(f"{request.form=}") # estás para depurar, no va
            items_update( # se están asignando los valores en la base de datos
                uid=uid,
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

    @app.route("/items/<items_id>/interactions/<int:interactions_id>/delete", methods=["GET"])
    def delete_items_interactions(items_id: str, interactions_id: int):
        interactions_delete = db_access["interactions_delete"]
        interactions_delete(interactions_id)

     

        return redirect(f"/items/{items_id}")

        

    @app.route("/items/<uid>/delete", methods=["POST"])
    def items_delete(uid: int):
        if request.method == "POST":
            items_delete = db_access["items_delete"]
            items_delete(uid=uid)
            return redirect("/")
