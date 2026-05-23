import matplotlib.pyplot as plt

# Tus tiempos - actualiza estos valores después de ejecutar los códigos
tiempo_original = 26.8134
tiempo_optimizado = 0.1120

tiempos = [tiempo_original, tiempo_optimizado]
etiquetas = ['Código Original', 'Código Optimizado']
colores = ["#ae3ce7", "#d72cc0"]

plt.figure(figsize=(8, 6))
barras = plt.bar(etiquetas, tiempos, color=colores, edgecolor='black', linewidth=1.5)

plt.ylabel('Tiempo de ejecución (segundos)', fontsize=12)
plt.title('Comparación de Rendimiento\nCálculo de Números Primos hasta 100,000', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

for barra, tiempo in zip(barras, tiempos):
    plt.text(barra.get_x() + barra.get_width()/2, 
             barra.get_height() + 0.5, 
             f'{tiempo:.4f} s', 
             ha='center', va='bottom', fontsize=11, fontweight='bold')

mejora = ((tiempo_original - tiempo_optimizado) / tiempo_original) * 100
plt.figtext(0.5, 0.01, f'Mejora del rendimiento: {mejora:.2f}%', 
            ha='center', fontsize=11, style='italic',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('comparacion_tiempos.png', dpi=300, bbox_inches='tight')
print(" Gráfico guardado como 'comparacion_tiempos.png'")
plt.show()
