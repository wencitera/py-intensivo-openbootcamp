""" 
Ejercicio 3

Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.

Objetivo:

Uso de bucles anidados

El uso de colecciones
"""

def main():
    primos = obtener_numeros_primos(10)
    print(primos)


def obtener_numeros_primos(numero):
    max = numero +1
    primos = []
    for i in range(2,max):
        if es_primo(i):
            primos.append(i)

    return primos

def es_primo(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


if __name__ == '__main__':
    main()