def count_numbers_and_strings(data_structure):
    total_numbers = 0
    total_string_lengths = 0

    def traverse(element):
        nonlocal total_numbers, total_string_lengths

        if isinstance(element, (list, tuple, set)):
            for item in element:
                traverse(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                traverse(key)
                traverse(value)
        elif isinstance(element, int):
            total_numbers += element
        elif isinstance(element, str):
            total_string_lengths += len(element)

    traverse(data_structure)

    return total_numbers, total_string_lengths


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_numbers, total_string_lengths = count_numbers_and_strings(data_structure)
print(f"Total numbers: {total_numbers}")
print(f"Total string lengths: {total_string_lengths}")