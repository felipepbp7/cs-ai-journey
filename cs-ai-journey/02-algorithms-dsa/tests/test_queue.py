import pytest
from data_structures101.queue import Queue

def test_queue_enqueue_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2

def test_queue_empty_dequeue():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()
