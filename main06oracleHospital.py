from models import hospital as model
from services import service06oraclehospital as service### como se llama el fichero den service

servicio = service.ServiceOracleHospital()###como se llama la clase, la cual esta dentro del fichero de service
hospitales = servicio.getAllHospital ()
for doc in hospitales:
    print(f"{doc.idhospital}{doc.nombre},{doc.direccion},{doc.numCama}")
    
print("1.-Insertar Hospital")
print("2.-Eliminar hospital")
print("3.- Modificar hospital")
print("Selecciones una opción")
opcion=int(input())
if (opcion ==1):
    print("ID DEL HOSPITAL")
    idhospital = int(input())
    print ("nombre")
    nom= input()
    print("direccion")
    dir = input()
    print("telefono")
    sal= int(input())
    print("numCama")
    hosp=int(input())
    reg= servicio.insertarHospital(idhospital,nom,dir,telf,cam)
    print(f"Hospitales insertados:{reg}")
elif (opcion==2):
    print("Introduzca ID a eliminar")
    idhospital= int(input())
    registros = servicio.eliminarHospital(idhospital)
    print(f"Hospitales eliminados: {registros}")
elif(opcion==3):
    print("Id del hospital modificar")
    idhospital = int(input())
    print ("nombre")
    nom= input()
    print("direccion")
    dir = input()
    print("telefono")
    telf= int(input())
    print("Hospital")
    hosp=int(input())
    reg=servicio.modificarHospital(idhospital,nom,dir,telf,cam)
print(f"Hospitales modificados: {registros}")
print("Fin de programa")