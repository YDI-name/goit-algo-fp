import heapq


class Graph:
    def __init__(self):
        # Використовуємо словник для зберігання списків суміжності
        self.graph = {}

    def add_edge(self, u, v, weight):
        """Додає орієнтоване ребро від вершини u до вершини v з вагою weight."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []  # Забезпечуємо наявність усіх вершин у словнику

        self.graph[u].append((v, weight))

    def dijkstra(self, start_vertex):
        """
        Знаходить найкоротші шляхи від start_vertex до всіх інших вершин.
        Повертає словник {вершина: мінімальна_відстань}.
        """
        # Ініціалізуємо відстані до всіх вершин як нескінченність
        distances = {vertex: float("infinity") for vertex in self.graph}
        distances[start_vertex] = 0

        # Бінарна купа для зберігання пар (поточна_відстань, вершина)
        # Python heapq працює як min-heap, сортуючи за першим елементом кортежу
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            # Витягуємо вершину з найменшою відомою відстанню
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Якщо ми вже знайшли коротший шлях до цієї вершини раніше,
            # пропускаємо обробку (оптимізація "лінивого видалення")
            if current_distance > distances[current_vertex]:
                continue

            # Перевіряємо всіх сусідів поточної вершини
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # Якщо знайдено коротший шлях до сусіда — оновлюємо дані
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    # Додаємо оновлену відстань у бінарну купу
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Приклад використання
if __name__ == "__main__":
    # 1. Створення графа
    g = Graph()

    # Додаємо ребра (вершина_від, вершина_до, вага)
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 5)
    g.add_edge("B", "D", 10)
    g.add_edge("C", "E", 3)
    g.add_edge("E", "D", 4)
    g.add_edge("D", "Z", 11)

    start_node = "A"

    # 2. Обчислення найкоротших шляхів
    shortest_paths = g.dijkstra(start_node)

    # 3. Виведення результатів
    print(f"Найкоротші відстані від вершини '{start_node}':")
    for vertex, distance in shortest_paths.items():
        if distance == float("infinity"):
            print(f"До {vertex}: Шляху немає")
        else:
            print(f"До {vertex}: {distance}")
