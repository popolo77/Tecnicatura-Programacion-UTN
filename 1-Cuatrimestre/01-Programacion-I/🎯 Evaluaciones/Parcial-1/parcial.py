herramientas = []
existencias = []

op = 0

while op != 8:
    print("1- Carga Inicial de Herramientas ")
    print("2- Carga de existencias")
    print("3- Visualizar inventario")
    print("4- Consulta de stock")
    print("5- Reporte de Agotados")
    print("6- Alta de Nuevo Producto")
    print("7- Actualizar stock")
    print("8- Salir")

    op = int(input("Ingrese una opción: "))

    if op == 1: #En la opción 1 se cargan las herramientas validando que no estén vacías ni repetidas.
        cant = int(input("Ingrese la cantidad de herramientas a cargar: "))

        for i in range(cant):
            nombre = input("Ingrese nombre de herramienta: ")
            while nombre == "" or nombre in herramientas:
                print("Error - Nombre vacio o repetido")
                nombre = input("Ingrese nombre de herramienta: ")

            herramientas.append(nombre)

    elif op == 2: #En la opción 2 se cargan las existencias, validando que no sean negativas.
        existencias = []
        for i in herramientas:
            print(f"Herramienta: {i}")
            stock = int(input("Ingrese existencia: "))
            while stock < 0:
                print("Error - Ingrese un número valido")
                stock = int(input("Ingrese existencia: "))
            existencias.append(stock)

    elif op == 3:#En la opción 3 se muestra el inventario recorriendo ambas listas con el mismo índice.
        if len(herramientas) == 0 or len(existencias) == 0:
            print("Error - Debe cargar datos primero")
        else:
            for i in range(len(herramientas)):
                print(f"{herramientas[i]} stock: {existencias[i]}")

    elif op == 4:#En la opción 4 se consulta el stock buscando la herramienta y obteniendo su posición con index.
        buscar = input("Ingrese nombre de herramienta a buscar: ")
        if buscar in herramientas:
            pos = herramientas.index(buscar)

            if existencias[pos] == 0:
                print("No hay stock")
            else:
                print(f"Stock: {existencias[pos]}")
        else:
            print("No existe stock creado de esa herramienta")

    elif op == 5:#En la opción 5 se muestran los productos sin stock.
        for x in range(len(herramientas)):
            if existencias[x] == 0:
                print(f"No hay stock de {herramientas[x]}")

    elif op == 6:#En la opción 6 se permite agregar un nuevo producto con sus validaciones correspondientes.
        nuevo_prod = input("Ingrese nombre del nuevo producto: ")
        while nuevo_prod == "" or nuevo_prod in herramientas:
            print("Error - Nombre vacio o repetido")
            nuevo_prod = input("Ingrese nombre del nuevo producto: ")

        nuevo_stock = int(input("Ingrese la cantidad: "))
        while nuevo_stock < 0:
            print("Error - Número invalido")
            nuevo_stock = int(input("Ingrese la cantidad: "))

        herramientas.append(nuevo_prod)
        existencias.append(nuevo_stock)

    elif op == 7:
        actuali_nombre = input("Ingrese nombre de herramienta: ")

        if actuali_nombre in herramientas:
            actuali_pos = herramientas.index(actuali_nombre)

            actuali_op = int(input("Ingrese 1 - Actualización por Venta ó 2 - Actualización por Ingreso: "))

            actuali_cant = int(input("Ingrese la cantidad: "))

            while actuali_cant < 0:
                print("Error - Número invalido")
                actuali_cant = int(input("Ingrese la cantidad: "))

            if actuali_op == 1:
                if actuali_cant > existencias[actuali_pos]:
                    print("Error - Stock insuficiente")
                else:
                    existencias[actuali_pos] -= actuali_cant

            elif actuali_op == 2:
                existencias[actuali_pos] += actuali_cant

            else:
                print("Opción inválida")
        else:
            print("La herramienta no existe")

    





            







