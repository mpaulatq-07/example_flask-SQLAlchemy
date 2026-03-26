from flask import Blueprint, render_template, request  #crear seccion dentro de la app
                                              #Funcion Render: Procesar un archivo para devolverlo al navegador

from models.contact import Contact                                              


contacts = Blueprint('contacts', __name__) #al ejecutar se pone nombre en este caso contacts
                                        # se crea secci`on para los contactos y devolvera un enrutador

@contacts.route("/")
def home():  #creacion de funcion home 
    return render_template('index.html')


@contacts.route('/new', methods=['POST']) 
def add_contact():
    fullname=request.form['fullname']
    email=request.form['email']
    phone=request.form['phone']

    new_contact=Contact(fullname, email, phone)  #los datos se pasan a la clase contact que se devuelve en un objeto

    print(new_contact)
    
    return "Saving a contact"


@contacts.route('/update')
def update():
    return "Update a contact"


@contacts.route('/delete')
def delete():
    return "Delete a contact"


@contacts.route('/about')
def about():
    return render_template('about.html')

