from stack_and_queue import __version__
from stack_and_queue.stack_and_queue import Stack, Queue
import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_stack_exists():
    assert Stack

def test_stack_empty():
    stack = Stack()
    assert stack.top is None

def test_stack_push():
    stack = Stack()
    stack.push("Ball")
    actual = stack.top.value
    expected = "Ball"
    assert actual == expected

def test_stack_push_nothing_error():
    stack = Stack()
    with pytest.raises(TypeError):
        stack.push()

def test_pop_with_one_value():
    stack = Stack()
    stack.push("Ball")
    stack.pop()
    assert stack.top == None

def test_pop_with_two_values():
    stack = Stack()
    stack.push("Ball")
    stack.push("Bat")
    stack.pop()
    assert stack.top.value == "Ball"

def test_pop_with_no_values():
    stack = Stack()
    with pytest.raises(TypeError):
        stack.pop()

def test_peek_one_value():
    stack = Stack()
    stack.push("Ball")
    actual = stack.peek()
    expected = "Ball"
    assert actual == expected

def test_peek_two_values():
    stack = Stack()
    stack.push("Ball")
    stack.push("Bat")
    actual = stack.peek()
    expected = "Bat"
    assert actual == expected

def test_peek_no_values():
    stack = Stack()
    actual = stack.peek()
    expected = None
    assert actual == expected

def test_is_empty_true():
    stack = Stack()
    assert stack.is_empty() == True

def test_is_empty_false():
    stack = Stack()
    stack.push("Ball")
    assert stack.is_empty() == False

def test_is_empty_for_Bool_value_in_stack_returns_false():
    stack = Stack()
    stack.push(True)
    assert stack.is_empty() == False


def test_enqueue_one_value():
    q = Queue()
    q.enqueue('Ball')
    assert q.front.value == "Ball"

def test_enqueue_two_values():
    q = Queue()
    q.enqueue("Ball")
    q.enqueue("Bat")
    assert q.front.value =="Ball" and q.back.value == "Bat"

def test_enqueue_three_values():
    q = Queue()
    q.enqueue("Ball")
    q.enqueue("Bat")
    q.enqueue("Glove")
    assert q.front.value == "Ball" and q.back.value =="Glove"

def test_dequeue_one_value():
    q = Queue()
    q.enqueue("Ball")
    q.dequeue()
    assert q.front is None and q.back is None

@pytest.mark.skip("still needs work")
def test_dequeue_three_values():
    q = Queue()
    q.enqueue("Ball")
    q.enqueue("Bat")
    q.enqueue("Glove")
    q.dequeue()
    assert q.front == "Bat" and q.back == "Glove"

def test_peek_one_value():
    q = Queue()
    q.enqueue("Ball")
    assert q.peek() == "Ball"

def test_peek_two_value():
    q = Queue()
    q.enqueue("Ball")
    q.enqueue("Bat")
    assert q.peek() == ('Ball')

def test_queue_is_empty_true():
    q = Queue()
    assert q.is_empty() == True

def test_queue_is_empty_false():
    q = Queue()
    q.enqueue("Ball")
    assert q.is_empty() == False

