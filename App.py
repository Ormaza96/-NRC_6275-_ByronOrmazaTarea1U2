from flask import Flask, redirect, render_template, request, url_for
import pymongo

app = Flask(__name__, template_folder='templates')

#Gestion de coneccion a base de datos mongodb
MONGOHOST = "localhost"
MONGOPORT = "27017"
MONGO_TIEMPO_FUERA = 1000

MONGO_URI = "mongodb://" + MONGOHOST + ":" + MONGOPORT + "/"

MONGO_BASEDATOS = "Ormaza"
MONGO_COLLECTION = "Registro"

cliente = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
baseDatos = cliente[MONGO_BASEDATOS]
coleccion = baseDatos[MONGO_COLLECTION]

print(baseDatos.list_collection_names())


@app.route('/')
def index():
    return render_template('index.html')


#Ingreso datos
@app.route('/registrar', methods =["GET", "POST"])
def registrar():

    if request.method == 'POST':
        name = request.form.get('name')                      
        email =request.form.get('email')               
        subject = request.form.get('subject')         
        menssage = request.form.get('menssage')    

        dict = {"Nombre":name,                     
                "Email": email,            
                "Subject": subject,     
                "Mensaje": menssage      
                }

        insertar = coleccion.insert_one(dict)      

        print(insertar.inserted_id)             
        return redirect(url_for('index'))     
    else:
      return render_template('index.html')  

#Metodo para correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)