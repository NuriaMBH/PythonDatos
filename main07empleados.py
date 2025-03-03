
#from services import service07mysqlempleados as service
#from services import Service07oracleempleados as service
from services import service07sqlserverempleados as service
from models.empleado import Empleado

print("Probando servicios varios de BBDD")
servicio = service.ServiceSqlServerEmpleados()
empleados= servicio.getEmpleados()
for emp in empleados:
    print(f"Apellido: {emp.apellido}, oficio: {emp.oficio}, salario: {emp.salario}")
# print("Introduzca un salario para buscar")
# salario= int(input())
# empleados = servicio.getEmpleadosSalario(salario)
# print("----empleados filtrados-----")
# for emp in empleados:
#     print(f"Apellido: {emp.apellido}, oficio: {emp.oficio}, salario: {emp.salario}")
# print("Fin de programa")


    
        