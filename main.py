import json
import mensaje
import admin
import ctrlActions as ctrl
import cliente

def abrirArchivo():
    with open('./movistar.json','r') as abrirArchivo:
        return json.load(abrirArchivo)
    
def guardarArchivo(datos):
    with open('./movistar.json','w') as guardarArchivo:
        json.dump(datos,guardarArchivo)

print(mensaje.menuInicial)
while (True):
    opcion=int(input('-> '))
    match opcion:
        case 1:
            cliente.cliente()
        case 2:
            admin.administrador()
        case _:
            print(mensaje.opcionNoValida)
            ctrl.borrar_pantalla
            break