from cgitb import reset
from ctypes import resize
from os import TMP_MAX
from re import I
from shlex import join
from turtle import clearstamp
from flask import Flask, request,jsonify
from flask_restful import Api
from flask_cors import CORS, cross_origin
import json
from xml.dom import minidom

from datos import *


app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route("/cargarConfiguracionDB", methods=['POST'])
def cargarConfiguracionDB():
  
    datos = open('backend/archivoConfiguracion.xml')

    archivosconfig =  minidom.parse(datos)
    

    global Cat
    Cat=[]
    global cfgs1
    cfgs1=[]
    global Rec
    Rec=[]
    global Ins
    Ins=[]
    global Clt
    Clt=[]
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
       Rec.append(res)
    

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
                recursos ={"IdRec":idRec,"Cantidad":rec.firstChild.data}
                i+=1
                listconfig.append(recursos)

            confs = Configuracion(idconfig,nombreconf.firstChild.data,descconf.firstChild.data,listconfig)
            Configuraciones.append(confs)
            
            cfgs1.append(confs)
            
        cats = Categoria(idcat,nombrecat.firstChild.data,descrcat.firstChild.data,cargacat.firstChild.data,Configuraciones)
        Cat.append(cats) 
    
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
                fecha_final = '*'
            
            insts = Instancia(idinstance,idconfiguracion.firstChild.data,nombre.firstChild.data,fecha_inicio.firstChild.data,fecha_final,estado.firstChild.data)
            Instancias.append(insts)
            
            Ins.append(insts)
            
        clts = Cliente(NIT,nombre_cliente.firstChild.data,usuario.firstChild.data,clave.firstChild.data,direccion.firstChild.data,email.firstChild.data,Instancias)
        Clt.append(clts)
            
    Dato ={
        'Información': 'Se leyó el archivo correctamente',
        'recursos':'Se añadieron '+ str(count_recursos)+' recursos',
        'categorias':'Se añadieron '+str(contadoracat)+' categorias',
        'clientes':'Se añadieron ' +str(contadoraclientes)+' clientes',
    }   


    if datos != '':
        response =jsonify(Dato)
        return(response)
    else:
        return jsonify({'data': 'error'})



@app.route("/cargarConfiguracion", methods=['POST'])
def cargarConfiguracion():
  
    datos = open('backend/archivoConfiguracion.xml')

    archivosconfig =  minidom.parse(datos)
    

    global Cat
    Cat=[]
    global cfgs1
    cfgs1=[]
    global Rec
    Rec=[]
    global Ins
    Ins=[]
    global Clt
    Clt=[]
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
       Rec.append(res)
    

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
                recursos ={"IdRec":idRec,"Cantidad":rec.firstChild.data}
                i+=1
                listconfig.append(recursos)

            confs = Configuracion(idconfig,nombreconf.firstChild.data,descconf.firstChild.data,listconfig)
            Configuraciones.append(confs)
            
            cfgs1.append(confs)
            
        cats = Categoria(idcat,nombrecat.firstChild.data,descrcat.firstChild.data,cargacat.firstChild.data,Configuraciones)
        Cat.append(cats) 
    
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
                fecha_final = '*'
            
            insts = Instancia(idinstance,idconfiguracion.firstChild.data,nombre.firstChild.data,fecha_inicio.firstChild.data,fecha_final,estado.firstChild.data)
            Instancias.append(insts)
            
            Ins.append(insts)
            
        clts = Cliente(NIT,nombre_cliente.firstChild.data,usuario.firstChild.data,clave.firstChild.data,direccion.firstChild.data,email.firstChild.data,Instancias)
        Clt.append(clts)
            
    Dato ={
        'Información': 'Se leyó el archivo correctamente',
        'recursos':'Se añadieron '+ str(count_recursos)+' recursos',
        'categorias':'Se añadieron '+str(contadoracat)+' categorias',
        'clientes':'Se añadieron ' +str(contadoraclientes)+' clientes',
    }   


    if datos != '':
        response =jsonify(Dato)
        return(response)
    else:
        return jsonify({'data': 'error'})



@app.route("/cargarConsumos", methods=['POST'])
def cargarConsumos():
    datos = request.get_data()
    cons =  minidom.parseString(datos)
    
    global Cons
    Cons=[]
    consumos = cons.getElementsByTagName('listadoConsumos')[0]
    consum = consumos.getElementsByTagName('consumo')
    count_consumos = 0
    for i in consum:
        count_consumos += 1
        cliente_nit = i.attributes['nitCliente'].value
        instance_id = i.attributes['idInstancia'].value
        tiempo_consum = i.getElementsByTagName('tiempo')[0]
        fechaHora = i.getElementsByTagName('fechaHora')[0]
        cns = Consumo(cliente_nit,instance_id,tiempo_consum.firstChild.data,fechaHora.firstChild.data)
        
        Cons.append(cns)
    
    Dato ={
        'Información': 'Se leyó el archivo correctamente',
        'consumos':'Se añadieron '+str(count_consumos)+' consumos',
    }
    if datos != '':
        response =jsonify(Dato)
        return(response)
    else:
        return jsonify({'data': 'error'})



@app.route("/cargarConsumosDB", methods=['POST'])
def cargarConsumosDB():
    datos = open('backend/consumos.xml')
    cons =  minidom.parse(datos)
    
    global Cons
    Cons=[]
    consumos = cons.getElementsByTagName('listadoConsumos')[0]
    consum = consumos.getElementsByTagName('consumo')
    count_consumos = 0
    for i in consum:
        count_consumos += 1
        nit = i.attributes['nitCliente'].value
        id = i.attributes['idInstancia'].value
        tiempo_consum = i.getElementsByTagName('tiempo')[0]
        fechaHora = i.getElementsByTagName('fechaHora')[0]
        cns = Consumo(nit,id,tiempo_consum.firstChild.data,fechaHora.firstChild.data)
        
        Cons.append(cns)
    
    Dato ={
        'Información': 'Se leyó el archivo correctamente',
        'consumos':'Se añadieron '+str(count_consumos)+' consumos',
    }
    if datos != '':
        response =jsonify(Dato)
        return(response)
    else:
        return jsonify({'data': 'error'})   



@app.route("/consultarCategorias", methods=['GET'])
def consultarCategorias():
    ct = []
    for c in Cat:
        
        config =c.configs
        configs = []
        
        for j in config:
            
            list_recu = j.recursos
            recursos = []
            for i in list_recu:
                Dato_rec ={"Id del recurso":i['IdRec'],"Cantidad":i['Cantidad']}
                recursos.append(Dato_rec)
            
            confjson ={
            'id':j.id,
            'nombre':j.nombre,
            'descripcion':j.descripcion,
            'recursos': recursos,          
            }
            configs.append(confjson)
        
        Dato ={
            'Información':'Categorías',
            'id':c.id,
            'Nombre':c.nombre,
            'descripcion':c.descripcion,
            'carga':c.carga,
            'lista configuraciones': configs, 
        }
        
        ct.append(Dato)
    res = jsonify(ct)
    return (res)
    
    


@app.route("/consultarConfiguraciones", methods=['GET'])
def consultarConfiguraciones(): 
    
    configs = []
    for c in Cat:        
        config =c.configs  
        for j in config:
            
            list_recu = j.recursos
            recursos = []
            for i in list_recu:
                Dato_rec ={"Id del recurso":i['IdRec'],"Cantidad":i['Cantidad']}
                recursos.append(Dato_rec)
            
            confjson ={
            'id':j.id,
            'nombre':j.nombre,
            'descripcion':j.descripcion,
            'recursos': recursos,          
            }
            configs.append(confjson)
        
    res = jsonify(configs)
    return (res)



@app.route("/consultarClientes", methods=['GET'])
def consultarClientes():
    
    clt = []
    for j in Clt:
        
        instancias = []
        
        for i in j.instancias:
            
            list_inst ={
                'Id':i.idI,
                'Id de configuracion':i.idC,
                'nombre':i.nombre,
                'fecha_inicio':i.fecha1,
                'fecha_final':i.fecha2,
                'estado_instancia':i.estado 
            }
            instancias.append(list_inst)
        
        Dato ={
            'nit':j.nit,
            'nombre':j.nombre,
            'user':j.usuario,
            'password':j.contra,
            'direccion':j.direccion,
            'email':j.email,
            'lista_inst':instancias        
        }
        clt.append(Dato)
    res = jsonify(clt)
    return (res)



@app.route("/consultarInstancias", methods=['GET'])
def consultarInstancias():
    
    instancias = []
    for j in Clt:
        for i in j.instancias:
            
            list_inst ={
                'Id':i.idI,
                'Id de configuracion':i.idC,
                'nombre':i.nombre,
                'fecha_inicio':i.fecha1,
                'fecha_final':i.fecha2,
                'estado_instancia':i.estado 
            }
            instancias.append(list_inst)
        
    res = jsonify(instancias)
    return (res)


@app.route("/consultarRecursos", methods=['GET'])
def consultarRecursos():
    rs = []
    
    for i in Rec:
        Dato={
            'Id':i.id,
            'Nombre':i.nombre,
            'Abreviatura':i.abreviatura,
            'Tipo':i.tipo,
            'Costo':i.costo,
            'Metrica':i.metrica            
        }
        rs.append(Dato)
    res = jsonify(rs)
    return (res)




@app.route("/crearRecurso", methods=['POST'])
def crearRecurso():
    
    
    recurso = request.get_json()
    
    id = recurso['id']
    nombre = recurso['nombre']
    abreviatura = recurso['abreviatura']
    metrica = recurso['metrica']
    tipo = recurso['tipo']
    costo = recurso['costo']
    
    tmp = Recurso(id,nombre,abreviatura, metrica, tipo,costo)
    Rec.append(tmp)
    
    Dato = {
                'info': 'Se agregó un recurso',
            }
    res = jsonify(Dato)
    return (res)




@app.route("/crearCategoria", methods=['POST'])
def crearCategoria():
    
    cats = request.get_json()
    
    id = cats['id']
    nombre = cats['nombre']
    descripcion = cats['descripcion']
    carga = cats['carga']
    configuraciones = cats['configuraciones']
    
    listconf = []
    print(configuraciones['id'])
    for i in cfgs1:
        if configuraciones['id'] == i.id:
            listconf.append(i)
            break
    
    tmp = Categoria(id,nombre,descripcion, carga,listconf)
    Cat.append(tmp)
    Dato = {
            'info': 'Se agregó una categoría',
            }
    res = jsonify(Dato)
    return (res)




@app.route("/crearConfiguracion", methods=['POST'])
def crearConfiguracion():
    configuracion = request.get_json()    
    id = configuracion['id']
    nombre = configuracion['nombre']
    descripcion= configuracion['descripcion']
    recursos = configuracion['recursos']
    
    recs =[]
    for i in recursos:
        Dato_rec ={
            'id del recurso':recursos['id'],
            'cantidad':recursos['cantidad'],         
        }
        recs.append(Dato_rec)           
    
    nuevaConfig = Configuracion(id,nombre,descripcion,recs)
    cfgs1.append(nuevaConfig)
    
    Dato = {
                'info': 'Se agregó una configuración'
            }
    respuesta = jsonify(Dato)
    return (respuesta) 




@app.route("/crearCliente", methods=['POST'])
def crearCliente():
    c = request.get_json()
    
    nit = c['nit']
    nombre = c['nombre']
    user = c['user']
    password = c['password']
    direccion = c['direccion']
    email = c['email']
    instancias = c['instancias']
    
    listinst = []
    
    for i in Ins:
        if instancias['id'] == i.idI:
            listinst.append(i)
            break
    
    tmp = Cliente(nit,nombre,user, password,direccion,email,listinst)
    Clt.append(tmp)
    Dato = {
            'info': 'Se agregó un cliente'
            }
    respuesta = jsonify(Dato)
    return (respuesta)





@app.route("/crearInstancia", methods=['POST'])
def crearInstancia():
    i = request.get_json()
    
    id = i['id']
    configuracion = i['id_config']
    nombre = i['nombre']
    fecha1 = i['fecha']
    fecha2 = '--'
    estado = i['estado']
    
    tmp = Instancia(id,configuracion,nombre,fecha1,fecha2,estado)
    Ins.append(tmp)
    
    Dato = {
                'info': 'Se agregó una instancia'
            }
    respuesta = jsonify(Dato)
    return (respuesta)




@app.route("/generarFactura", methods=['POST'])
def generarFactura():
    cost =0
    consclt = []
    cst =[]
    consin =[]
    val = False
    
    tmp = request.get_json()
    nit2 = tmp['nit_cliente']
    

    for i in Cons:
        if i.nit == nit2:
            val = True
            instancia = i.id
            tiempo =i.tiempo
            fecha = i.fecha
            
            datos ={
                'instancia': instancia,
                'tiempo': tiempo,
                'fecha_hora': fecha
            }
            consclt.append(datos)
        
    if val == False:
        dato={
            'info': 'No existe consumo'
        }
        res = jsonify(dato)
        return (res)    

    for i in Clt:
        if i.nit == nit2:
            nombre = i.nombre
    
    for i in consclt:
        tiempo = i['tiempo']
        fecha_hora  = i['fecha_hora']
        csttot = 0
        
        for j in Ins:
            
            if i['instancia'] == j.idI:
                configuracion_id = j.idC
        
        for j in cfgs1:
            if configuracion_id == j.id:
                recursos = j.recursos
                
                cstconfig = 0

                for k in recursos:
                    id = k['IdRec']
                    cantidad = k['Cantidad']
  
                    for m in Rec:
                        if m.id == id:
                            costh =  m.costo

                    vlr =   float(costh) * int(cantidad)
                    cstconfig = cstconfig + vlr

        
        csttot =  cstconfig * float(tiempo)
        datos ={
            'costo_consumo':round(csttot,4),
            'fecha_hora':fecha_hora
        }
        consumo_ind ={
            'tiempo': tiempo,
            'costo':round(csttot,4)
        }
        cst.append(datos)
        consin.append(consumo_ind)
        
        
    
    for datos in cst:
        costo = datos['costo_consumo']
        cost = cost + costo
        fecha_final_consumo = str(datos['fecha_hora'])
        
        
    Dato = {
        'Nombre': nombre,
        'Nit':nit2,
        'Monto':round(cost,4),
        'Fecha ':fecha_final_consumo,
        'consumo':consin
    }
    respuesta = jsonify(Dato)
    return (respuesta)



if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host="0.0.0.0", port="5000")