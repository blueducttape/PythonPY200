from collections.abc import MutableSequence
from typing import Any, Optional, Iterable
from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self._len = 0
        self._head: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any) -> None:
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)
        if self._head is None:
            self._head = append_node
        else:
            last_index = self._len - 1
            last_node = self._step_by_step_on_nodes(last_index)
            self.linked_nodes(last_node, append_node)
        self._len += 1

    def __len__(self):
        return self._len

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.
        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __check_index(self, index: Any) -> None:
        """проверка занчения на соответствие требованиям к индексу"""
        if not isinstance(index, int):  # проверка типов
            raise TypeError()
        if not 0 <= index < self._len:  # проверка диапазона индексов
            raise IndexError()

    def _step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        self.__check_index(index)
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self._step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self._step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int) -> None:
        """удаление элемента из списка по индеку"""
        self.__check_index(index)
        if index == 0:
            self._head = self._head.next
        elif index == self._len - 1:
            tail = self._step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self._step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next
            self.linked_nodes(prev_node, next_node)
        self._len -= 1

    def _to_list(self) -> list:
        """вывод значений списка"""
        return [linked_list_value.value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._to_list()})"

    def __str__(self) -> str:
        return f"{self._to_list()}"

    def insert(self, index: int, value: Any) -> None:
        """
        Вставка нового элемента по индексу
        :param index: индекс жедаемого места вставки
        :param value: значение узла
        """
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index:  # для for
            raise IndexError()
        if index >= self._len:
            self.append(value)
        else:
            new_node = Node(value)
            if index == 0:
                new_node.next = self._head
                self._head = new_node
            else:
                current_node = self._step_by_step_on_nodes(index)
                prev_node = self._step_by_step_on_nodes(index - 1)
                new_node.next = current_node
                prev_node.next = new_node
            self._len += 1

    def count(self, value: int) -> int:
        """
        Возвращает количество вхождений value в список
        :param value:
        :return:
        """
        result = 0
        for _, val in enumerate(self):
            if val == value:
                result += 1
        return result

    def extend(self, iterable_obj: Iterable):
        """
        Добавляет в список значения из итерируемого объекта
        """
        for item in iterable_obj:
            self.append(item)

    def pop(self, index: int = None) -> Any:
        """
        Возвращает и удаляет элемент по индексу (если None - берется последний)
        :param index: индекс искомого элемента
        :return: значение элемента
        """
        if isinstance(index, type(None)):
            index = self._len - 1
        result = self._step_by_step_on_nodes(index)
        self.__delitem__(index)
        return result

    def __iter__(self) -> Iterable:
        current_node = self._head
        for _ in range(self._len):
            yield current_node
            current_node = current_node.next


class DoubleLinkedList(LinkedList):
    """ Класс двусвязного списка из объектов типа DoubleLinkedNode """

    def __init__(self, data: Iterable = None):
        self._tail = None
        super().__init__(data)

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode,
                     right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = DoubleLinkedNode(value)
        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node
        self._len += 1


if __name__ == "__main__":
    ll = DoubleLinkedList([1, 2, 3, 4, 5, 6])
    print(ll)
    ll.insert(3, 6)
    l1 = iter(ll)
    for v in l1:
        print(v)
