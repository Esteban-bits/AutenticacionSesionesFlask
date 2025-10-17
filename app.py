from flask import Flask, render_template, redirect, request
from models import db  
import controlador        

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/juegosAlq'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
@app.route("/juegos")
def juegos():
    juegos_lista = controlador.obtener_juegos()
    return render_template("juegos.html", juegos=juegos_lista)

@app.route("/agregar_juego")
def formulario_agregar_juego():
    return render_template("agregar_juego.html")

@app.route("/guardar_juego", methods=["POST"])
def guardar_juego():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador.insertar_juego(nombre, descripcion, precio)
    return redirect("/juegos")

@app.route("/eliminar_juego", methods=["POST"])
def eliminar_juego():
    id_juego = int(request.form["id"])
    controlador.eliminar_juego(id_juego)
    return redirect("/juegos")

@app.route("/formulario_editar_juego/<int:id>")
def editar_juego(id):
    juego = controlador.obtener_juego_por_id(id)
    return render_template("editar_juego.html", juego=juego)

@app.route("/actualizar_juego", methods=["POST"])
def actualizar_juego():
    id_juego = int(request.form["id"])
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador.actualizar_juego(id_juego, nombre, descripcion, precio)
    return redirect("/juegos")

if __name__ == '__main__':
    with app.app_context(): 
        db.create_all()     
    app.run(debug=True)
