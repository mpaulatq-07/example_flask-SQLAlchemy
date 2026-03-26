from app import app, db


with app.app_context():
    db.create_all()

if __name__ == "__main__":  #si el proyecto se ejecuta como archivo principal se ejecuta el proyecto flask
    app.run(debug=True)  #Para evitar reiniciar el codigo
