import diseño as linea_menu
import archivos as obAr


def ingresarEstudiante() :
    global mat, total
    linea_menu.linea()
    print("|*-*-*-*-*-*-*-Haz entrado a...*-*-*-*-*-*-*-*|\n"
          "|*-*-Sistema de Ingreso de Estudiantes U.G*-*-|")
    cedula = input("| ---> Ingresa una cedula: ")
    nombre = input("| ---> Ingresa tu nombre completo: ")
    print("| ----> ¿Que carreras quieres elegir?         |")
    print("|   1.- Informatica         100$              |")
    print("|   2.- Marketing           200$              |")
    print("|   3.- Turismo             300$              |")
    print("|   4.- Contabilidad        400$              |")
    carrera = int(input("| ---> Ingresa la carrera a elegir: "))

    if carrera == 1 :
        print("| ---> Elegiste Informatica ")
        carrera = "Informatica"
        mat = 100
        print("Sabias que puedes aplicar a Becas 2022 - 2023")

    if carrera == 2 :
        print("| ---> Elegiste Marketing")
        carrera = "Marketing"
        mat = 200

    if carrera == 3 :
        print("| ---> Elegiste Turismo")
        carrera = "Turismo"
        mat = 300

    if carrera == 4 :
        print("| ---> Elegiste Contablidad")
        carrera = "Contabilidad"
        mat = 400
    linea_menu.linea()
    print("|--- Felicidades, puedes aplicar a Beca UG ---|\n"
          "Dinos tu nota")
    nota = int(input("| ---> Ingresa tu nota: "))

    if nota >= 7 :
        print("|  ¡¡¡¡¡Felicidades aplicas a Beca :DD !!!!!  |")
        print("|  Tu pagar sin incluir beca es " + str(mat) + "  |")
        print("|  Pero tu beca es del 80%                    |")
        desc = mat * 0.80
        print("|  Tu descuento es del " + str(desc))
        subtotal = mat - desc
        print("|  Tu subtotal es " + str(subtotal))
        iva = mat * 0.12
        print("|  El iva 12% separado del descuento por beca" + str(iva))
        total = subtotal + iva
        print("|  Tu total a pagar es del " + str(total))


    else :
        print("No aplicas a Beca")
        mat = total

    obj = (cedula, nombre, carrera, total)
    print("\n**** Se a guardado con exito ****\n")
    linea_menu.linea()
    print("|    Tu cedula es: " + str(obj[0]) + "\n" + "|    Nombre: " + obj[1] + "\n" + "|    Carrera: " + obj[
        2] + "\n" + "|    Total a Pagar: " + str(obj[3]))
    print("|**********************************************|")
    __grabar(obj)


def __grabar(obj) :
    msg = str(obj[0]) + ";" + obj[1] + ";" + obj[2] + ";" + str(obj[3]) + ";\n"
    obAr.crearArchivo("proyecto.csv", msg, "a")


def consulta() :
    cedula = input("Ingresa tu cedula")
    obj = getEstudiante(cedula)
    if obj != None :
        print(obj)
    else :
        print("Cedula no existe!!")


def getEstudiante(cedula) :
    obk = None
    lista = obAr.leerArchivo("proyecto.csv")
    for i in range(len(lista)) :
        if cedula == lista[i][0] :
            obk = lista[i]
            print(obk)
            break
    return obk


def getListar() :
    lista = obAr.leerArchivo("proyecto.csv")
    print("\n *-*-* Vamos a enlistar todos los datos *-*-* \n")
    for i in range(len(lista)) :
        print("---- ----- -----")
        print("--> Cedula: " + lista[i][0] + "\nNombre: " + lista[i][1] + " Carrera: " + lista[i][2] + " Total: " +
              lista[i][3] + "\n")


def eliminar() :
    lista = obAr.leerArchivo("proyecto.csv")
    print("Total de Registros:", len(lista))
    cedula = input("Ingresa tu cedula")
    pos = __getPosicion(cedula, lista)
    if pos != -1 :
        print(lista[pos])
        print("******************************")
        lista.pop(pos)
        msg = ""
        for i in range(len(lista)) :
            msg = msg + str(lista[i][0]) + ";" + lista[i][1] + ";" + lista[i][2] + ";" + lista[i][3] + "\n"
        obAr.crearArchivo("proyecto.csv", msg, "w")
        # print(msg)
        print("Se elimino el registro de la cedula:", cedula)
        print("Longitud :", len(lista))
    else :
        print("No se encontro cedula.")


def __getPosicion(cedula, lista1) :
    pos = -1
    for i in range(len(lista1)) :
        if cedula == lista1[i][0] :
            pos = i
            break
    return pos


def actualizar() :
    lista = obAr.leerArchivo("proyecto.csv")
    print("Longitud :", len(lista))
    cedula = input("Ingrese cedula")
    pos = __getPosicion(cedula, lista)
    if pos != -1 :

        print(lista[pos][1])
        print(lista[pos][2])
        print(lista[pos][3])
        nombre = input("Nombre:")
        carrera = input("Carrera:")
        total = input("total:")
        lista[pos][1] = nombre
        lista[pos][2] = carrera
        lista[pos][3] = total
        op = input("Deseas grabar la info, pon S si lo deseas")
        if op == "S" :
            msg = ""
            for i in range(len(lista)) :
                msg = msg + str(lista[i][0]) + ";" + lista[i][1] + ";" + lista[i][2] + ";" + lista[
                    i][3] + ";\n"
            obAr.crearArchivo("proyecto.csv", msg, "w")
            print("Se grabo exitosamente...")
    else :
        print("No se encontro cedula.")


def ordenamiento() :
    lista = obAr.leerArchivo("proyecto.csv")
    print("\n *-*-* Vamos a enlistar todos los datos *-*-* \n")
    for i in range(len(lista)) :
        print("--> Cedula: " + lista[i][0] + " \nNombre: " + lista[i][1] + " \nCarrera: " + lista[i][2] + " \nTotal: " +
              lista[i][3])


def estadistica() :
    global Infor
    print("Esta es mi sección de Estadistica")
    lista = obAr.leerArchivo("proyecto.csv")
    print("\n *-*-* Ver el mayor número de matriculados por carrera en UG *-*-* \n")
    x = 0
    Infor = 0
    Conta = 0
    Mark = 0
    Turi = 0
    Total_pagar_informatica = 0
    Total_pagar_turismo = 0
    Total_pagar_marketing = 0
    Total_pagar_contabilidad = 0

    for i in range(len(lista)) :
        x = int(lista[i][3]) + x

        if lista[i][2] == "Informatica" :
            Infor = Infor + 1
            Total_pagar_informatica = Total_pagar_informatica + int(lista[i][3])

        if lista[i][2] == "Contabilidad" :
            Conta = Conta + 1
            Total_pagar_contabilidad = Total_pagar_contabilidad + int(lista[i][3])

        if lista[i][2] == "Marketing" :
            Mark = Mark + 1
            Total_pagar_marketing = Total_pagar_marketing + int(lista[i][3])

        if lista[i][2] == "Turismo" :
            Turi = Turi + 1
            Total_pagar_marketing = Total_pagar_turismo + int(lista[i][3])

    print("Total de pagar de Info es", Total_pagar_informatica)
    print("Total de pagar de Mark es" , Total_pagar_marketing)
    print("Total de pagar de Turi es", Total_pagar_turismo)
    print("Total de pagar de Conta es", Total_pagar_contabilidad)