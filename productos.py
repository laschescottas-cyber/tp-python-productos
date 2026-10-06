productos = []

while True:
    print(".Sistema de gestión de productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoría del producto: ")
        precio = input("Ingrese el precio del producto: ")

        if nombre != "" and categoria != "" and precio.isdigit():
            producto = [nombre, categoria, int(precio)]
            productos.append(producto)
            print("Producto agregado correctamente")
        else:
            print("Datos incorrectos")

    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados")
        else:
            for i in range(len(productos)):
                print(i + 1, productos[i])

    elif opcion == "3":
        buscar = input("Ingrese el nombre del producto: ")

        encontrado = False

        for producto in productos:
            if producto[0] == buscar:
                print(producto)
                encontrado = True

        if encontrado == False:
            print("Producto no encontrado")

    elif opcion == "4":
        if len(productos) == 0:
            print("No hay productos para eliminar")
        else:
            for i in range(len(productos)):
                print(i + 1, productos[i])

            numero = int(input("Ingrese el número del producto a eliminar: "))

            if numero >= 1 and numero <= len(productos):
                productos.pop(numero - 1)
                print("Producto eliminado")
            else:
                print("Número incorrecto")

    elif opcion == "5":
        print("Fin del programa")
        break

    else:
        print("Opción incorrecta")