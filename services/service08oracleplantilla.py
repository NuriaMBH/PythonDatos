#getPlantilla(): mostrara los datos(listado de la plantilla)
#updateSalarioPlantilla():modificara el salario de la plantilla de un hospital 
#con un incremento que le daremos y con un numero de hospital
import oracledb
from models.plantilla import Plantilla
class ServiceOraclePlantilla:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle'
        , dsn='localhost/xe') 
    def getPlantilla(self):
        sql = "select * from PLANTILLA"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        #DEBEMOS INDICAR EL TIPO DE LISTA QUE 
        #ESTAMOS DEVOLVIENDO
        # variable:list[TIPO DE CLASE] = []
        data:list[Plantilla] =[]
        for row in cursor:
            PLANTILLA = Plantilla()
            PLANTILLA.idPlantilla = row[0]
            PLANTILLA.apellido = row[4]
            PLANTILLA.funcion = row[5]
            PLANTILLA.salario = row[7]
            PLANTILLA.hospital= row[6]
            data.append(PLANTILLA)
        cursor.close()
        return data   
    def updateSalarioPlantilla(self, salario_incremento, hospital_id):
        sql = "UPDATE PLANTILLA SET SALARIO = SALARIO + :incremento WHERE HOSPITAL_ID = :hospital_id"
        cursor = self.connection.cursor()
        cursor.execute(sql, {'incremento': salario_incremento, 'hospital_id': hospital_id})
        data:list[Plantilla] = []
        for row in cursor:
            PLANTILLA = Plantilla()
            PLANTILLA.idPlantilla = row[0]
            PLANTILLA.apellido = row[4]
            PLANTILLA.funcion = row[5]
            PLANTILLA.salario = row[7]
            PLANTILLA.hospital= row[]
            data.append(emp)
        cursor.close()
        return data