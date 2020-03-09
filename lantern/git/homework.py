from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    if first == second:
        return True
    else:
        return False


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    if type(first) == type(second):
        return True
    else:
        return False


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    if first is second:
        return True
    else:
        return False


def multiple_ints(first_value: int, second_value: int) -> int:
    if type(first_value * second_value) == int:
        return first_value * second_value
    else:
        raise TypeError




def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    # if type(first_value) and type(second_value) != int:
    return (int(first_value) * int(second_value))
    # else:
    # raise ValueError('Not valid input data')


# """
# If possible to convert arguments to int value - convert and multiply them.
# If it is impossible raise ValueError
#
# Args:
#     first_value: number for multiply
#     second_value: number for multiply
#
# Raises:
#     ValueError
#
# Returns: multiple of two numbers.
#
# Examples:
#     multiple_ints_with_conversion(6, 6)
#     >>> 36
#     multiple_ints_with_conversion(2, 2.0)
#     >>> 4
#     multiple_ints_with_conversion("12", 1)
#     >>> 12
#     try:
#         multiple_ints_with_conversion("Hello", 2)
#     except ValueError:
#         print("Not valid input data")
#     >>> "Not valid input data"
# """


def is_word_in_text(word: str, text: str) -> bool:
    if text.find(word) != -1:
        # words = text.split(' ')
        # for i in words:
        #     if word==i:
        return True
    else:
        return False

    # """
    # If text contain word return True
    # In another case return False.
    #
    # Args:
    #     word: Searchable substring
    #     text: Text for search
    #
    # Examples:
    #     is_word_in_text("Hello", "Hello word")
    #     >>> True
    #     is_word_in_text("Glad", "Nice to meet you ")
    #     >>> False
    #
    # """


def some_loop_exercise() -> list:
    lis = []
    for i in range(13):
        lis.append(i)
        if i == 6 or i == 7:
            lis.remove(i)

    return lis

    # """
    # Use loop to create list that contain int values from 0 to 12 except 6 and 7
    # """


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    temp = []
    for i in range(len(data)):
        if data[i] >= 0:
            temp.append(data[i])

    return temp

    # """
    # Use loops to solve this task.
    # You could use data.remove(negative_number) to solve this issue.
    # Also you could create new list with only positive numbers.
    # Examples:
    #     remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
    #     >>> [1, 5, 8]
    # """


# remove_from_list_all_negative_numbers([1, 2, -9, 6, 7, 6, -19, -12])


def alphabet() -> dict:
    dic = {}
    letter = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(1, len(letter) + 1):
        dic[i] = letter[i - 1]

    return (dic)

    # """
    # Create dict which keys are alphabetic characters. And values their number in alphabet
    # Notes You could see an implementaion of this one in test, but create another one
    # Examples:
    #     alphabet()
    #     >>> {"a": 1, "b": 2 ...}
    # """


# alphabet()


def simple_sort(data: List[int]) -> List[int]:
    for i in range(0, len(data) - 1):
        for j in range(0, len(data) - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j], data[j + 1] = data[j + 1], temp

    return data

    # """
    # Sort list of ints without using built-in methods.
    # Examples:
    #     simple_sort([2, 9, 6, 7, 3, 2, 1])
    #     >>> [1, 2, 2, 3, 6, 7, 9]
    # """
