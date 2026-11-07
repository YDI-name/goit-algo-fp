import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys
from collections import deque


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для NetworkX


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Функція для додавання вузлів та ребер у граф для візуалізації."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Binary Tree"):
    """Функція для малювання дерева."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    plt.title(title, fontsize=14)
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
        font_color="white",
        font_weight="bold",
        font_size=12,
    )
    plt.show()


def generate_gradient_colors(n, base_color="#1296F0"):
    """Генерує `n` кольорів від темного до світлого відтінку на основі base_color."""
    # Перетворюємо HEX у RGB (значення від 0 до 1)
    base_color = base_color.lstrip("#")
    r, g, b = tuple(int(base_color[i : i + 2], 16) / 255.0 for i in (0, 2, 4))

    # Перетворюємо RGB у HLS (Hue, Lightness, Saturation)
    h, l, s = colorsys.rgb_to_hls(r, g, b)

    colors = []
    for i in range(n):
        # Змінюємо яскравість (Lightness) від 0.2 (темний) до 0.9 (світлий)
        lightness = 0.2 + (0.7 * i / max(1, n - 1))
        # Перетворюємо назад у RGB
        new_r, new_g, new_b = colorsys.hls_to_rgb(h, lightness, s)
        # Перетворюємо у HEX формат, напр., #1A2B3C
        hex_color = (
            f"#{int(new_r * 255):02X}{int(new_g * 255):02X}{int(new_b * 255):02X}"
        )
        colors.append(hex_color)

    return colors


def dfs_traversal(root):
    """Обхід дерева в глибину (DFS) - використовуємо стек."""
    visited = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            visited.append(node)
            # Додаємо правого нащадка першим, щоб лівий оброблявся раніше
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited


def bfs_traversal(root):
    """Обхід дерева в ширину (BFS) - використовуємо чергу."""
    visited = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            # Додаємо лівого, потім правого нащадка
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return visited


def visualize_traversal(root, traversal_func, title):
    """Виконує обхід, призначає кольори вузлам та малює дерево."""
    # Отримуємо порядок вузлів
    traversal_order = traversal_func(root)

    # Генеруємо палітру кольорів відповідно до кількості вузлів
    colors = generate_gradient_colors(len(traversal_order))

    # Призначаємо кольори вузлам у порядку їх відвідування
    for idx, node in enumerate(traversal_order):
        node.color = colors[idx]

    # Малюємо дерево з новими кольорами
    draw_tree(root, title)


# Побудова тестового дерева

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.right.left.right = Node(2)

# Запуск візуалізацій
if __name__ == "__main__":
    print("Візуалізація обходу в глибину (DFS)...")
    visualize_traversal(root, dfs_traversal, "Обхід в глибину (DFS)")
    print("Візуалізація обходу в ширину (BFS)...")
    visualize_traversal(root, bfs_traversal, "Обхід в ширину (BFS)")
