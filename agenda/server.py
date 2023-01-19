from myapp.app import create_app
# en app, que esta dentro de la carpeta my app esta la funcion creada

if __name__ == "__main__":
    app = create_app() # se crea la aplicacion
    app.run(debug=True) # se ejecuta la aplicacion