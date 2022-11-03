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
    nit = ""
    id = ""
    tiempo = float
    fecha_hora = ""

    def __init__(self,nit,id,tiempo,fecha):
        self.nit= nit
        self.id = id
        self.tiempo =tiempo
        self.fecha = fecha


class Recurso():
    id = ""
    nombre = ""
    metrica = ""
    tipo = ""
    costo = float
    abreviatura = ""
    

    def __init__(self,id,nombre,abreviatura,metrica,tipo,costo):
        self.id=id
        self.nombre = nombre
        self.abreviatura =abreviatura
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

