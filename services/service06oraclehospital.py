import oracledb
from models import hospital as model
class ServiceOracleHospital:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe') 
    def getAllHospitall(self):
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
    sql = "insert into DOCTOR values (:id,:hosp)"   
            