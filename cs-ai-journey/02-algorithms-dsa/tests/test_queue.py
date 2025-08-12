def test_queue_len_bool_and_size():
    q = Queue()
    assert len(q) == 0 and (not q) and q.size() == 0
    q.enqueue(1); q.enqueue(2)
    assert len(q) == 2 and q and q.size() == 2

def test_queue_interleaved_ops():
    q = Queue()
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    assert q.dequeue() == 1
    q.enqueue(4)
    assert [q.dequeue(), q.dequeue(), q.dequeue()] == [2, 3, 4]
    assert q.is_empty()
