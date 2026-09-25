from typing import List


def sort_words(words: List[str]) -> List[str]:
    def words_len(words):
        return len(words)
    words.sort(key=words_len, reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    def num_len(numbers):
        return abs(numbers)
    numbers.sort(key=num_len)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
