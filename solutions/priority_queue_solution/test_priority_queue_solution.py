import pytest
from .priority_queue_solution import PriorityQueue, LinearPQ, BinaryHeapPQ

@pytest.fixture(params=[LinearPQ, BinaryHeapPQ],ids=["linear","heap"])
def priority_queue(request)-> PriorityQueue:
    return request.param()
    
string_data= {
    "Bill":8,
    "Jeff":5,
    "Stacy":1
}

queue_fallback = {
        "A": 5,
        "B": 5,
        "C": 5,
        "D": 5,
        "E": 5,
    }
queue_fallback_expected = ["A","B","C","D","E"]


string_data_expected = ["Stacy", "Jeff", "Bill"]

test_list= [
    "str",
    "queue_fallback"
]

tests = [
    (string_data, string_data_expected),
    (queue_fallback, queue_fallback_expected)
]


@pytest.mark.parametrize("data,expected", tests, ids=test_list)
class TestPriorityQueues:
    # @pytest.mark.parametrize("data", [(string_data)], ids=["str"])
    def test_priority_queue_build_pass(self,data, expected, priority_queue):
        try:
            priority_queue.build_queue(data)
            assert True
        except Exception as e:
            pytest.fail(f"safe_function raised an unexpected exception: {e}")

    # @pytest.mark.parametrize("data", [(string_data_expected)], ids=["str"])
    def test_priority_queue_build_fail(self,data, expected, priority_queue):
        with pytest.raises(TypeError):
             priority_queue.build_queue(expected)
    # @pytest.mark.parametrize("data,expected", [(string_data, string_data_expected)], ids=["str"])
    def test_priority_queue_pass(self,data,expected,priority_queue):
        priority_queue.build_queue(data)
        for i in expected:
            assert i == priority_queue.delete_min()