import time
import random as rand
import os
import json

bahias = {}


def clear():
    os.system("cls")

def validationPlate(data):
    InpPlate = str(input("Ingese su Placa de Carro\n"))
    InpPlate = InpPlate.upper()
    

def readData():
    with open("car_Plates.json", encoding="utf-8") as f:
        data = json.loads(f.read())
    return print("Lectura de placas realizada correctamente"), data


def Asig_Bahias():
    for i in range(1, 101):
        if i in range(1, 6):
            bahias[i] = "vip"
        elif i in range(61, 66):
            bahias[i] = "discapacitados"
        elif i in range(80, 83):
            bahias[i] = "emergencia"
        elif i in range(98, 101):
            bahias[i] = "proovedores"
        else:
            bahias[i] = "normal"

    return print("Asignación de Bahías realizada con exito")


def Placeapark(carTipe, data):
    match carTipe:
        case 1:
            validationPlate(data)
        # case 2:

        # case 3:

        # case 4:

        # case 5:


def run():
    clear()
    Asig_Bahias()
    data = readData()
    time.sleep(2)
    clear()
    while True:
        carTipe = int(input(
            "Selecciona el tipo de vehiculo: \n 1: VIP \n 2: Discapacitados \n 3: Emergencia \n 4: Proveedores \n 5: Normal \n"))
        clear()
        Placeapark(carTipe, data)


if __name__ == "__main__":
    run()
