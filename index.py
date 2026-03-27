from app import create_app
from utils.db import db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":  #si el proyecto se ejecuta como archivo principal se ejecuta el proyecto flask
    app.run(debug=True)  #Para evitar reiniciar el codigo
