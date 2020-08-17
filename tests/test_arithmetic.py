import pytest
from src.arithmetic import number_of_ways_to_climb_staircase


@pytest.mark.parametrize('n,expected', [
    (4, 5)
])
def test_default_number_of_ways_to_climb_staircase(n,expected):
    result = number_of_ways_to_climb_staircase(n)
    assert expected == result


@pytest.mark.parametrize('n,x,expected', [
    (4, set([1, 2]), 5)
])
def test_number_of_ways_to_climb_staircase(n,x,expected):
    result = number_of_ways_to_climb_staircase(n, x)
    assert expected == result
