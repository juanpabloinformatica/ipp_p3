"""
return an anagram phrase
"""
from collections import Counter

from load_dictionary import dictionary2list


def word_in_phrase(word: dict, phrase_dict: dict):
    for key in word.keys():
        if key not in phrase_dict:
            return False
    for key in phrase_dict.keys():
        if phrase_dict[key] < word[key]:
            return False
    return True


def generate_anagrams(phrase_dict, words, TOPE) -> list:
    anagrams = []
    for word in words:
        word_dict = word2dict(word)
        if word_in_phrase(word_dict, phrase_dict):
            anagrams.append(word)
    return anagrams[:TOPE]


def update_phrase_dict(phrase_dict: dict, anagram_phrase: str):
    anagram_phrase_dict = word2dict(format_phrase(anagram_phrase))
    for key in phrase_dict.keys():
        print(f"{key}: {anagram_phrase_dict[key]}")
        new_value = phrase_dict[key] - anagram_phrase_dict[key]
        phrase_dict[key] = new_value


def get_word_in_list() -> int:
    return int(input("select number of word u want to add to your phrase: "))


def pick_word(anagrams: list) -> str:
    for index, word in enumerate(anagrams):
        print(f"{index}: {word}", end=", ")
    print("\n")
    return anagrams[get_word_in_list()]


def get_input_phrase() -> str:
    return input("Write the phrase to get anagrams: ")


def word2dict(word: str) -> dict:
    return Counter(word)


def format_phrase(phrase: str) -> str:
    return ("".join(phrase.replace(" ", ""))).lower()


def update_words(words, new_anagram: str) -> list[str]:
    words = list(filter(lambda word: word not in new_anagram, words))
    return words


def still_letters(phrase_dict: dict):
    return True if len(phrase_dict) > 0 else False


def remove_used_letters(phrase_dict: dict):
    keys_to_remove = []
    for key in phrase_dict.keys():
        if phrase_dict[key] == 0:
            keys_to_remove.append(key)
    for key in keys_to_remove:
        del phrase_dict[key]


def main() -> None:
    """
    Entry point
    """
    words = dictionary2list()
    new_anagram = ""
    phrase = get_input_phrase()
    phrase = format_phrase(phrase)
    phrase_dict = word2dict(phrase)
    print(f"first {phrase_dict}\n")
    TOPE = 10
    anagrams = generate_anagrams(phrase_dict, words, TOPE)
    while True:
        if len(anagrams) > 0:
            picked_word = pick_word(anagrams)
        else:
            print("no more anagrams")
            break
        new_anagram += f"{picked_word} "
        # update_words(words, new_anagram)
        update_phrase_dict(phrase_dict, new_anagram)
        remove_used_letters(phrase_dict)
        anagrams = generate_anagrams(phrase_dict,words,TOPE)
        print(f"updated {phrase_dict}\n")
        if still_letters(phrase_dict) and len(anagrams)>0:
            condition = int(input("do u want to continue playing:\n1 yes, 2 no:  "))
            if condition == 1 and still_letters(phrase_dict):
                continue
            else:
                print("User decided to stop.")
                break
        else:
            print("no more possible combinations")
            break
    print(f"Here is your new anagram:\t{new_anagram}")


if __name__ == "__main__":
    main()
