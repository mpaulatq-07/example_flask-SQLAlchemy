from app import db

class Contact(db.Model): #se instancia
    id = db.Column (db.Integer, primarykey=True) #propiedad (se dice nombre de la tabla, ID, etc)
    fullname = db.Column (db.String(100))
    email = db.Column (db.String(100))
    phone = db.Column (db.String(100))


    #constructor
    def __init_(self, fullname, email, phone):  #recibir (datos)
        self.fullname = fullname
        self.email = email
        self.phone = phone


#cuando llame la clase pedira los datos y se creara por nosotros 
    