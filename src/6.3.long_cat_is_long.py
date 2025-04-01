"""
This module processes a text input to extract unique words and their lengths.

Functions:
- long_cat_is_long(text): Takes a string of text, processes it by removing non-alphabetic characters, 
  converts it to lowercase, and returns a dictionary where each unique word is mapped to its length.
  The function performs the following:
  1. Converts the text to lowercase.
  2. Splits the text into words.
  3. Cleans each word by removing any non-alphabetic characters.
  4. Returns a dictionary with words as keys and their respective lengths as values.
"""

import string


def long_cat_is_long(text):

    """
    The function get text and create dictionary with uniqes words

    params:text
    return: dictionary that every word inside uniqe
    """

    text = text.lower()


    words = text.split()
    clean_words = []


    for word in words:
        clean_word = ''.join(char for char in word if char.isalpha())
        if clean_word:
            clean_words.append(clean_word)

    word_lengths = {}

    for word in clean_words:
        word_lengths[word] = len(word)
    return word_lengths


if __name__ == "__main__":
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """

    expected_result = {
        'you': 3, 'see': 3, 'wire': 4, 'telegraph': 9, 'is': 2, 'a': 1, 'kind': 4, 'of': 2, 'very': 4, 'long': 4,
        'cat': 3, 'pull': 4, 'his': 3, 'tail': 4, 'in': 2, 'new': 3, 'york': 4, 'and': 3, 'head': 4, 'meowing': 7,
        'los': 3, 'angeles': 7, 'do': 2, 'understand': 10, 'this': 4, 'radio': 5, 'operates': 8, 'exactly': 7,
        'the': 3, 'same': 4, 'way': 3, 'send': 4, 'signals': 7, 'here': 4, 'they': 4, 'receive': 7, 'them': 4,
        'there': 5, 'only': 4, 'difference': 10, 'that': 4, 'no': 2
    }


    result = long_cat_is_long(text)
    print(result == expected_result)
