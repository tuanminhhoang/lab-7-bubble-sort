import pytest

from main import bbs


@pytest.fixture
def sample_numbers():
    return [5, 1, 4, 2, 8]


def test_bbs_sorts_unsorted_list(sample_numbers):
    result = bbs(sample_numbers)
    assert result == [1, 2, 4, 5, 8]


def test_bbs_handles_already_sorted_list():
    numbers = [1, 2, 3, 4]
    result = bbs(numbers)
    assert result == [1, 2, 3, 4]


def test_bbs_handles_duplicates_and_negatives():
    numbers = [3, -1, 3, 2, -1]
    result = bbs(numbers)
    assert result == [-1, -1, 2, 3, 3]


def test_bbs_handles_empty_list():
    numbers = []
    result = bbs(numbers)
    assert result == []


def test_bbs_sorts_in_place_and_returns_same_list_object():
    numbers = [4, 3, 2, 1]
    result = bbs(numbers)
    assert result is numbers
    assert numbers == [1, 2, 3, 4]
