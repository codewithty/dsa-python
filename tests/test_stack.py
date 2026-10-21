import pytest
from structures.stack import Stack

def test_pop_on_empty_raises():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_new_stack_is_empty():
    s = Stack()
    assert s.is_empty()


def test_pop_returns_last_pushed():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2

def test_peek_does_not_remove():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert len(s) == 2
