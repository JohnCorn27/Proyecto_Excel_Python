def crearArchivo(nombre, contenido, modo) :
    archivo = open(nombre, modo)
    archivo.write(contenido)
    archivo.close()

def leerArchivo(nombre):
    archivo = open(nombre, "r")
    lista = []
    for linea in archivo.readlines():
        tupla= linea.split(';')
        obj = [tupla[0], tupla[1], tupla[2],(tupla[3])]
        lista.append(obj)
        archivo.close()
    return lista

