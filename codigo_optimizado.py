import time
import math

def es_primo_opt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limite = int(math.isqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True

def primos_optimizado():
    return [num for num in range(2, 100001) if es_primo_opt(num)]

if __name__ == "__main__":
    inicio = time.time()
    resultado = primos_optimizado()
    fin = time.time()
    print(f"Tiempo de ejecución OPTIMIZADO: {fin - inicio:.4f} segundos")
    print(f"Cantidad de primos encontrados: {len(resultado)}")
