import random  # Importamos el módulo 'random' para generar números aleatorios.
import matplotlib.pyplot as plt  # Importamos matplotlib para crear gráficos.
import time  # Importamos el módulo time para medir el tiempo de ejecución.

def movimiento_rana(saltos):
    """
    Simula el movimiento de una rana en una recta numérica y registra las posiciones.
    
    Parámetros:
    - saltos (int): La cantidad total de saltos que realizará la rana.
    
    Retorno:
    - list: Lista de posiciones de la rana en cada salto.
    """
    posicion = 0  # Inicializamos la posición de la rana en 0 (origen de la recta numérica).
    posiciones = [posicion]  # Lista para almacenar las posiciones en cada salto.
    
    # Iteramos 'saltos' veces para simular cada salto de la rana.
    for _ in range(saltos):
        # Cada salto puede ser hacia adelante (+1) o hacia atrás (-1) con igual probabilidad.
        salto = random.choice([-1, 1])
        
        # Actualizamos la posición de la rana sumando el valor del salto.
        posicion += salto
        
        # Agregamos la nueva posición a la lista de posiciones.
        posiciones.append(posicion)

    # Retornamos la lista de posiciones de la rana después de todos los saltos.
    return posiciones

# Establecemos el número total de saltos que queremos simular (1 millón en este caso).
saltos = 1000000

# Inicia la temporización
start_time = time.time()

# Llamamos a la función 'movimiento_rana' con 1 millón de saltos y guardamos las posiciones.
posiciones = movimiento_rana(saltos)

# Finaliza la temporización
end_time = time.time()

# Calculamos el tiempo total de procesamiento
tiempo_total = end_time - start_time

# Imprimimos la posición final de la rana y el tiempo total de procesamiento.
print(f"La posición final de la rana después de {saltos} saltos es {posiciones[-1]}")
print(f"Tiempo total de procesamiento: {tiempo_total:.4f} segundos")

# Graficamos las frecuencias de salida utilizando un histograma.
plt.hist(posiciones, bins=30, edgecolor='black', density=True)
plt.title('Distribución de las posiciones de la rana')  # Título del gráfico.
plt.xlabel('Posición')  # Etiqueta del eje X.
plt.ylabel('Frecuencia relativa')  # Etiqueta del eje Y.
plt.grid(True)  # Mostramos una cuadrícula en el gráfico.
plt.show()  # Mostramos el gráfico.
