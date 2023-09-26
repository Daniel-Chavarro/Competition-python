import time
import random as rand
import os
import json
import re



# Contador para el tiempo total según zonas

TimeA = 0
TimeB = 0
TimeC = 0

# Contador para el dinero recolectado por las tarifas

Counter_money = 0

# Contadores para el numero de vehiculos que ingresaron según el tipo de bahía

Counter_Vip = 0
Counter_Disc = 0
Counter_Emer = 0
Counter_Prov = 0
Counter_Comm = 0

# Contadores para el numero de vehiculos que ingresaron según la zona

Counter_zoneA = 0
Counter_zoneB = 0
Counter_zoneC = 0

regex = r'^[a-zA-Z]{3}\d{3}$'

Bused = {}

# Variable listas para las bahias disponibles

Bvip = []
Bdisc = []
Bemer = []
Bprov = []
Bcomm = []


# Variables listas  para las zonas, usa las otras listas
BzoneA = [i for i in (Bvip + Bcomm) if i in range(1, 31)]
BzoneB = [i for i in Bcomm if i in range(31, 61)]
BzoneC = [i for i in (Bcomm + Bemer + Bdisc + Bprov)if i in range(61, 101)]

# Limpia el cmd


def clear():
    os.system("cls")


def validation_AsignationPlate():
    global Counter_Comm, Counter_Disc, Counter_Emer, Counter_Prov, Counter_Vip

    while True:
        InpPlate = str(input(
            f"Ingese su Placa de Carro. En caso de haber dado por error, digitar 0:\n"))
        if re.match(regex, InpPlate):
            InpPlate = InpPlate.upper()
            if InpPlate in Bused:
                print("La placa ya esta registrada")
                continue
            else:
                break
        elif InpPlate == "0":
            return False, False, False
        else:
            print("La placa no es válida")
            continue

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

                    Counter_Vip += 1
                    return InpPlate, data[i], placeP
                case "discapacitados":
                    if len(Bdisc) != 0:
                        placeP = rand.choice(Bdisc)
                        Bdisc.remove(placeP)

                    else:
                        if len(Bdisc) != 0:
                            placeP = rand.choice(Bdisc)
                            Bdisc.remove(placeP)
                        else:
                            maxnumLastb = max(
                                [i for i in Bcomm if i in range(1, 80)])
                            minumNextb = min(
                                [i for i in Bcomm if i in range(83, 98)])
                            if (80-maxnumLastb) < (minumNextb-82):
                                placeP = maxnumLastb
                                Bcomm.remove(placeP)
                            else:
                                placeP = minumNextb
                                Bcomm.remove(placeP)

                    Counter_Disc += 1
                    return InpPlate, data[i], placeP

                case "emergencia":
                    if len(Bemer) != 0:
                        placeP = rand.choice(Bemer)
                        Bemer.remove(placeP)
                    else:
                        maxnumLastb = max(
                            [i for i in Bcomm if i in range(1, 61)])
                        minumNextb = min(
                            [i for i in Bcomm if i in range(66, 98)])
                        if (80-maxnumLastb) < (minumNextb-82):
                            placeP = maxnumLastb
                            Bcomm.remove(placeP)
                        else:
                            placeP = minumNextb
                            Bcomm.remove(placeP)

                    Counter_Emer += 1
                    return InpPlate, data[i], placeP

                case "proveedores":
                    if len(Bprov) != 0:
                        placeP = rand.choice(Bprov)
                        Bprov.remove(placeP)
                    else:
                        placeP = max(Bcomm)
                        Bcomm.remove(placeP)

                    Counter_Prov += 1
                    return InpPlate, data[i], placeP

        else:
            continue

    if len(Bcomm) != 0:
        placeP = rand.choice(Bcomm)
        Bcomm.remove(placeP)
        Counter_Comm += 1
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
    global Counter_zoneA, Counter_zoneB, Counter_zoneC, Counter_money, TimeA, TimeB, TimeC
    clear()
    readData()
    Asig_Bahias()
    time.sleep(2)
    clear()
    while True:
        register = str(input(
            "0: Ingresar al parqueadero \n1: Salir del parqueadero \n2: Finalizar parqueadero y entregar informe \nIngrese el numero \n"))
        if register == "0":
            if len(Bcomm+Bdisc+Bvip+Bprov+Bemer) == 0:
                clear()
                print("El parqueadero esta lleno, no puedes ingresar")
                continue

            BzoneA = [i for i in (Bvip + Bcomm) if i in range(1, 31)]
            BzoneB = [i for i in Bcomm if i in range(31, 61)]
            BzoneC = [i for i in (Bcomm + Bemer + Bdisc +
                                  Bprov)if i in range(61, 101)]
            print(f"""
                    {len(Bvip)} Bahias vip dispoibles                                   
                    {len(Bdisc)} Bahías discapacitados disponibles                      {len(BzoneA)} Bahias disponibles en zona A
                    {len(Bemer)} Bahías emergecia disponibles                           {len(BzoneB)} Bahias disponibles en zona B
                    {len(Bprov)} Bahias proveedores disponibles                         {len(BzoneC)} Bahias disponibles en zona C
                    {len(Bcomm)} Bahias comunes disponibles
                    
                    {len(BzoneA+BzoneB+BzoneC)} Bahias en Total
                    """)

            Cplate, type, place = validation_AsignationPlate()
            if (Cplate and type and place) == False:
                clear()
                continue
            else:
                if place in BzoneA:
                    zone = "A"
                    Counter_zoneA += 1
                elif place in BzoneB:
                    zone = "B"
                    Counter_zoneB += 1
                elif place in BzoneC:
                    zone = "C"
                    Counter_zoneC += 1
                clear()
                print(f"{Cplate}\nBahía {type}\nZona {zone} \nBahía número {place}")

            Bused[Cplate] = {"num_bahia": place,
                             "type_bahia": type,
                             "time_arrived": time.time()}

        # Salida del parqueadero

        elif register == "1":
            clear()
            while True:

                # Validacion formato

                Cplate = input("Ingrese su placa de carro: \n")
                if re.match(regex, Cplate):
                    Cplate = Cplate.upper()
                    break
                else:
                    clear()
                    print("La placa no es válida")
                    continue

            # Elimina la bahia en el diccionario usado y lo vouelve a agregar a la lista segun el tipo

            if Cplate in Bused:
                match Bused[Cplate]["type_bahia"]:
                    case 'vip':
                        Bvip.append(Bused[Cplate]["num_bahia"])
                        Bvip.sort()
                    case "discapacitados":
                        Bdisc.append(Bused[Cplate]["num_bahia"])
                        Bdisc.sort()
                    case "emergencia":
                        Bemer.append(Bused[Cplate]["num_bahia"])
                        Bemer.sort()
                    case "proveedores":
                        Bprov.append(Bused[Cplate]["num_bahia"])
                        Bprov.sort()

                        time_arrived = Bused[Cplate]["time_arrived"]
                        time_exit = time.time()
                        time_total = time_exit - time_arrived
                        minutes_total = time_total / 60
                        if round(int(minutes_total)) > 30:
                            print(
                                f"Gracias por usar el Parqueadero, el tiempo de uso fue {round(int(minutes_total))} Minutos, Debe pagar una tarifa de $5000 Pesos")
                            Counter_money += 5000
                        else:
                            print(
                                f"Gracias por usar el Parqueadero, el tiempo de uso fue {round(int(minutes_total))} Horas")

                    case "normal":
                        Bcomm.append(Bused[Cplate]["num_bahia"])
                        Bcomm.sort()

                # Recoleccion de tiempo y Conversion de tiempo

                time_arrived = Bused[Cplate]["time_arrived"]
                time_exit = time.time()
                time_total = time_exit - time_arrived
                hours_total = time_total / 3600

                # Sumandole a los contadores segun el tipo de zona

                if Bused[Cplate]["num_bahia"] in range(1, 31):
                    TimeA += hours_total
                elif Bused[Cplate]["num_bahia"] in range(31, 61):
                    TimeB += hours_total
                elif Bused[Cplate]["num_bahia"] in range(61, 101):
                    TimeC += hours_total

                del Bused[Cplate]

                clear()
                print(
                    f"Gracias por usar el Parqueadero, el tiempo de uso fue {round(hours_total, 2)} Horas")
            else:
                clear()
                print(f"La placa ingresada no se encuentra registrada.")

        # Opcion Finalizar y entregar informe

        elif register == "2":
            password = str(input("Ingrese la contraseña:"))
            if password == "^@3fXn%V#92oJAD2":
                clear()
                print(f"""
                Resultados Día de hoy:
                Total ingresados por tipo de Bahía:
                {Counter_Comm} Commun
                {Counter_Disc} Discapacitados
                {Counter_Emer} Emergencia
                {Counter_Prov} Proveedores
                {Counter_Vip} Vip
                
                Total Ingresos por Zona:
                {Counter_zoneA} Zona A
                {Counter_zoneB} Zona B
                {Counter_zoneC} Zona C

                Dinero Recolectado por tarifa de poveedores: ${Counter_money} Pesos
                ${Counter_money/2} Pesos para Mejoramiento de parqueadero
                ${Counter_money/2} Pesos para Promocion de Estudiantes

                Tiempo segun la zona:
                {TimeA} Horas en la zona A
                {TimeB} Horas en la zona B
                {TimeC} Horas en la zona C
                """)

                time.sleep(60)
                break
            else:
                clear()
                print("Contraseña invalida")

        else:
            clear()
            print("Solo puede poner una de las dos opciones actuales")


if __name__ == "__main__":
    run()
