# Función para encontrar la orientación de tripletas de puntos (p, q, r)
# Devuelve 0 si p, q y r son colineales, 1 si en sentido horario y 2 si en sentido antihorario
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # colineal
    elif val > 0:
        return 1  # sentido horario
    else:
        return 2  # sentido antihorario

# Función para la envolvente convexa utilizando el algoritmo de Jarvis
def convex_hull(points):
    n = len(points)
    
    # Si hay menos de 3 puntos, no se puede formar una envolvente convexa
    if n < 3:
        return None
    
    # Encontrar el punto más a la izquierda
    leftmost = min(points)
    hull = []
    p = points.index(leftmost)
    q = 0
    
    # Comenzar desde el punto más a la izquierda y avanzar en sentido horario
    while True:
        hull.append(points[p])
        
        # Buscar un punto 'q' tal que la orientación de tripletas 'p, i, q' sea en sentido antihorario para cualquier punto 'i'
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        
        # Establecer 'q' como siguiente punto de 'p' para seguir avanzando
        p = q
        
        # Si volvemos al primer punto, hemos completado el ciclo
        if p == 0:
            break
    
    return hull

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de coordenadas de puntos [(x, y)]
    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
    
    # Encontrar la envolvente convexa
    convex_hull_points = convex_hull(points)
    
    # Mostrar la envolvente convexa
    print("Envolvente Convexa:")
    for point in convex_hull_points:
        print(point)
