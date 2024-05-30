def merge_sorted_arrays(arr1, arr2):
    merged_array = sorted(arr1 + arr2)
    return merged_array

array1 = [1, 3, 4, 5]
array2 = [2, 4, 6, 8]
merged_result = merge_sorted_arrays(array1, array2)
print(f"Merged array: {merged_result}")


def remove_duplicates_list(numbers):
    return list(set(numbers))

integer_list = [5, 2, 9, 1, 7, 2, 5]
unique_list = remove_duplicates_list(integer_list)
print("List without duplicates:", unique_list)


def reverse_words(sentence):
    words = sentence.split()
    reversed_words = " ".join(reversed(words))
    return reversed_words

user_sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(user_sentence)
print("Reversed sentence:", reversed_sentence)


