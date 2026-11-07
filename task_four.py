import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
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


def draw_tree(tree_root):
    if tree_root is None:
        return

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


# --- НОВА ФУНКЦІЯ ДЛЯ ПОБУДОВИ КУПИ ---
def build_heap_tree(heap_array):
    """
    Перетворює масив (бінарну купу) у структуру вузлів (Node) для візуалізації.
    """
    if not heap_array:
        return None

    # 1. Створюємо список об'єктів Node для кожного елемента масиву
    nodes = [Node(val) for val in heap_array]

    # 2. Проходимо по масиву і встановлюємо зв'язки (left, right)
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        # Якщо лівий нащадок існує в межах масиву, прив'язуємо його
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]

        # Якщо правий нащадок існує в межах масиву, прив'язуємо його
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    return nodes[0]


# ПРИКЛАД ВИКОРИСТАННЯ

heap_array = [0, 4, 1, 5, 10, 3]
root = build_heap_tree(heap_array)
draw_tree(root)
