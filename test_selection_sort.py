from collections import Counter
from typing import List
from hypothesis import given, strategies as strategies_provider, settings
from selection_sort import selection_sort


def test_empty_sequence():
    empty_sequence: List[int] = []
    selection_sort(empty_sequence)
    assert empty_sequence == []


def test_single_element_sequence():
    single_element_sequence = [42]
    selection_sort(single_element_sequence)
    assert single_element_sequence == [42]


def test_already_sorted_sequence():
    ordered_sequence = [1, 2, 3, 4, 5, 6, 7]
    selection_sort(ordered_sequence)
    assert ordered_sequence == [1, 2, 3, 4, 5, 6, 7]


def test_reverse_sorted_sequence():
    reversed_sequence = [7, 6, 5, 4, 3, 2, 1]
    selection_sort(reversed_sequence)
    assert reversed_sequence == [1, 2, 3, 4, 5, 6, 7]


def test_sequence_with_duplicate_elements():
    duplicated_sequence = [5, 1, 3, 5, 2, 5, 1, 4]
    selection_sort(duplicated_sequence)
    assert duplicated_sequence == [1, 1, 2, 3, 4, 5, 5, 5]


def test_sequence_with_negative_numbers():
    negative_sequence = [-3, 10, -50, 0, 4, -1, 22]
    selection_sort(negative_sequence)
    assert negative_sequence == [-50, -3, -1, 0, 4, 10, 22]


def test_sequence_with_floating_point_numbers():
    floating_point_sequence = [3.1415, 2.7182, -1.4142, 0.0, 1.618]
    selection_sort(floating_point_sequence)
    assert floating_point_sequence == [-1.4142, 0.0, 1.618, 2.7182, 3.1415]


@settings(max_examples=100, derandomize=True)
@given(strategies_provider.lists(strategies_provider.integers()))
def test_selection_sort_properties_postcondition(generated_integers_list: List[int]):
    working_sequence = list(generated_integers_list)
    selection_sort(working_sequence)
    assert Counter(working_sequence) == Counter(generated_integers_list)
    assert all(
        working_sequence[element_index] <= working_sequence[element_index + 1]
        for element_index in range(len(working_sequence) - 1)
    )


@settings(max_examples=100, derandomize=True)
@given(strategies_provider.lists(strategies_provider.integers()))
def test_selection_sort_differential_against_language_reference(generated_integers_list: List[int]):
    working_sequence = list(generated_integers_list)
    selection_sort(working_sequence)
    assert working_sequence == sorted(generated_integers_list)
