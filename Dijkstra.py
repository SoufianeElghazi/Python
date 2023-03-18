import sys


def dijkstra(graph, start):
    """
    Implémentation de l'algorithme de Dijkstra pour trouver le chemin le plus court dans un graphe pondéré.

    :param graph: un dictionnaire représentant le graphe pondéré. Chaque clé est un noeud et chaque valeur est un dictionnaire représentant les voisins de ce noeud et les coûts pour s'y rendre.
    :param start: le noeud de départ
    :return: un dictionnaire représentant le chemin le plus court vers chaque noeud à partir du noeud de départ
    """
    # Initialisation des distances à l'infini
    distances = {node: sys.maxsize for node in graph}
    # La distance du noeud de départ à lui-même est de 0
    distances[start] = 0
    # Ensemble des noeuds visités
    visited = set()

    while len(visited) < len(graph):
        # Recherche du noeud non visité avec la distance minimale
        min_distance = sys.maxsize
        min_node = None
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        # Marquage du noeud courant comme visité
        visited.add(min_node)

        # Mise à jour des distances des voisins du noeud courant
        for neighbor, cost in graph[min_node].items():
            distance = distances[min_node] + cost
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances
# Application:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

dijkstra(graph, 'A') # -----> {'A': 0, 'B': 1, 'C': 3, 'D': 4}
