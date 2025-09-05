import figuras

def menu():
    print("\n📐 Calculadora de Geometría Básica")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")
    print("5. Salir")

while True:
    menu()
    opcion = input("Elige una figura: ")

    if opcion == "1":
        lado = float(input("Lado: "))
        print("Área:", figuras.area_cuadrado(lado))
        print("Perímetro:", figuras.perimetro_cuadrado(lado))

    elif opcion == "2":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print("Área:", figuras.area_rectangulo(base, altura))
        print("Perímetro:", figuras.perimetro_rectangulo(base, altura))

    elif opcion == "3":
        a = float(input("Lado A: "))
        b = float(input("Lado B: "))
        c = float(input("Lado C: "))
        h = float(input("Altura (para el área): "))
        print("Área:", figuras.area_triangulo(a, h))
        print("Perímetro:", figuras.perimetro_triangulo(a, b, c))

    elif opcion == "4":
        radio = float(input("Radio: "))
        print("Área:", figuras.area_circulo(radio))
        print("Perímetro:", figuras.perimetro_circulo(radio))

    elif opcion == "5":
        print("¡Adiós! 👋")
        break

    else:
        print("Opción no válida")