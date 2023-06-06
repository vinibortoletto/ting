from ting_file_management.priority_queue import PriorityQueue
import pytest


@pytest.fixture
def regular_priority_item():
    return {
        "nome_do_arquivo": "mock_file_path.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": ["line", "line", "line", "line", "line"],
    }


@pytest.fixture
def high_priority_item():
    return {
        "nome_do_arquivo": "mock_file_path.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["line", "line", "line", "line"],
    }


def test_basic_priority_queueing(regular_priority_item, high_priority_item):
    queue = PriorityQueue()

    # test is_priority()
    is_priority = queue.is_priority(regular_priority_item)
    assert is_priority is False

    is_priority = queue.is_priority(high_priority_item)
    assert is_priority is True

    # test enqueue()
    queue.enqueue(regular_priority_item)
    assert len(queue.regular_priority) == 1

    queue.enqueue(high_priority_item)
    assert len(queue.high_priority) == 1

    # test dequeue()
    queue.dequeue()
    queue.dequeue()
    assert len(queue.regular_priority) == 0
    assert len(queue.high_priority) == 0

    # test search()
    queue.enqueue(regular_priority_item)
    queue.enqueue(high_priority_item)

    assert queue.search(1) == regular_priority_item
    assert queue.search(0) == high_priority_item

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(999)
