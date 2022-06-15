#Importamos Diseño para poder imprimir el menu por pantalla
import diseño as linea_menu
#Aqui traemos las funciones a usar para crear, leer, actualizar y eliminar usuario
import modulo as objMo


#Traemos la función linea de diseño para imprimir el diseño
linea_menu.menu()

def inicio():
# En este input vamos a elegir la opción a usar
    opc = int(input("| ---> Ingresa una opción: "))

#Aqui estan las funciones a usar para el proyecto
    if opc ==1:
        objMo.ingresarEstudiante()
#Para consultar los datos ingresando la cedula
    if opc ==2:
        objMo.consulta()
#Para eliminar datos ingresando la cedula
    if opc ==4:
        objMo.eliminar()
#Para actualizar solo ingresando la cedula
    if opc ==3:
        objMo.actualizar()
#Consulta toda la lista en el excel
    if opc ==6:
        objMo.getListar()
#Permitira Ordenar los datos
    if opc ==5:
        objMo.ordenamiento()
#Permitira ver los datos por estadistica
    if opc ==7:
        objMo.estadistica()

#Sale del programa
    if opc ==8:
        print("Gracias")

inicio()