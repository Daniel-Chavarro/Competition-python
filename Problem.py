import time
import random as rand
import os
import json

bahias = []


def clear():
    os.system("cls")


def validationPlate():
    InpPlate = str(input("Ingese su Placa de Carro\n"))
    InpPlate = InpPlate.upper()
    for i in data:
        if InpPlate == i:
            match data[i]:
                case "vip":
                    return InpPlate, data[i]
                
                case "discapacitados":
                    return InpPlate, data[i]

                case "emergencia":
                    return InpPlate, data[i]

                case "proveedores":
                    return InpPlate, data[i]
                    
        else:
            continue
    return InpPlate, "normal"


def readData():
    global data
    with open("car_Plates.json", encoding="utf-8") as f:
        data = json.loads(f.read())
    return print("Lectura de placas realizada correctamente")


def Asig_Bahias():
    for i in range(1, 101):
        if i in range(1, 6):
            bahias.append("vip")
        elif i in range(61, 66):
            bahias.append("discapacitados")
        elif i in range(80, 83):
            bahias.append("emergencia")
        elif i in range(98, 101):
            bahias.append("proveedores")
        else:
            bahias.append("normal")

    return print("Asignación de Bahías realizada con exito")




def run():
    clear()
    readData()
    Asig_Bahias()
    time.sleep(2)
    clear()
    while True:
        Cplate, type = validationPlate()
        print(bahias.values())


if __name__ == "__main__":
    run()
