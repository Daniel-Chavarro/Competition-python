import time
import random as rand
import os
import json
import re


regex = r'^[a-zA-Z]{3}\d{3}$'

# Variable listas para las bahias disponibles

Bvip = []
Bdisc = []
Bemer = []
Bprov = []
Bcomm = []

#Variables listas  para las zonas, usa las otras listas
BzoneA = [i for i in (Bvip + Bcomm) if i in range(1,31)]
BzoneB = [i for i in Bcomm if i in range(31,61)]
BzoneC = [i for i in (Bcomm + Bemer + Bdisc + Bprov )if i in range(61,101)]

#Limpia el cmd

def clear():
    os.system("cls")


def validation_AsignationPlate():
    while True:
        InpPlate = str(input(f"Ingese su Placa de Carro\n"))
        if re.match(regex, InpPlate):
            break
        else:
            print("La placa no es válida")
            continue
    
    InpPlate = InpPlate.upper()
    for i in data:
        if InpPlate == i:
            match data[i]:
                case "vip":
                    if len(Bvip) != 0:
                        placeP = rand.choice(Bvip)
                        Bvip.remove(placeP)
                    else:
                        placeP = min(Bcomm)
                        Bcomm.remove(placeP)

                    return InpPlate, data[i], placeP
                case "discapacitados":
                    if len(Bdisc) != 0:
                        placeP = rand.choice(Bdisc)
                        Bdisc.remove(placeP)
                        return InpPlate, data[i], placeP
                    else:
                        if len(Bdisc) != 0:
                            placeP = rand.choice(Bdisc)
                            Bdisc.remove(placeP)
                        else:
                            maxnumLastb = max([i for i in Bcomm if i in range(66, 80)])
                            minumNextb = min([i for i in Bcomm if i in range(83,98)])
                            if (80-maxnumLastb) < (minumNextb-82):
                                placeP = maxnumLastb
                                Bcomm.remove(placeP)
                            else:
                                placeP = minumNextb
                                Bcomm.remove(placeP)

                case "emergencia":
                    if len(Bemer) != 0:
                        placeP = rand.choice(Bemer)
                        Bemer.remove(placeP)
                    else:
                        maxnumLastb = max([i for i in Bcomm if i in range(6, 61)])
                        minumNextb = min([i for i in Bcomm if i in range(66,80)])
                        if (80-maxnumLastb) < (minumNextb-82):
                            placeP = maxnumLastb
                            Bcomm.remove(placeP)
                        else:
                            placeP = minumNextb
                            Bcomm.remove(placeP)

                    return InpPlate, data[i], placeP

                case "proveedores":
                    if len(Bprov) != 0:
                        placeP = rand.choice(Bprov)
                        Bprov.remove(placeP)
                    else:
                        placeP = max(Bcomm)
                        Bcomm.remove(placeP)

                    return InpPlate, data[i], placeP

        else:
            continue

    if len(Bcomm) != 0:
        placeP = rand.choice(Bcomm)
        Bcomm.remove(placeP)
        return InpPlate, "normal", placeP


def readData():
    global data
    with open("car_Plates.json", encoding="utf-8") as f:
        data = json.loads(f.read())
    return print("Lectura de placas realizada correctamente")


def Asig_Bahias():
    for i in range(1, 101):
        if i in range(1, 6):
            Bvip.append(i)
        elif i in range(61, 66):
            Bdisc.append(i)
        elif i in range(80, 83):
            Bemer.append(i)
        elif i in range(98, 101):
            Bprov.append(i)
        else:
            Bcomm.append(i)

    return print("Asignación de Bahías realizada con exito")


def run():
    clear()
    readData()
    Asig_Bahias() 
    time.sleep(2)
    clear()
    while True:
        register = int(input("0: Ingresar al parqueadero \n1: Salir del parqueadero \n Ingrese el numero \n"))
        match register:
            case 0:
                BzoneA = [i for i in (Bvip + Bcomm) if i in range(1,31)]
                BzoneB = [i for i in Bcomm if i in range(31,61)]
                BzoneC = [i for i in (Bcomm + Bemer + Bdisc + Bprov )if i in range(61,101)]
                print(f"""
                        {len(Bvip)} Bahias vip dispoibles                                   
                        {len(Bdisc)} Bahías discapacitados disponibles                      {len(BzoneA)} Bahias disponibles en zona A
                        {len(Bemer)} Bahías emergecia disponibles                           {len(BzoneB)} Bahias disponibles en zona B
                        {len(Bprov)} Bahias proveedores disponibles                         {len(BzoneC)} Bahias disponibles en zona C
                        {len(Bcomm)} Bahias comunes disponibles
                        
                        {len(BzoneA+BzoneB+BzoneC)} Bahias en Total
                        """)                       
                
                Cplate, type, place = validation_AsignationPlate()
                clear()
                print(f"{Cplate}\nBahía {type}\nBahía número {place}")
            case 1:
                


if __name__ == "__main__":
    run()
