import unittest

from task import Node


class TestCase(unittest.TestCase):
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node("node_without_next")

        msg = "Значение следующего узла по умолчанию должно быть None"
        self.assertIsNone(node.next, msg)

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        right_node = Node("right")
        left_node = Node("left", right_node)

        msg = "Значение следующего узла при инициализации некорректно"
        self.assertEqual(repr(left_node.next), repr(right_node), msg)

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node = Node("node_without_next")

        msg = "Значение представления __repr__ некорректно для узла без следующего узла. "
        self.assertEqual(repr(node), "Node(node_without_next, None)", msg)

    @unittest.skip("Тест пропущен по причине ...")
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        ...

        def test_str(self):
            some_value = 5
            node = Node(some_value)

            self.assertEqual(str(node), str(some_value))

    def test_str(self):
        some_value = 5
        node = Node(some_value)

        # TODO проверить строковое представление

    def test_is_valid(self):
        Node.is_valid(None)
        Node.is_valid(Node("correct_node"))

        with self.assertRaises(TypeError):
            Node.is_valid("incorrect_type")

