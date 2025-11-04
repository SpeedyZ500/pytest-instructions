import pytest
from example_code import add_a_and_b, PriorityQueue, LinearPQ, BinaryHeapPQ, same_signs


def test_add_a_and_b_both_numeric():
    #Given
    a = 5
    b = 12.0
    expected = 17.0

    #Then
    result = add_a_and_b(a, b)
    assert result == expected

def test_add_a_and_b_not_numeric_reject():
    #Given
    a = [1,3,5]
    b = "whatever"

    #Then
    with pytest.raises(TypeError):
        add_a_and_b(a, b)

class TestAddAB:
    def test_add_a_and_b_both_numeric(self):
        #Given
        a = 5
        b = 12.0
        expected = 17.0
        #Then
        result = add_a_and_b(a, b)
        assert result == expected

    def test_add_a_and_b_not_numeric_reject(self):
        #Given
        a = [1,3,5]
        b = "whatever"
        #Then
        with pytest.raises(TypeError):
            add_a_and_b(a, b)



class TestClassExample:
    value = 1
    def test_class_example_1(self):
        self.value = 2
        assert self.value == 2
    def test_class_example_2(self):
        assert self.value == 1

@pytest.mark.parametrize("a",["stuff", ["things", "nonsense"], (1,2)])
def test_same_signs_incompatible(a):
    with pytest.raises(TypeError):
        same_signs(a,a)

@pytest.mark.parametrize("a",[1, 2, 3, 5, 2.3])
@pytest.mark.parametrize("b",[0, 1, 2, 3, 5, 2.3, float('inf')])
def test_same_signs_positive_positive(a, b):
    assert same_signs(a, b)

@pytest.mark.parametrize("a",[-1, -2, -3, -5, -2.3])
@pytest.mark.parametrize("b",[ -1, -2, -3, -5, -2.3, -float('inf')])
def test_same_signs_negative_positive(a, b):
    assert same_signs(a, b)

@pytest.mark.parametrize("a",[1, 2, 3, 5, 2.3])
@pytest.mark.parametrize("b",[-1, -2, -3, -5, -2.3])
def test_same_signs_not_same_signs(a, b):
    assert not same_signs(a, b)



@pytest.fixture(params=[LinearPQ, BinaryHeapPQ],ids=["linear","heap"])
def priority_queue(request)-> type[PriorityQueue]:
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

    


    


