import pytest
from data_structures101.stack import Stack

def test_stack_push_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1

def test_stack_peek():
    s = Stack()
    s.push(10)
    assert s.peek() == 10

def test_stack_empty_pop():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
