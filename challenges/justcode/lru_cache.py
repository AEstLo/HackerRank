# https://www.hackerrank.com/contests/justcode/challenges/lru-implementtion

import unittest


class DoubleLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def setNext(self, node):
        self.next = node

    def setPrev(self, node):
        self.prev = node

    def getValue(self):
        return self.value


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addLast(self, value):
        new_node = DoubleLinkedListNode(value)
        if self.tail is None:
            assert self.head is None
            self.head = self.tail = new_node
        else:
            self.tail.setNext(new_node)
            new_node.setPrev(self.tail)
            self.tail = new_node

    def addFirst(self, value):
        new_node = DoubleLinkedListNode(value)
        if self.head is None:
            self.addLast(value)
        else:
            new_node.setNext(self.head)
            self.head.setPrev(new_node)
            self.head = new_node

    def moveFirst(self, node):
        if node.prev and node != self.head:
            prev = node.prev
            if node == self.tail:
                self.tail = prev
            prev.setNext(node.next)
            if node.next:
                node.next.setPrev(prev)
            node.setNext(self.head)
            self.head.setPrev(node)
            self.head = node

    def removeLast(self):
        if self.tail is not None:
            value = self.tail.getValue()
            prev = self.tail.prev
            if prev:
                prev.next = None
            self.tail = prev
            return value
        return None

    def toString(self):
        ret = []
        node = self.head
        while node:
            ret.append(str(node.value))
            node = node.next
        return ' '.join(ret)

    def toStringDebug(self):
        ret = []
        node = self.head
        while node:
            ret.append(
                f'(prev <- {node.prev and node.prev.value} ) {node.value} (next -> {node.next and node.next.value})')
            node = node.next
        return ' '.join(ret)


class LRUCache:
    def __init__(self, capacity):
        self.size = capacity
        self.cache_ll = DoubleLinkedList()
        self.hash_elements = {}

    def get(self, value):
        if value in self.hash_elements:
            node = self.hash_elements[value]
            self.cache_ll.moveFirst(node)
            return True
        else:
            self.cache_ll.addFirst(value)
            self.hash_elements[value] = self.cache_ll.head
            while len(self.hash_elements) > self.size:
                value_deleted = self.cache_ll.removeLast()
                if value_deleted is not None:
                    del self.hash_elements[value_deleted]
            return False

    def toString(self):
        return self.cache_ll.toString()


class Testing(unittest.TestCase):

    def test_001(self):
        lru_cache = LRUCache(4)
        page_faults = 0
        for elem in '1 1 2 3 5 3 1 4 5 9 6 3 2 5'.split(' '):
            elem_int = int(elem)
            if not lru_cache.get(elem_int):
                page_faults += 1
        self.assertEqual(page_faults, 10)
        self.assertEqual(lru_cache.toString(), '5 2 3 6')

    def test_002(self):
        lru_cache = LRUCache(3)
        page_faults = 0
        for elem in '4 5 4 5 4 4 3'.split(' '):
            elem_int = int(elem)
            if not lru_cache.get(elem_int):
                page_faults += 1
        self.assertEqual(page_faults, 3)
        self.assertEqual(lru_cache.toString(), '3 4 5')

    def test_003(self):
        lru_cache = LRUCache(7)
        page_faults = 0
        for elem in '1 2 2 0 3 6 5 2 0 1 4 5 8 7 4 0 2 5 6 0 2 1 4 5 6 9 8 7 4 5 6 3 2 1 4 8 7 4 5'.split(' '):
            elem_int = int(elem)
            if not lru_cache.get(elem_int):
                page_faults += 1
        self.assertEqual(page_faults, 20)
        self.assertEqual(lru_cache.toString(), '5 4 7 8 1 2 3')


if __name__ == '__main__':
    unittest.main()
