from flask import Flask  # importacion de clase flask
from routes.contacts import contacts  # importar en Blueprint
from utils.db import db


def create_app():
    app = Flask(__name__)  # Ejecutar flask y que devuelva un objeto,en este caso app

    # pasar parametros para poder configurarlo (nombre bd, contraseña, etc)
    app.secret_key = "secret_key_1234"

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql://root:12345@localhost/contactsdb"  # a donde queremos concetarnos
    )
    # propiedad con valor de la direccion de la BD
    # https://www.youtube.com/watch?v=BP3D03CYFHA&t=2538s

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = (
        False  # Configuracion flask (por defecto)
    )

    db.init_app(app)

    # SQLAlchemy(app) #pasar pasa en el modulo el app

    app.register_blueprint(contacts)  # añadirlo a la app
    return app
