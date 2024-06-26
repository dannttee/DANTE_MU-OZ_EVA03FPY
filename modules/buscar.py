import json
def buscar(dato, jsonf):
   
   if not jsonf.exist():
      print('la base de datos no existe\n')
    elif jsonf.stat().st_size == 0:
     print('la base de datos esta vacia \n')
    else: with open(jsonf, mode )
