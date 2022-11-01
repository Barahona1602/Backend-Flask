class Cliente():
    nit = ""
    nombre = ""
    usuario = ""
    contra = ""
    direccion = ""
    email = ""
    instancias = []


    def __init__(self,nit,nombre,usuario,contra,direccion,email,instancias):
        self.nit= nit
        self.nombre = nombre
        self.usuario =usuario
        self.contra = contra
        self.direccion = direccion
        self.email = email
        self.instancias = instancias
    

class Consumo():
    nit_cliente = ""
    id_Instancia = ""
    tiempo_consumido = float
    fecha_hora = ""

    def __init__(self,nit_cliente,id_Instancia,tiempo_consumido,fecha_hora):
        self.nit_cliente= nit_cliente
        self.id_Instancia = id_Instancia
        self.tiempo_consumido =tiempo_consumido
        self.fecha_hora = fecha_hora


class Recurso():
    id_recurso = ""
    nombre_recurso = ""
    metrica = ""
    tipo = ""
    costo = float
    abreviatura_recurso = ""
    

    def __init__(self,id_recurso,nombre_recurso,abreviatura_recurso,metrica,tipo,costo):
        self.id_recurso=id_recurso
        self.nombre_recurso = nombre_recurso
        self.abreviatura_recurso =abreviatura_recurso
        self.metrica =metrica
        self.tipo = tipo
        self.costo = costo



class Configuracion():
    id = ""
    nombre = ""
    descripcion = ""
    recursos = []

    def __init__(self,id,nombre,descripcion,recursos):
        self.id=id
        self.nombre = nombre
        self.descripcion =descripcion
        self.recursos = recursos
    


class Categoria():
    id = ""
    nombre = ""
    descripcion = ""
    carga = ""
    configs = []
    
    
    def __init__(self,id,nombre,descripcion,carga,configs):
        self.id=id
        self.nombre = nombre
        self.descripcion =descripcion
        self.carga = carga
        self.configs = configs
    

class Instancia():
    idI = ""
    idC = ""
    nombre = ""
    fecha1 = ""
    fecha2 = ""
    estado = ""


    def __init__(self,idI,idC,nombre,fecha1,fecha2,estado):
        self.idI= idI
        self.idC = idC
        self.nombre =nombre
        self.fecha1 = fecha1
        self.fecha2 = fecha2
        self.estado = estado

