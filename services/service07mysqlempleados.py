import pymysql
from models.empleado import Empleado



from models.empleado import Empleado
class ServiceMySqlEmpleados:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',port=3306,user='getafe',passwd='mysql',db='HOSPITAL')
    def getEmpleados(self):
        sql="select * from EMP"
        cursor=self.connection.cursor()
        cursor.execute(sql)
        data:list[Empleado] = []
        for row in cursor:
            emp=Empleado()
            emp.idEmpleado = row[0]
            emp.apellido= row[1]
            emp.oficio=row[2]
            emp.salario= row[5]
            data.append(emp)
        cursor.close()
        return data
    def getEmpleadosSalario(self, salario):
        sql="select * from EMP where SALARIO >= %s"
        cursor=self.connection.cursor()
        cursor.execute(sql,(salario,))
        #debemos indocar el tipo de lista que estamos devolviendo
        #variable:list[tipo de clase]=[]
        data:list[Empleado] = []
        for row in cursor:
            emp=Empleado()
            emp.idEmpleado = row[0]
            emp.apellido= row[1]
            emp.oficio=row[2]
            emp.salario= row[5]
            data.append(emp)
        cursor.close()
        return data
   
