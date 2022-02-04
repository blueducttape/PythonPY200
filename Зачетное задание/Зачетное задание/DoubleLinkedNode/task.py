from typing import Any, Optional

class Node:

    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, prev: Optional["DoubleLinkedNode"] = None,
                 next_: Optional["DoubleLinkedNode"] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        """Возвращает значение DoubleLinkedNode.prev"""
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional["DoubleLinkedNode"]):
        """Устанавливает значение DoubleLinkedNode.prev"""
        self.is_valid(prev_)
        self._prev = prev_

    def __repr__(self):
        return f"{self.__class__.__name__}({self._prev}, {self.value}, {self._next})"


if __name__ == "__main__":
    node1 = Node(123)
    node2 = Node(456, node1)

    dnode1 = DoubleLinkedNode(111)
    dnode2 = DoubleLinkedNode(222)
    dnode3 = DoubleLinkedNode(333, dnode1, dnode2)

    print(node1)
    print(node2)
