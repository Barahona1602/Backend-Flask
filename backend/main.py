from flask import Flask, request,jsonify
from flask_restful import Api
from flask_cors import CORS, cross_origin
import json
from dotenv import load_dotenv
from xml.dom import minidom




app = Flask(__name__)
CORS(app)
api = Api(app)
load_dotenv()

@app.route("/cargarConfiguracion", methods=['POST'])
def cargarConfiguracion():
    pass


@app.route("/cargarConsumos", methods=['POST'])
def cargarConsumos():
    pass

@app.route("/consultarDatos", methods=['GET'])
def consultarDatos():
    pass


#correcto
@app.route("/crearRecurso", methods=['POST'])
def crarRecurso():
    pass

#correcto
@app.route("/crearCategoria", methods=['POST'])
def crarCategoria():
    pass

#correcto
@app.route("/crearConfiguracion", methods=['POST'])
def crarConfiguracion():
    pass

#correcto
@app.route("/crearCliente", methods=['POST'])
def crarCliente():
    pass

@app.route("/crearInstancia", methods=['POST'])
def crarInstancia():
    pass



if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host="0.0.0.0", port="5000")