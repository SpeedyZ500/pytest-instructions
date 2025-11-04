import pytest
from example_code import add_a_and_b, PriorityQueue, LinearPQ, BinaryHeapPQ


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

@pytest.fixture(params=[LinearPQ, BinaryHeapPQ],ids=["linear","heap"])
def priority_queue(request)-> type[PriorityQueue]:
    return request.param()
    
string_data= {
    "Bill":8,
    "Jeff":5,
    "Stacy":1
}
string_data_expected = ["Stacy", "Jeff", "Bill"]
class TestPriorityQueues:
    @pytest.mark.parametrize("data", [(string_data)], ids=["str"])
    def test_priority_queue_build_pass(self,data, priority_queue):
        try:
            priority_queue.build_queue(data)
            assert True
        except Exception as e:
            pytest.fail(f"safe_function raised an unexpected exception: {e}")

    @pytest.mark.parametrize("data", [(string_data_expected)], ids=["str"])
    def test_priority_queue_build_fail(self,data, priority_queue):
        with pytest.raises(TypeError):
             priority_queue.build_queue(data)

    @pytest.mark.parametrize("data,expected", [(string_data, string_data_expected)], ids=["str"])
    def test_priority_queue_pass(self,data,expected,priority_queue):
        priority_queue.build_queue(data)
        for i in expected:
            assert i == priority_queue.delete_min()

    


    


