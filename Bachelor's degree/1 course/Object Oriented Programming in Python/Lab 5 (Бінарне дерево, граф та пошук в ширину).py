# Computer Science FB01, Lab 5, Сахній Назар ФБ-01
print("Computer Science FB01, Lab 5, Варіант 18")
print("Сахній Назар ФБ-01")


def bfs_connected_component(graph, start):  # функція пошуку у ширину
    queue = [start]  # проміжний масив для пошуку у ширину/черга
    levels = dict()  # словник для зберігання глибини вершин
    levels[start] = 0
    visited = [start]  # масив пройдених вершин
    while queue:
        node = queue.pop(0)  # беремо вершину з "черги"
        neighbours = graph[node]  # беремо сусідів вершини із словника
        for neighbour in neighbours:  # пошук по сусідам
            if neighbour not in visited:  # якщо сусідню вершину ще не проходили(тобто, граф може бути не деревом)
                queue.append(neighbour)  # додаємо сусідню вершину до черги
                visited.append(neighbour)  # додаємо сусідню вершину до пройдених

                levels[neighbour] = levels[node] + 1  # записуємо її глибину до словника
    print(levels)  # вивід словника
    print("Length of graph is:", list(levels.values())[-1])  # вивід довжини графа
    return visited  # повертаємо список вершин у їх порядку


def path(graph, start, end):  # функція пошуку маршруту від вершини до вершини, код дуже схожий, бо це також пошук :)
    way = []  # масив, у який записуємо маршрут
    queue = [start]  # "черга" №2, починається з першої даної вершини
    visited = [start]  # масив для пройдених вершин, починається з першої даної вершини
    while end not in queue:  # поки не дійшли до останньої вершини
        node = queue.pop(0)  # беремо вершину з "черги"
        way.append(node)  # додаємо її до маршруту
        neighbours = graph[node]  # беремо сусідів вершини із словника

        for neighbour in neighbours:  # пошук по сусідям
            if neighbour not in visited:  # якщо сусідню вершину ще не проходили(тобто, граф може бути не деревом)
                queue.append(neighbour)  # додаємо сусідню вершину до черги
                visited.append(neighbour)  # додаємо сусідню вершину до пройдених

    way.append(end)  # додаємо нашу кінцеву вершину до маршруту
    return way


def common_part(start1, start2, end):  # ф-ія знаходження спільної ділянки маршрутів А->C, B->C
    path1 = path(graph, start1, end)
    print(f"Маршрут з {start1} до {end} : {path1}")
    path2 = path(graph, end, start2)
    path2.reverse()
    print(f"Маршрут з {start2} до {end} : {path2}")

    path3 = []
    length = 0
    for i in range(len(path1) - 1):
        if path1[i] in path2:
            length += 1
            if path1[i + 1] == path2[path2.index(path1[i + 1])]:
                path3.append(path1[i] + "-" + path1[i + 1])
    return f'{length} ділянки', path3


graph = {'A': ['N'],
         'B': ['N', 'L', 'K'],
         'N': ['A', 'B'],
         'X': ['K'],
         'Z': ['K'],
         'K': ['B', 'X', 'Z'],
         'C': ['L', 'D'],
         'L': ['B', 'C', 'I'],
         'I': ['L'],
         'D': ['C'],
         }  # Ініціалізація нашого графу

print(f"Ділянки, що співпадають:{common_part('A', 'B', 'C')}")
input("\nЩоб вийти із програми натисніть Enter")
