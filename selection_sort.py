from typing import List, Any


def selection_sort(the_sequence: List[Any]) -> None:
    total_elements = len(the_sequence)
    for outer_index in range(total_elements - 1):
        minimum_element_index = outer_index
        for inner_index in range(outer_index + 1, total_elements):
            if the_sequence[inner_index] < the_sequence[minimum_element_index]:
                minimum_element_index = inner_index

        if minimum_element_index != outer_index:
            temporary_value = the_sequence[outer_index]
            the_sequence[outer_index] = the_sequence[minimum_element_index]
            the_sequence[minimum_element_index] = temporary_value
