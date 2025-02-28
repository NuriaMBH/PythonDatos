from models import doctor as model
from services import service05oracledoctores as service### como se llama el fichero de service


print("-------CRUD DOCTORES-----")
servicio = service.ServiceOracleDoctores()###como se llama la clase, la cual esta dentro del fichero de service
doctores = servicio.getAllDoctores ()
for doc in doctores:
    print(f"{doc.idDoctor}{doc.apellido}, Especialidad:{doc.especialidad},{doc.salario}")
    
print("1.-Insertar Doctor")
print("2.-Eliminar Doctor")
print("3.- Modificar Doctor")
print("Selecciones una opción")
opcion=int(input())
if (opcion ==1):
    print("ID DEL DOCTOR")
    idDoctor = int(input())
    print ("Apellido")
    ape= input()
    print("especialidad")
    espe = input()
    print("salario")
    sal= int(input())
    print("Hospital")
    hosp=int(input())
    reg= servicio.insertarDoctor(idDoctor, ape, espe,sal,hosp)
    print(f"Doctores insertados:{reg}")
elif (opcion==2):
    print("Introduzca ID a eliminar")
    iddoctor= int(input())
    registros = servicio.eliminarDoctor(iddoctor)
    print(f"Doctores eliminados: {registros}")
elif(opcion==3):
    print("Id del doctor modificar")
    idDoctor = int(input())
    print ("Apellido")
    ape= input()
    print("especialidad")
    espe = input()
    print("salario")
    sal= int(input())
    print("Hospital")
    hosp=int(input())
    reg=servicio.modificarDoctor(idDoctor,ape,espe,sal,hosp)
    print(f"Doctores modificados: {registros}")
print("Fin de programa")