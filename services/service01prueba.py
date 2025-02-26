from models import mascota
#ESTE SERVICIO SERÁ EL QUE TENDRA METODOS
#PARA SER UTILIZADOS EN MAIN
def getSaludo():
    return "Bienvenidoa Matrix"

def getMascota1():
    dato = mascota.Mascota()
    dato.nombre = "Chilli"
    dato.raza = "perro"
    dato.edad = 2
    return dato
def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = "River"
    dato.raza = "pez"
    dato.edad = 5
    return dato