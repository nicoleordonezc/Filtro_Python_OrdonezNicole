import json
import mensaje
import ctrlActions as ctrl

def abrirArchivo():
    with open('./movistar.json','r') as abrirArchivo:
        return json.load(abrirArchivo)
    
def guardarArchivo(datos):
    with open('./movistar.json','w') as guardarArchivo:
        json.dump(datos,guardarArchivo)


                                        

def administrador():
    while (True):
        ctrl.borrar_pantalla
        print(mensaje.menuAdministrador)
        opcion=int(input('-> '))
        match opcion:
            case 1:
                while(True):
                    ctrl.borrar_pantalla

                    datos=abrirArchivo()
                    print(mensaje.cliente)
                    opcion=int(input('-> '))
                    match opcion:
                        case 1:
                            listaTemporal= datos["clientes"]
                            cantidadClientes=len(listaTemporal)
                            nombres=input('Ingrese los nombres del cliente nuevo: ')
                            direccion=input('Ingrese la direccion del cliente nuevo: ')
                            contacto=input('Ingrese el contacto del cliente nuevo: ')
                            plan=input('Ingrese el plan del cliente nuevo: ')
                            clienteNuevo={"id":cantidadClientes+1,
            "nombre":nombres,
            "direccion":direccion,
            "contacto": contacto,
            "plan": [plan],
            "categoria":"Nuevo",
            "registro":[plan],
            "reclamos":[{"pregunta":[], "queja":[]}],
            "tiempo_afiliado":0}
                            listaTemporal.append(clienteNuevo)
                            datos["clientes"] = listaTemporal
                            print('EL cliente fue ingresado correctamente')
                            guardarArchivo(datos)
                        case 2:        
                            ctrl.borrar_pantalla
                            print(mensaje.actDatos)
                            opcion=int(input('-> '))
                            id_cliente=int(input('Ingrese el ID del cliente: '))
                            for clientes in datos['clientes']:
                                if clientes["id"]==id_cliente:
                                    match opcion:
                                        case 1:
                                            nombreNuevo=input('Ingrese los nuevos nombres: ')
                                            clientes["nombre"]=nombreNuevo
                                            print(mensaje.opcionValida)
                                            guardarArchivo(datos)
                                        case 2:
                                            direccionNuevo=input('Ingrese la nueva direccion: ')
                                            clientes["direccion"]=direccionNuevo
                                            print(mensaje.opcionValida)
                                            guardarArchivo(datos)
                                        case 3:
                                            contactoNuevo=input('Ingrese el nuevo contacto: ')
                                            clientes["contacto"]=contactoNuevo
                                            print(mensaje.opcionValida)
                                            guardarArchivo(datos)
                                        case 4:
                                            planNuevo=input('Ingrese el nuevo: ')
                                            clientes["plan"]=planNuevo
                                            clientes["registro"].append(planNuevo)
                                            print(mensaje.opcionValida)
                                            guardarArchivo(datos)
                                        case 5:
                                            break              
                                        case _:
                                            print(mensaje.opcionNoValida)
                                                
                        case 3:
                            id_cliente=int(input('Ingrese el ID del cliente: '))
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
                        case 4:
                            break
            case 2:
                datos=abrirArchivo()
                id_cliente=int(input('Ingrese el ID del cliente: '))
                for clientes in datos['clientes']:
                    if clientes["id"]==id_cliente:
                        print(clientes['reclamos'])
            case 3:
                datos=abrirArchivo()
                print(mensaje.reportes)
                opcion=int(input('-> '))
                match opcion:
                    case 1:
                        id_cliente=int(input('Ingrese el ID del cliente: '))
                        for clientes in datos['clientes']:
                            if clientes["id"]==id_cliente:
                                print(clientes['registro'])
                    case 2:
                        id_cliente=int(input('Ingrese el ID del cliente: '))
                        for clientes in datos['clientes']:
                            if clientes["id"]==id_cliente:
                                if clientes["tiempo_afiliado"]>=6:
                                    print('El usuario es leal')                      
                                else:
                                    print('El usuario no es leal')       
                    case 3:
                        for servicios in datos['servicios']:
                            print(servicios)
                    case 4:
                        plan=(input('Ingrese el plan que desea ver: '))
                        for servicios in datos['clientes']:
                            if servicios["plan"]==plan:
                                n=servicios["plan"]
                                cantidad=len(n)
                                print(cantidad)
                    case 5:
                        id_cliente=int(input('Ingrese el ID del cliente: '))
                        for clientes in datos['clientes']:
                            if clientes["id"]==id_cliente:
                                n=clientes["registro"]
                                cantidadProducto=len(n)
                                print('Cantidad de productos ofrecidos: ')
                                print(cantidadProducto)
                    case 6:
                        break
                    case _:
                        print(mensaje.opcionNoValida)
                        ctrl.pausar_pantalla
            case 4:
                datos=abrirArchivo()
                print(mensaje.servicios)
                opcion=int(input('-> '))
                match opcion:
                    case 1:
                        nombre=input('Ingrese el nombre del nuevo servicio: ')
                        descripcion=input('Ingrese la descripcion del nuevo servicio: ')
                        valor=int(input('Ingrese el valor del nuevo servicio: '))
                        nuevoServicio={"nombre":nombre, "valor": valor,"descripcion":descripcion }
                        print(mensaje.opcionValida)
                        datos['servicios'].append(nuevoServicio)
                        guardarArchivo(datos)
                    case 2:
                        print(mensaje.actServicio)
                        opcion=int(input('-> '))
                        match opcion:
                            case 1:
                                servicio=(input('Ingrese el nombre del servicio: '))
                                for servicios in datos['servicios']:
                                    if servicios["nombre"]==servicio:
                                        valor=int(input('Ingrese el nuevo valor: '))
                                        print(mensaje.opcionValida)
                                        datos['servicios']['valor']=valor
                                        guardarArchivo(datos)
                            case 2:
                                servicio=(input('Ingrese el nombre del servicio: '))
                                for servicios in datos['servicios']:
                                    if servicios["nombre"]==servicio:
                                        descripcion=(input('Ingrese el nuevo valor: '))
                                        print(mensaje.opcionValida)
                                        datos['servicios']['descipcion']=descripcion
                                        guardarArchivo(datos)
                            case 3:
                                break
                            case _:
                                print(mensaje.opcionNoValida)
                                ctrl.pausar_pantalla
                    case 3:
                        servicio=(input('Ingrese el nombre del servicio: '))
                        for servicios in datos['servicios']:
                            if servicios["nombre"]==servicio:
                                print(f'Valor: {servicios["valor"]}\nDescripcion: {servicios["descripcion"]}')
                    case _:
                        print(mensaje.opcionNoValida)
                        ctrl.pausar_pantalla
            case 5:
                break
            case _:
                print(mensaje.opcionNoValida)
                ctrl.pausar_pantalla

