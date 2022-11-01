from flask import Flask, request,jsonify
from flask_restful import Api
from flask_cors import CORS, cross_origin
import json
from dotenv import load_dotenv
from xml.dom import minidom

from datos import *


app = Flask(__name__)
CORS(app)
api = Api(app)
load_dotenv()

@app.route("/cargarConfiguracion", methods=['POST'])
def cargarConfiguracion():
  
    global Categorias
    Categorias=[]
    configuracion = open('backend/archivoConfiguracion.xml')

    archivosconfig =  minidom.parse(configuracion)
    

    
    listRecursos_gen = archivosconfig.getElementsByTagName('listaRecursos')[0]
    recursos_list = listRecursos_gen.getElementsByTagName('recurso')
    count_recursos = 0
    for i in recursos_list:
       count_recursos += 1
       id = i.attributes['id'].value
       nombre = i.getElementsByTagName('nombre')[0]
       abreviatura = i.getElementsByTagName('abreviatura')[0]
       metrica = i.getElementsByTagName('metrica')[0]
       tipo = i.getElementsByTagName('tipo')[0]
       valorXhora = i.getElementsByTagName('valorXhora')[0]
       res = Recurso(id ,nombre.firstChild.data,abreviatura.firstChild.data,metrica.firstChild.data,tipo.firstChild.data,valorXhora.firstChild.data)
       global Recursos
       Recursos=[]
       Recursos.append(res)
    

    cate = archivosconfig.getElementsByTagName('listaCategorias')[0]
    categorias = cate.getElementsByTagName('categoria')
    contadoracat = 0
    for i in categorias:
        Configuraciones = [] 
        
        contadoracat += 1
        idcat = i.attributes['id'].value
        nombrecat = i.getElementsByTagName('nombre')[0]
        descrcat = i.getElementsByTagName('descripcion')[0]
        cargacat = i.getElementsByTagName('cargaTrabajo')[0]
        list_config = i.getElementsByTagName('configuracion')

        #configuraciones por Categoria
        contadoraconfig = 0
        for j in list_config:
            contadoraconfig += 1
            idconfig = j.attributes['id'].value
            nombreconf = j.getElementsByTagName('nombre')[0]
            descconf = j.getElementsByTagName('descripcion')[0]
            
            recursosCat = j.getElementsByTagName('recurso')

            listconfig = []
            i=0
            for k in recursosCat:
                idRec = k.attributes['id'].value
                rec = j.getElementsByTagName('recurso')[i]
                recursos ={
                    "IdRec":idRec,
                    "Cantidad":rec.firstChild.data
                }
                i+=1
                listconfig.append(recursos)

            confs = Configuracion(idconfig,nombreconf.firstChild.data,descconf.firstChild.data,listconfig)
            Configuraciones.append(confs)
            global Configuraciones_glob
            Configuraciones_glob=[]
            Configuraciones_glob.append(confs)
            
        cats = Categoria(idcat,nombrecat.firstChild.data,descrcat.firstChild.data,cargacat.firstChild.data,Configuraciones)
        Categorias.append(cats) 
    
    clientes = archivosconfig.getElementsByTagName('cliente')
    contadoraclientes = 0 
    for i in clientes:
        contadoraclientes += 1
        Instancias = []
        
        NIT = i.attributes['nit'].value
        nombre_cliente = i.getElementsByTagName('nombre')[0]
        usuario = i.getElementsByTagName('usuario')[0]
        clave = i.getElementsByTagName('clave')[0]
        direccion = i.getElementsByTagName('direccion')[0]
        email = i.getElementsByTagName('correoElectronico')[0]
        instancias = i.getElementsByTagName('instancia')
        
        for j in instancias:
            idinstance = j.attributes['id'].value
            idconfiguracion = j.getElementsByTagName('idConfiguracion')[0]
            nombre = j.getElementsByTagName('nombre')[0]
            fecha_inicio = j.getElementsByTagName('fechaInicio')[0]
            estado = j.getElementsByTagName('estado')[0]
            if estado.firstChild.data == 'Cancelada':
                fecha_finalOn = j.getElementsByTagName('fechaFinal')[0]
                fecha_final = fecha_finalOn.firstChild.data
            else:
                fecha_final = '--'
            
            insts = Instancia(idinstance,idconfiguracion.firstChild.data,nombre.firstChild.data,fecha_inicio.firstChild.data,fecha_final,estado.firstChild.data)
            Instancias.append(insts)
            global Instancias_glob
            Instancias_glob=[]
            Instancias_glob.append(insts)
            
        clts = Cliente(NIT,nombre_cliente.firstChild.data,usuario.firstChild.data,clave.firstChild.data,direccion.firstChild.data,email.firstChild.data,Instancias)
        global Clientes
        Clientes=[]
        Clientes.append(clts)
            
    Dato ={
        'Información': 'Se leyó el archivo correctamente',
        'recursos':'Se añadieron '+ str(count_recursos)+' recursos',
        'categorias':'Se añadieron '+str(contadoracat)+' categorias',
        'clientes':'Se añadieron ' +str(contadoraclientes)+' clientes',
    }   


    if configuracion != '':
        response =jsonify(Dato)
        return(response)
    else:
        return jsonify({'data': 'error'})


@app.route("/cargarConsumos", methods=['POST'])
def cargarConsumos():
    consumos = open('backend/consumos.xml')
    consum_files =  minidom.parse(consumos)
    
    consumos = consum_files.getElementsByTagName('listadoConsumos')[0]
    consum = consumos.getElementsByTagName('consumo')
    count_consumos = 0
    for i in consum:
        count_consumos += 1
        cliente_nit = i.attributes['nitCliente'].value
        instance_id = i.attributes['idInstancia'].value
        tiempo_consum = i.getElementsByTagName('tiempo')[0]
        fechaHora = i.getElementsByTagName('fechaHora')[0]
        cns = Consumo(cliente_nit,instance_id,tiempo_consum.firstChild.data,fechaHora.firstChild.data)
        global Consumos
        Consumos=[]
        Consumos.append(cns)
    
    Dato ={
        'Información': 'Se leyó el archivo correctamente',
        'consumos':'Se añadieron '+str(count_consumos)+' consumos',
    }
    if consumos != '':
        response =jsonify(Dato)
        return(response)
    else:
        return jsonify({'data': 'error'})   



@app.route("/consultarCategorias", methods=['GET'])
def consultarCategorias():
    
    list_categorias = []
    for c in Categorias:
        
        config =c.configs
        configs = []
        
        for conf in config:
            
            list_recu = conf.recursos
            recursos = []
            for rec in list_recu:
                Dato_rec ={
                    'Id del recurso':rec['IdRec'],
                    'Cantidad':rec['Cantidad'],         
                }
                recursos.append(Dato_rec)
            
            Dato_conf ={
            'id':conf.id,
            'nombre':conf.nombre,
            'descripcion':conf.descripcion,
            'recursos': recursos,          
            }
            configs.append(Dato_conf)
        
        Dato ={
            'Información':'Categorías',
            'id':c.id,
            'Nombre':c.nombre,
            'descripcion':c.descripcion,
            'carga':c.carga,
            'lista de configuraciones': configs, 
        }
        
        list_categorias.append(Dato)
    respuesta = jsonify(list_categorias)
    return (respuesta)


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