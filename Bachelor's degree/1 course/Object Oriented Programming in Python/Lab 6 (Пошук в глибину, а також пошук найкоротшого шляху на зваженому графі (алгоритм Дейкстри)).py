import sys
import heapq

# Computer Science FB01, Lab 6, Сахній Назар ФБ-01
print("Computer Science FB01, Lab 6, Варіант 18")
print("Сахній Назар ФБ-01\n")


class Vertex:
    def __init__(self, vertex):
        self.id = vertex
        self.adjacent = {}
        self.distance = sys.maxsize  # Встановлює вагу кожного ребра графа до нескінченності
        self.visited = False  # Робить всі вершини не "відвіданими"
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __lt__(self, other):
        return self.id < other.id


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, vertex):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(vertex)
        self.vert_dict[vertex] = new_vertex
        return None

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)


def shortest(v, path):  # Зробить найкоротший шлях від попередника
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return None


def dijkstra(aGraph, start):
    start.set_distance(0)
    unvisited_queue = [(v.get_distance(), v) for v in aGraph]  # Поміщає пару кортежів у чергу пріоритетів
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):

        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        for next in current.adjacent:

            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)

        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)

        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


def cheapest_path(g, start_v, target_v, text) -> None:
    dijkstra(g, g.get_vertex(start_v))

    target = g.get_vertex(target_v)
    path = [target.get_id()]
    shortest(target, path)
    path = path[::-1]

    print(f"Найменш затратний маршрут {text}:")
    counter = 0
    while counter < len(path):
        if counter < len(path) - 1:
            print(path[counter] + " -> ", end='')
            counter += 1
        else:
            print(path[counter])
            counter += 1


# Звичайний маршрут
g = Graph()
g.add_vertex('A')
g.add_vertex('X')
g.add_vertex('Y')
g.add_vertex('Z')
g.add_vertex('V')
g.add_vertex('W')
g.add_vertex('B')
g.add_edge('A', 'X', 2)
g.add_edge('A', 'V', 8)
g.add_edge('A', 'Z', 2)
g.add_edge('X', 'Y', 2)
g.add_edge('X', 'W', 5)
g.add_edge('Y', 'W', 1)
g.add_edge('Y', 'V', 7)
g.add_edge('Z', 'Y', 1)
g.add_edge('Z', 'V', 7)
g.add_edge('V', 'B', 3)
g.add_edge('W', 'V', 4)
g.add_edge('W', 'B', 1)
cheapest_path(g, "A", "B", "(У довільному випадку)")

# Рівноцінні ділянки
g = Graph()
g.add_vertex('A')
g.add_vertex('X')
g.add_vertex('Y')
g.add_vertex('Z')
g.add_vertex('V')
g.add_vertex('W')
g.add_vertex('B')
g.add_edge('A', 'X', 1)
g.add_edge('A', 'V', 1)
g.add_edge('A', 'Z', 1)
g.add_edge('X', 'Y', 1)
g.add_edge('X', 'W', 1)
g.add_edge('Y', 'W', 1)
g.add_edge('Y', 'V', 1)
g.add_edge('Z', 'Y', 1)
g.add_edge('Z', 'V', 1)
g.add_edge('V', 'B', 1)
g.add_edge('W', 'V', 1)
g.add_edge('W', 'B', 1)
cheapest_path(g, "A", "B", "(Всі ділянки рівноцінні)")

# Два рівноцінні маршрути
g = Graph()
g.add_vertex('A')
g.add_vertex('X')
g.add_vertex('Y')
g.add_vertex('Z')
g.add_vertex('V')
g.add_vertex('W')
g.add_vertex('B')
g.add_edge('A', 'X', 10)
g.add_edge('A', 'V', 10)
g.add_edge('A', 'Z', 5)
g.add_edge('X', 'Y', 10)
g.add_edge('X', 'W', 10)
g.add_edge('Y', 'W', 10)
g.add_edge('Y', 'V', 10)
g.add_edge('Z', 'Y', 10)
g.add_edge('Z', 'V', 5)
g.add_edge('V', 'B', 5)
g.add_edge('W', 'V', 10)
g.add_edge('W', 'B', 10)
cheapest_path(g, "A", "B", "(Два рівноцінних маршрути)")

input("\nЩоб вийти із програми натисніть Enter")
