#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TASK 4
Author: Lenchevski Vladimir
Date: 15.03.2026
Version: 1.0
"""

import string
from decorators import timer_decorator, log_decorator
from validation import repeat_program

ALICE_TEXT = """So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."""


def clean_word(word):
    """
    Clean a word by removing punctuation from both ends.
    """
    return word.strip(string.punctuation + '"\'')


def is_vowel(char):
    """
    Check if a character is a vowel (English).
    """
    return char.lower() in 'aeiouy'


def ends_with_consonant(word):
    """
    Check if a word ends with a consonant (not a vowel).
    """
    cleaned = clean_word(word)
    if not cleaned:
        return False

    last_char = cleaned[-1]
    return last_char.isalpha() and not is_vowel(last_char)


def get_words(text):
    """
    Extract words from text, preserving order.
    """
    raw_words = text.split()
    words = []

    for raw_word in raw_words:
        cleaned = clean_word(raw_word)
        if cleaned:
            words.append(cleaned)

    return words


@timer_decorator
@log_decorator
def task4():
    """
    Main function for Task 4.
    Analyzes quote according to variant 16 requirements.
    """
    print("\n" + "=" * 60)
    print("TASK 4: Analysis of Quote")
    print("Variant 16:")
    print("a) Count words ending with consonant")
    print("b) Find average word length, display words with that length")
    print("c) Display every 7th word")
    print("=" * 60)

    while True:
        try:
            print("\n" + "=" * 50)
            print("Original Text:")
            print("=" * 50)
            print(ALICE_TEXT)
            print("=" * 50)

            # Get words from text
            words = get_words(ALICE_TEXT)

            if not words:
                print("No words found in text.")
                return

            print(f"\nTotal words found: {len(words)}")

            consonant_words = [w for w in words if ends_with_consonant(w)]

            print("\n" + "-" * 50)
            print("a) Words ending with consonant:")
            print(f"   Count: {len(consonant_words)} out of {len(words)} words")

            if len(consonant_words) <= 20:
                print("   Words ending with consonant:", ", ".join(consonant_words))
            else:
                print("   First 20 words ending with consonant:", ", ".join(consonant_words[:20]), "...")

            word_lengths = [len(w) for w in words]
            avg_length = sum(word_lengths) / len(words)
            rounded_avg = round(avg_length)

            print("\n" + "-" * 50)
            print("b) Average word length:")
            print(f"   Average length: {avg_length:.2f}")
            print(f"   Rounded to integer: {rounded_avg}")

            words_with_avg_length = [w for w in words if len(w) == rounded_avg]

            if words_with_avg_length:
                print(f"   Words with length {rounded_avg}:")
                print("   " + ", ".join(words_with_avg_length))
            else:
                print(f"   Слов длиной {rounded_avg} символов в строке нет")

            print("\n" + "-" * 50)
            print("c) Every 7th word:")

            seventh_words = []
            for i, word in enumerate(words, 1):
                if i % 7 == 0:
                    seventh_words.append(f"{i}. {word}")

            if seventh_words:
                print("   " + "\n   ".join(seventh_words))
            else:
                print("   No words found at positions that are multiples of 7")

            print("\n" + "-" * 50)
            print("Additional Statistics:")
            print(f"   Shortest word length: {min(word_lengths)}")
            print(f"   Longest word length: {max(word_lengths)}")

            length_dist = {}
            for length in word_lengths:
                length_dist[length] = length_dist.get(length, 0) + 1

            print("\n   Word length distribution:")
            for length in sorted(length_dist.keys()):
                print(f"     Length {length}: {length_dist[length]} word(s)")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            return
        except Exception as e:
            print(f"Unexpected error: {e}")

        if not repeat_program():
            break


if __name__ == "__main__":
    task4()