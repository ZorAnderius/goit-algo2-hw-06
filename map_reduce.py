import string
from collections import defaultdict
from concurrent.futures.thread import ThreadPoolExecutor


def remove_punctuation(text: str):
    return text.translate(str.maketrans('', '', string.punctuation))

def map_function(word: str) -> (str, int):
    return word, 1

def shuffle_function(mapped_value):
    shuffled = defaultdict(list)
    for key, value in mapped_value:
        shuffled[key].append(value)
    return shuffled.items()

def reduce_function(shuffled_value):
    key, value = shuffled_value
    return key, sum(value)

def map_reduce(text: str):
    text = remove_punctuation(text)
    words = text.split()
    with ThreadPoolExecutor() as executor:
        mapped = list(executor.map(map_function, words))

    shuffled = shuffle_function(mapped)

    with ThreadPoolExecutor() as executor:
        reduced_values = list(executor.map(reduce_function, shuffled))
    return dict(reduced_values)
