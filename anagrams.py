"""
Anagrams of a word

"""
from collections import Counter


from load_dictionary import dictionary2list


def get_anagrams(word_input: str, words: list) -> list:
    """
    Get anagram of a word
    """
    anagrams = []
    word_dict = Counter(word_input)
    for word in words:
        if Counter(word) == word_dict:
            print(word)
            anagrams.append(word)
    return anagrams


def main() -> None:
    """
    Entry point
    """
    word_input = input("Write word:\t")
    words = dictionary2list()
    anagrams = get_anagrams(word_input, words)
    print(anagrams)
    pass


if __name__ == "__main__":
    main()
