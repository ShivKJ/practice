from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Dict


@dataclass
class Node:
    char: str = field(default=None)
    is_end_of_word: bool = field(default=False)
    children: Dict[str, 'Node'] = field(default_factory=dict)

    def __contains__(self, char: str):
        return char in self.children

    def __getitem__(self, char) -> 'Node':
        return self.children[char]

    def __setitem__(self, char, node: 'Node'):
        self.children[char] = node

    def __bool__(self):
        return bool(self.children)

    def __delitem__(self, key):
        del self.children[key]


@dataclass
class Trie:
    root: Node = field(default_factory=Node, init=False)

    def insert(self, text: str):
        """
        inserting this text into trie.
        :param text:
        """
        if not text:  # no text
            return

        current = self.root

        for c in text:
            if c in current:
                current = current[c]
            else:
                node = Node(c)
                current[c] = node
                current = node

        current.is_end_of_word = True

    def search(self, text: str):
        """
        :param text:
        :return: True if word is in this trie
        """
        return text in self

    def __contains__(self, text: str) -> bool:
        return self.__last_node(text).is_end_of_word

    def __last_node(self, text: str):
        """
        last node corresponding to text[-1] if exists, else returning root node
        :param text:
        :return:
        """
        current = self.root

        for c in text:
            if c in current:
                current = current[c]
            else:
                return self.root

        return current

    def startsWith(self, prefix: str):
        """
        :param prefix:
        :return: True if there is some text in trie having this prefix
        """
        node = self.__last_node(prefix)

        if node is self.root:
            return False

        return True

    def delete(self, text):
        """
        :param text:
        :return: True if this text exists and gets deleted else False
        """
        if not text:  # no text
            return

        stack: Deque[Node] = deque()
        stack.append(self.root)

        for c in text:
            peek = stack[-1]

            if c in peek:
                stack.append(peek[c])
            else:
                return False

        peek = stack[-1]
        peek.is_end_of_word = False

        while peek is not self.root and not peek.children and not peek.is_end_of_word:
            node = stack.pop()
            peek = stack[-1]

            del peek[node.char]

        return True
