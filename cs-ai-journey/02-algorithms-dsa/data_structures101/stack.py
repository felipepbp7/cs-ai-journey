from __future__ import annotations
from typing import Generic, List, TypeVar

T = TypeVar("T")

class Stack(Generic[T]):
    """Pilha LIFO simples baseada em list.

    Operações:
      - push(item): O(1) amortizado
      - pop(): O(1)
      - peek(): O(1)
      - is_empty(): O(1)
      - size()/len(): O(1)
    """

    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Stack.pop: empty stack")
        return self.items.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Stack.peek: empty stack")
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)

    # Pythonic
    def __len__(self) -> int:
        return len(self.items)

    def __bool__(self) -> bool:
        return not self.is_empty()

    def __repr__(self) -> str:
        return f"Stack({self.items!r})"
