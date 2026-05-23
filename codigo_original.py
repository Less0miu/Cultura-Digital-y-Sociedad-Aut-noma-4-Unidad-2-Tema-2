import time

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primos_hasta_100k():
    primos = []
    for num in range(1, 100001):
        if es_primo(num):
            primos.append(num)
    return primos

if __name__ == "__main__":
    inicio = time.time()
    resultado = primos_hasta_100k()
    fin = time.time()
    print(f"Tiempo de ejecución ORIGINAL: {fin - inicio:.4f} segundos")
    print(f"Cantidad de primos encontrados: {len(resultado)}")
