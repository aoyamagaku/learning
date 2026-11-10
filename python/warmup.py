# def count_even(numbers):
#     count = 0
#     for i in numbers:
#         if i % 2 == 0:
#             count +=1
#     return count
#
# print(count_even([1, 2, 3, 4, 6]))
# print(count_even([1, 3, 5]))
# print(count_even([]))
from dataclasses import replace


# def is_palindrome(text):
#     ready_text = text.replace(" ", "").lower()
#     reverse_text = ready_text[::-1]
#     if ready_text == reverse_text:
#         return True
#     else:
#         return False
#
# print(is_palindrome("шалаш"))
# print(is_palindrome("А роза упала на лапу Азора"))
# print(is_palindrome("Python"))

# def most_common_word(text):
#     text = text.lower()
#     text_dict = {}
#     for i in text.split():
#         if i in text_dict:
#             text_dict[i] += 1
#         else:
#             text_dict[i] = 1
#
#     best_word = None
#     best_count = 0
#     for key in text_dict:
#         if text_dict[key] > best_count:
#             best_word = key
#             best_count = text_dict[key]
#     return best_word
#
# print(most_common_word("кот пёс кот рыба Кот пёс"))

