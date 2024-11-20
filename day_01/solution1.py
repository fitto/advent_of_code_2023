from typing import Dict

DIGITS_ONLY = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

ALL_DIGITS = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def str_contains_one_of_substrings(this_str: str,
                                   substrings: Dict[str, int]
                                   ) -> int | None:
    for key, value in substrings.items():
        if key in this_str:
            return value
    return None


def find_coordinates(file_name: str,
                     strings_collection: Dict[str, int]
                     ) -> int | None:
    all_numbers = []

    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip()
            print(line)

            first_digit = None
            i = 1
            while first_digit is None:
                first_digit = str_contains_one_of_substrings(line[:i],
                                                             strings_collection
                                                             )
                i += 1
                if i > len(line) + 1:
                    print(f'Error - first digit not found in {line}')
                    return None

            last_digit = None
            i = 1
            while last_digit is None:
                last_digit = str_contains_one_of_substrings(line[-i:],
                                                            strings_collection
                                                            )
                i += 1
                if i > len(line) + 1:
                    print(f'Error - last digit not found in {line}')
                    return None

            new_number = first_digit * 10 + last_digit
            all_numbers.append(new_number)
            print(new_number)

        return sum(all_numbers)


print(find_coordinates('task1.txt', ALL_DIGITS))
