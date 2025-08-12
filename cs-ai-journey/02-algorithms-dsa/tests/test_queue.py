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


# ---- Novos testes ----
def test_queue_len_bool_and_size():
    q = Queue()
    assert len(q) == 0
    assert not q
    assert q.size() == 0

    q.enqueue(1)
    q.enqueue(2)
    assert len(q) == 2
    assert q
    assert q.size() == 2


def test_queue_interleaved_ops():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1

    q.enqueue(4)
    assert [q.dequeue(), q.dequeue(), q.dequeue()] == [2, 3, 4]
    assert q.is_empty()
