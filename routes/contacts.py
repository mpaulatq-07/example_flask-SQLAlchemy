from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)  # crear seccion dentro de la app

# Funcion Render: Procesar un archivo para devolverlo al navegador

from models.contact import Contact
from utils.db import db


contacts = Blueprint(
    "contacts", __name__
)  # al ejecutar se pone nombre en este caso contacts
# se crea secci`on para los contactos y devolvera un enrutador


@contacts.route("/")
def home():  # creacion de funcion home y se traen los contactos para ser listados
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)


@contacts.route("/new", methods=["POST"])
def add_contact():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]  # se reciben los datos del formulario

    new_contact = Contact(
        fullname, email, phone
    )  # los datos se pasan a la clase contact que se devuelve en un objeto

    db.session.add(new_contact)
    db.session.commit()

    flash("Contact added successfully!")

    return redirect(url_for("contacts.home"))


@contacts.route("/update/<id>", methods=["POST", "GET"])
def update(id):

    contact = Contact.query.get_or_404(id)

    if request.method == "POST":
        contact.fullname = request.form["fullname"]
        contact.email = request.form["email"]
        contact.phone = request.form["phone"]

        db.session.commit()
        return redirect(url_for("contacts.home"))

    return render_template("update.html", contact=contact)


@contacts.route("/delete/<id>")
def delete(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for("contacts.home"))


@contacts.route("/about")
def about():
    return render_template("about.html")
