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
    
    # def getNIT (self):
    #     return self.nit 
    
    # def setNIT (self, nit):
    #     self.nit = nit
    
    # def getnombre (self):
    #     return self.nombre 
    
    # def setnombre (self, nombre):
    #     self.nombre = nombre
    
    # def getusuario (self):
    #     return self.usuario 
    
    # def setusuario (self, usuario):
    #     self.usuario = usuario
    
    # def getcontra (self):
    #     return self.contra 
    
    # def setcontra (self, contra):
    #     self.contra = contra
    
    # def getdireccion (self):
    #     return self.contra 
    
    # def setdireccion (self, direccion):
    #     self.direccion = direccion
    
    # def getemail (self):
    #     return self.email 
    
    # def setemail (self, email):
    #     self.email = email

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
    
    # def get_id (self):
    #     return self.id 
    
    # def set_id (self, id):
    #     self.id = id
    
    # def get_nombre (self):
    #     return self.nombre 
    
    # def set_nombre (self, nombre):
    #     self.nombre = nombre
    
    # def get_descripcion (self):
    #     return self.descripcion 
    
    # def set_descripcion (self, descripcion):
    #     self.descripcion = descripcion


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
    
    
    # def getid (self):
    #     return self.id 
    
    # def setid (self, id):
    #     self.id = id
    
    # def getnombre (self):
    #     return self.nombre 
    
    # def setnombre (self, nombre):
    #     self.nombre = nombre
    
    # def getdescripcion (self):
    #     return self.descripcion 
    
    # def setdescripcion (self, descripcion):
    #     self.descripcion = descripcion
    
    # def getcarga (self):
    #     return self.carga 
    
    # def setcarga (self, carga):
    #     self.carga = carga




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

    # def getidI (self):
    #     return self.idI 
    
    # def setidI (self, idI):
    #     self.idI = idI
    
    # def getidC (self):
    #     return self.idC 
    
    # def setidC (self, idC):
    #     self.idC = idC
        
    # def getnombre (self):
    #     return self.nombre 
    
    # def setnombre(self, nombre):
    #     self.nombre = nombre
    
    # def getfecha1 (self):
    #     return self.fecha1 
    
    # def setfecha1 (self, fecha1):
    #     self.fecha1 = fecha1
    
    # def getfecha2 (self):
    #     return self.fecha2 
    
    # def setfecha2 (self, fecha2):
    #     self.fecha2 = fecha2
    
    # def getestado (self):
    #     return self.estado 
    
    # def setestado (self, estado):
    #     self.estado = estado