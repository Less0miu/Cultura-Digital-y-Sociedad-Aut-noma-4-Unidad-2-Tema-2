import cProfile
from codigo_optimizado import primos_optimizado

cProfile.run('primos_optimizado()', 'profiling_optimizado.txt')
print(" Profiling optimizado guardado")
