from models import mascota
#ESTE SERVICIO SERÁ EL QUE TENDRA METODOS
#PARA SER UTILIZADOS EN MAIN
def getSaludo():
    return "Bienvenidoa a SQL Server"

def getMascota1():
    dato = mascota.Mascota()
    dato.nombre = "Amanda"
    dato.raza = "gusano"
    dato.edad = 2
    return dato
def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = "Solito"
    dato.raza = "gato"
    dato.edad = 5
    return dato