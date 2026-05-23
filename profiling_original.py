import cProfile
from codigo_original import primos_hasta_100k

cProfile.run('primos_hasta_100k()', 'profiling_original.txt')
print(" Profiling original guardado")
