from services import service02prueba as service
from models import mascota


saludo= service.getSaludo()

print ("Todo ok," + saludo)
perro = service.getMascota1()
pez = service.getMascota2()
print(perro.nombre)
print(pez.nombre)
