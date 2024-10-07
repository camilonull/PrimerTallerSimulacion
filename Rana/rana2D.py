import random
import time

def saltos_a_objetivo_2d(objetivo_x, objetivo_y):
    """
    Simula el movimiento de una rana en un plano 2D hasta alcanzar un objetivo.
    
    Parámetros:
    - objetivo_x (int): Coordenada x del objetivo.
    - objetivo_y (int): Coordenada y del objetivo.
    
    Retorno:
    - int: Número total de saltos necesarios para llegar al objetivo.
    """
    x, y = 0, 0  # Inicializamos las coordenadas en (0,0)
    saltos = 0  # Contador de saltos

    # Bucle que continuará hasta que la rana alcance las coordenadas objetivo
    while (x, y) != (objetivo_x, objetivo_y):
        salto_x = random.choice([-1, 1])  # Elección aleatoria de salto en el eje x
        salto_y = random.choice([-1, 1])  # Elección aleatoria de salto en el eje y

        x += salto_x  # Actualizamos la posición en el eje x
        y += salto_y  # Actualizamos la posición en el eje y
        saltos += 1   # Aumentamos el contador de saltos

    return saltos  # Retornamos el número total de saltos necesarios

# Definimos el objetivo en 2D
objetivo_2d = (250, 300)

# Inicia la temporización
start_time = time.time()

# Calculamos el número de saltos necesarios para llegar al objetivo
saltos_necesarios = saltos_a_objetivo_2d(*objetivo_2d)

# Finaliza la temporización
end_time = time.time()

# Calculamos el tiempo total de procesamiento
tiempo_total = end_time - start_time

# Imprimimos los resultados
print(f"Se necesitan {saltos_necesarios} saltos para llegar a la posición {objetivo_2d} en 2D.")
print(f"Tiempo total de procesamiento: {tiempo_total:.4f} segundos")

