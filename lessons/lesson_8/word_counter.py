# write a function which recieves text different length
# returns dictionary where key is unique word and value how many times it appears
from collections import defaultdict, Counter


def get_word_count(sentence: str) -> dict:
    """
    Function which recieves text with different length
    Args:
        sentence: Sentence to count words from
    Returns:
        Dict
    """
    
    # sentence.
    splitted_sentence = sentence.replace(",", "").replace(".", "").lower().split(" ")

    dict_to_return = defaultdict(int)

    for x in splitted_sentence:
        dict_to_return[x] += 1

    return dict_to_return


print(get_word_count("Qwe asd zxc, asd"))


def get_word_count_counter(sentence: str) -> dict:
    # O(n)
    # n - words
    """
    Function which recieves text with different length
    Args:
        sentence: Sentence to count words from
    Returns:
        Dict
    """
    splitted_sentence = sentence.replace(",", "").replace(".", "").lower().split(" ")

    return Counter(splitted_sentence)

get_word_count_counter("Qwe, asd zxc asd")
