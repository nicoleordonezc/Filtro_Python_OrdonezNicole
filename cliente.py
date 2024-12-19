import json
import ctrlActions as ctrl
import mensaje

def abrirArchivo():
    with open('./movistar.json','r') as abrirArchivo:
        return json.load(abrirArchivo)
    
def guardarArchivo(datos):
    with open('./movistar.json','w') as guardarArchivo:
        json.dump(datos,guardarArchivo)

def cliente():
    while(True):
        datos=abrirArchivo()
        print(mensaje.menuCliente)
        opcion=int(input('-> '))
        match opcion:
            case 1:
                id_cliente=int(input('Ingrese su ID: '))
                for clientes in datos['clientes']:
                    if clientes["id"]==id_cliente: 
                        for clientes in datos['clientes']:
                            if clientes["tiempo_afiliado"]==0:
                                clientes["categoria"]="Nuevo"
                            elif clientes["tiempo_afiliado"]>=6:
                                clientes["categoria"]="Regular"
                            else:
                                clientes["categoria"]="leal"
                                guardarArchivo(clientes)
                            if clientes["id"]==id_cliente:                                   
                                print(f'Nombres: {clientes["nombre"]}\nDireccion: {clientes["direccion"]}\nContacto: {clientes["contacto"]}\nPlan: {clientes["plan"]}\nCategoria: {clientes["categoria"]}\nTiempo afiliado: {clientes["tiempo_afiliado"]} meses')
                        break               
            case 2:
                id_cliente=int(input('Ingrese su ID: '))
                for clientes in datos['clientes']:
                    if clientes["id"]==id_cliente: 
                        print(mensaje.preguntaQueja)
                        opcion=int(input('-> '))
                        match opcion:
                            case 1:
                                pregunta=input('Cual es tu pregunta: ')
                                print('Pronto te daremos respuesta')                             
                                clientes['reclamos'].append(pregunta)
                                guardarArchivo(datos)
                            case 2:
                                queja=input('Cual es tu queja: ')
                                print('Pronto te daremos respuesta')                   
                                clientes['reclamos'].append(queja)
                                guardarArchivo(datos)
                            case 3:
                                break
                            case _:
                                print(mensaje.opcionNoValida)
                                ctrl.pausar_pantalla
            case 3:
                break
            case _:
                print(mensaje.opcionNoValida)
                ctrl.borrar_pantalla