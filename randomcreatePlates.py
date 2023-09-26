import os
import json
import random as rand
import time

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
lenght = 3
types = ["vip", "discapacitados", "emergencia", "proveedores"]

dictionary = {}


def randomizer():
    for i in range(0,321):
        word = rand.sample(letters,lenght)
        Fnumber = rand.sample(numbers,lenght)
        typerandom = rand.sample(types,1)
        typecar = "".join(typerandom)
        plate = "".join(word) + "".join(Fnumber)
        dictionary[plate] = typecar





def run():
    os.system("cls")
    randomizer()
    with open("Car_plates.json", "w" , encoding="utf-8") as f:
        json.dump(dictionary,f, indent=4)
    os.system("cls")
    print("Creacion de placas aleatorias completadas, terminando programa en 3 segundos")
    time.sleep(3)

if __name__ == "__main__":
    run()
