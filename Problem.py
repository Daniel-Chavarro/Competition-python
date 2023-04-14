import time
import random as rand
import os 

diccionario = {}

def Asig_Bahias():
    for i in range(1, 101):
        if i in range(1, 6):
            diccionario[i] = "vip"
        elif i in range(61, 66):
            diccionario[i] = "discapacitados"
        elif i in range(80, 83):
            diccionario[i] = "emergencia"
        elif i in range(98, 101):
            diccionario[i] = "proovedores"
        else:
            diccionario[i] = "normal"
    
    return print("Asignación de Bahías realizada con exito")

def Placeapark(carTipe):
    match carTipe:
        case 1:
        
        case 2:
        
        case 3:
        
        case 4:
        
        case 5:
        


def run():
    os.system("cls")
    Asig_Bahias()
    time.sleep(2)
    carTipe = int(input("Selecciona el tipo de vehiculo: \n 1: VIP \n 2: Discapacitados \n 3: Emergencia \n 4: Proveedores \n 5: Normal \n"))
    Placeapark(carTipe)

if __name__ == "__main__":
    run()