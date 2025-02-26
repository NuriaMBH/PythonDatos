from services import service03personasNuria as service
from models import personaNuria


saludo= service.getSaludo()

print ("Todo ok," + saludo)
#nombre de varibale persona1, persona2
persona1 = service.getPersona1()
persona2 = service.getPersona2()
print(persona1.nombre)
print(persona2.nombre)
