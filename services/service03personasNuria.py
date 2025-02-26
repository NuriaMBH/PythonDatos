from models import personaNuria
#ESTE SERVICIO SERÁ EL QUE TENDRA METODOS
#PARA SER UTILIZADOS EN MAIN
def getSaludo():
    return "Bienvenidoa a Persona Server"

def getPersona1():
    dato = personaNuria.Persona()
    dato.nombre = "Belinda"
    dato.oficio = "Informática"
    dato.edad = 34
    return dato
def getPersona2():
    dato = personaNuria.Persona()
    dato.nombre = "Joselito"
    dato.oficio = "Limpiador"
    dato.edad = 45
    return dato