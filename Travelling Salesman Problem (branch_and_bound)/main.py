import sys
paths = {}

class Node:
    def __init__(self, number, cost_now, unvisited_cities):
        self.number = number
        self.cost_now = cost_now
        self.unvisited_cities = unvisited_cities
        self.previous = None
        self.next = None

    def create_child(self, city, cost):
        new_unvisited_cities = [i for i in self.unvisited_cities if i != city]
        return Node(city, self.cost_now + cost, new_unvisited_cities)

def branch_and_bound(matrix, current_node, visited):
    global bound
    # se todas as cidades foram visitadas
    if not current_node.unvisited_cities:
        # se encontrar um caminho melhor que o bound atual, atualiza o bound e adiciona aos paths
        if current_node.cost_now < bound:
            bound = current_node.cost_now
            paths[tuple(visited)] = current_node.cost_now
        return
    
    # para cada cidade não visitada procura caminhos a partir da cidade atual
    for next_city in current_node.unvisited_cities:
        # no momento em o caminho atual ultrapassar o valor, para de explorar esse caminho
        if current_node.cost_now + matrix[current_node.number][next_city] < bound:
            # cria a proxima cidade
            child_node = current_node.create_child(next_city, matrix[current_node.number][next_city])
            child_node.previous = current_node
            visited.append(next_city)

            # explora a nova cidade
            branch_and_bound(matrix, child_node, visited)
            visited.pop() # remove cidades depois de explorar nas chamadas recursivas

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    
    distances = [
        [0, 12, 18, 24, 30, 36],
        [12, 0, 42, 30, 36, 24],
        [18, 42, 0, 36, 48, 30],
        [24, 30, 36, 0, 54, 42],
        [30, 36, 48, 54, 0, 60],
        [36, 24, 30, 42, 60, 0]]
    
    starter_city = 1 #<-- cidade inicial

    visited = [starter_city]
    cities = [i for i in range(len(distances)) if i != starter_city]
    bound = sys.maxsize
    start_node = Node(starter_city , 0, cities)

    branch_and_bound(distances, start_node, visited)

    print("Best path:", min(paths, key=paths.get))
    print("Best cost:", paths[min(paths, key=paths.get)])
    print("\nAll paths (bound checked):")
    for path in paths:
        print(path, paths[path])