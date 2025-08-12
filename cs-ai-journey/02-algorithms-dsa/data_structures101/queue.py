from __future__ import annotations
from collections import deque
from typing import Deque, Generic, TypeVar

T = TypeVar("T")

class Queue(Generic[T]):
    """Fila FIFO baseada em collections.deque.

    Operações:
      - enqueue(item): O(1)
      - dequeue(): O(1)
      - is_empty(): O(1)
      - size()/len(): O(1)
    """

    def __init__(self) -> None:
        self.items: Deque[T] = deque()

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("Queue.dequeue: empty queue")
        return self.items.popleft()

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
        return f"Queue({list(self.items)!r})"
