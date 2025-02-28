import oracledb
from models import hospital as model
class ServiceOracleHospital:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe') 
    def getAllHospital(self):
        sql="select* from HOSPITAL"
        cursor=self.connection.cursor()
        cursor.execute(sql)
        datos=[]
        for row in cursor:
            doc=model.Hospital()
            doc.idhospital = row[1]
            doc.nombre= row[2]
            doc.direccion=row[3]
            doc.telefono= row[4]
            doc.numCama= row[0]
            datos.append(doc)
        cursor.close()
        return datos
def insertarHospital(self, idhospital,nombre,direccion,telefono,numCama):
    sql = "insert into DOCTOR values (:id,:hosp,:nom,:dir,:telf,:cam)"
    cursor = self.connection.cursor()
    cursor.execute(sql,(nombre,idhospital,direccion,telefono,numCama))   
    registros = cursor.rowcount
    self.connection.comit()
    cursor.close()
    return registros
def eliminarHospital(self, idhospital):
    sql="delete from hospital where Hospital_NO=:P1"####
    cursor = self.connection.cursor()
    cursor.execute(sql,(idhospital,))
    registros =cursor.rowcount
    self.connection.commit()
    cursor.close
    return registros 
#####
def modificarHospital(self,idhospital,direccion,telefono,numCama):
    sql="""
        update HOSPITAL set DIRECCION=:p1, TELEFONO=:p2
        ,NUMCAMA=p3,HOSPITAL_COD=:p4
        where NOMBRE=:p5
    """
    cursor = self.connection.cursor()
    cursor.execute(sql,(idhospital,direccion,telefono,numCama))
    registros = cursor.rowcount
    self.connection.commit()
    cursor.close()
    return registros        