import time
import random as rand
import os
import json

bahias = {}


def clear():
    os.system("cls")


def validationPlate():
    InpPlate = str(input("Ingese su Placa de Carro\n"))
    InpPlate = InpPlate.upper()
    for i in data:
        print(i)
        print(data[i])
        if InpPlate == i:
            match data[i]["type"]:
                case "vip":
                    print("vip")
                case "discapacitados":
                    print("discapacitados")
                case "emergencia":
                    print("emergencia")
                case "proveedores":
                    print("proveedores")
        else:
            break
    print("Bahía comun")


def readData():
    global data
    with open("car_Plates.json", encoding="utf-8") as f:
        data = json.loads(f.read())
    return print("Lectura de placas realizada correctamente")


def Asig_Bahias():
    for i in range(1, 101):
        if i in range(1, 6):
            bahias[i] = "vip"
        elif i in range(61, 66):
            bahias[i] = "discapacitados"
        elif i in range(80, 83):
            bahias[i] = "emergencia"
        elif i in range(98, 101):
            bahias[i] = "proveedores"
        else:
            bahias[i] = "normal"

    return print("Asignación de Bahías realizada con exito")


def Placeapark(carTipe):
    match carTipe:
        case 1:
            validationPlate()
        # case 2:

        # case 3:

        # case 4:

        # case 5:


def run():
    clear()
    readData()
    Asig_Bahias()
    time.sleep(2)
    clear()
    while True:
        validationPlate()


if __name__ == "__main__":
    run()
