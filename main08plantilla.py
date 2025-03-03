#from services import service08mysqlplantilla as service
#from services import Service08oracleplantilla as service
from services import service08sqlserverplantilla as service
from models.plantilla import Plantilla

servicio = service.ServiceSqlServerPlantilla()
plntillas = servicio.getPlantilla()
for PLANTILLA in Plantilla:
    print(f"Apellido: {PLANTILLA.apellido}, funcion: {PLANTILLA.funcion}, salario: {PLANTILLA.salario},hospital: {PLANTILLA.hospital}")
