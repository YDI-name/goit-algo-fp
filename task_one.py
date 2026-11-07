from typing import Optional, Any


class Node:
    """Вузол однозв'язного списку."""

    def __init__(self, data: Any):
        self.data = data
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def insert_at_end(self, data: Any) -> None:
        """Додавання вузла в кінець списку."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def __iter__(self):
        """Робить список ітерованим (можна використовувати у for-циклах)."""
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def __str__(self) -> str:
        """Дозволяє друкувати список через print(linked_list)."""
        elements = [str(data) for data in self]
        return " -> ".join(elements) if elements else "Порожній список"

    # Реверсування
    def reverse(self) -> None:
        """Реверсування списку на місці"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування (Merge Sort)
    def sort(self) -> None:
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head: Optional[Node]) -> Optional[Node]:
        if not head or not head.next:
            return head

        # Знаходимо середину та розбиваємо список навпіл
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        return _merge_nodes(left, right)

    def _get_middle(self, head: Node) -> Node:
        """Знаходить середину списку методом двох вказівників (швидкий і повільний)."""
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# Об'єднання двох відсортованих списків
def _merge_nodes(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
    """Допоміжна функція, яка зливає два ланцюжки вузлів. Використовується і для Task 2, і для Task 3."""
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Прикріплюємо залишки
    tail.next = l1 if l1 else l2
    return dummy.next


def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    """Об'єднує два відсортовані об'єкти LinkedList в один новий."""
    merged_list = LinkedList()
    merged_list.head = _merge_nodes(list1.head, list2.head)
    return merged_list


if __name__ == "__main__":
    # 1. Тест реверсування
    llist = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        llist.insert_at_end(val)
    print("До реверсування:", llist)
    llist.reverse()
    print("Після реверсування:", llist)

    print("-" * 30)

    # 2. Тест сортування
    llist_unsorted = LinkedList()
    for val in [4, 2, 5, 1, 3]:
        llist_unsorted.insert_at_end(val)
    print("Невідсортований:", llist_unsorted)
    llist_unsorted.sort()
    print("Відсортований:", llist_unsorted)

    print("-" * 30)

    # 3. Тест об'єднання двох списків
    list1 = LinkedList()
    for val in [1, 3, 5]:
        list1.insert_at_end(val)

    list2 = LinkedList()
    for val in [2, 4, 6, 8]:
        list2.insert_at_end(val)

    print("Список 1:", list1)
    print("Список 2:", list2)

    merged = merge_sorted_lists(list1, list2)
    print("Об'єднаний:", merged)
