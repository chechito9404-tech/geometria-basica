import math

def area_cuadrado(lado):
    return lado * lado

def perimetro_cuadrado(lado):
    return 4 * lado

def area_rectangulo(base, altura):
    return base * altura

def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

def area_triangulo(base, altura):
    return (base * altura) / 2

def perimetro_triangulo(a, b, c):
    return a + b + c

def area_circulo(radio):
    return math.pi * (radio ** 2)

def perimetro_circulo(radio):
    return 2 * math.pi * radio