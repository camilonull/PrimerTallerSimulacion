# Importamos el módulo 'random' para generar números aleatorios.
import random
import time  # Importamos el módulo 'time' para medir el tiempo de procesamiento.

# Definimos la función 'saltos_a_objetivo_3d' que determina cuántos saltos necesita la rana para alcanzar un objetivo en 3D.
def saltos_a_objetivo_3d(objetivo_x, objetivo_y, objetivo_z):
    """
    Simula el movimiento de una rana en un espacio 3D hasta alcanzar un objetivo.
    
    Parámetros:
    - objetivo_x (int): Coordenada x del objetivo.
    - objetivo_y (int): Coordenada y del objetivo.
    - objetivo_z (int): Coordenada z del objetivo.
    
    Retorno:
    - int: Número total de saltos necesarios para llegar al objetivo.
    """
    # Inicializamos las coordenadas de la rana en (0, 0, 0), es decir, el origen del espacio tridimensional.
    x, y, z = 0, 0, 0
    # Inicializamos el contador de saltos en 0.
    saltos = 0

    # Usamos un bucle while que continuará hasta que la rana alcance las coordenadas objetivo.
    while (x, y, z) != (objetivo_x, objetivo_y, objetivo_z):
        # La rana puede saltar en el eje x, y o z.
        salto_x = random.choice([-1, 1])
        salto_y = random.choice([-1, 1])
        salto_z = random.choice([-1, 1])

        # Actualizamos las coordenadas de la rana sumando el valor del salto en cada eje.
        x += salto_x
        y += salto_y
        z += salto_z
        # Aumentamos el contador de saltos en 1.
        saltos += 1

    # Al final, retornamos el total de saltos necesarios para alcanzar el objetivo.
    return saltos

# Definimos el objetivo en 3D como una tupla (x, y, z).
objetivo_3d = (45, 23, 17)

# Inicia la temporización
start_time = time.time()

# Llamamos a la función 'saltos_a_objetivo_3d' con el objetivo especificado y guardamos el número de saltos necesarios.
saltos_3d = saltos_a_objetivo_3d(*objetivo_3d)

# Finaliza la temporización
end_time = time.time()

# Calculamos el tiempo total de procesamiento
tiempo_total = end_time - start_time

# Imprimimos el resultado: cuántos saltos se necesitan para llegar a la posición objetivo en 3D.
print(f"Se necesitan {saltos_3d} saltos para llegar a la posición {objetivo_3d} en 3D.")
print(f"Tiempo total de procesamiento: {tiempo_total:.4f} segundos")
