def validarFormato(patente):
    if (len(patente))==6 and patente[0].isalpha() and patente[1].isalpha and patente[2].isalnum() and patente[3].isalnum() and patente[4].isnumeric() and patente[5].isnumeric():
        return True
    else:
        return False

def agregar(automotora):
    patente = ""
    while validarFormato(patente) == False:
        patente = input("Ingrese la patente: ")

    marca = input("Ingrese la marca: ")
    year = validarYear()
    precio = validarPrecio()

    dic = {"patente":patente,
           "marca":marca,
           "año":year,
           "precio":precio}
    automotora.append(dic)

def buscar(automotora, patente):
    pos = -1
    for i in range(len(automotora)):
        if automotora[i]['patente']==patente:
            pos = i
            break
    return pos

def mostrarAuto(automotora):
    patente = input("Ingrese la patente a buscar: ")
    ubicacion = buscar(automotora, patente)
    if (ubicacion >= 0):
        print("Vehiculo Encontrado")
        print(f"Patente: {automotora[ubicacion]['patente']}")
        print(f"Año: {automotora[ubicacion]['año']}")
        print(f"Marca: {automotora[ubicacion]['marca']}")
        print(f"Precio: {automotora[ubicacion]['precio']}")
    else:
        print("No existe esa patente")


def eliminar(automotora):
    patente = input("Ingrese la patente a borrar: ")
    ubicacion = buscar(automotora,patente)
    if ubicacion >= 0:
        print("Vehiculo Encontrado")
        automotora.pop(ubicacion)
    else:
        print("NO existe esa patente")

def listar(automotora):
    print("AUTOMOTORA")
    print("-------------------------------------")
    print("Patente\t\tMarca\t\tAño\t\tPrecio")
    print("-------------------------------------")
    for i in range(len(automotora)):
        print(f"{automotora[i]['patente']}\t\t{automotora[i]['marca']}\t\t{automotora[i]['año']}\t\t{automotora[i]['precio']}")
    print("-------------------------------------")


def valorizar(automotora):
    acum = 0
    for i in range(len(automotora)):
        acum = acum + automotora[i]['precio'] + (automotora[i]['precio'] * 0.19)
    return acum

def validarOpc():
    while True:
        try:
            opc = int(input("Ingrese su opcion: "))
            if opc > 0 and opc <=6:
                break
        except ValueError:
            print("no valido")
    return opc

def validarYear():
    while True:
        try:
            year = int(input("Ingrese el año del vehiculo"))
            if year > 1989 and year < 2027:
                break
        except ValueError:
            print("no valido")
    return year

def validarPrecio():
    while True:
        try:
            precio = int(input("ingrese el precio: "))
            if precio > 0:
                break
        except ValueError:
            print("no valido")
    return precio
    

def mostrarMenu():
    automotora=[]
    while True:
        print("MENU AUTOMOTORA")
        print("1.- Agregar Vehiculo")
        print("2.- Mostrar un Vehiculo")
        print("3.- Eliminar Vehiculo")
        print("4.- Listar Taller")
        print("5.- Valorizar Taller")
        print("6.- Salir")
        opc=int(input("Ingrese su opción :"))
        if(opc==1):
             agregar(automotora)
        elif(opc==2):
            mostrarAuto(automotora)
        elif(opc==3):
            eliminar(automotora)
        elif(opc==4):
            listar(automotora)
        elif(opc==5):
            res = int(valorizar(automotora))
            print(f"Valorizacion: {res}")
        elif(opc==6):
            print("Fin de programa")
            break

mostrarMenu()
 








