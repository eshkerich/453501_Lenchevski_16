"""
Lab 4 - Task 2
Author: Lenchevski Vladimir
Date: 15.04.2026
Version: 1.0
"""
import zipfile
import os
import re
from typing import List

def my_len(s: str) -> int:
    count = 0
    for _ in s:
        count += 1
    return count

def replace_last_three_with_dollar(text: str, target_len: int) -> str:
    result = []
    i = 0
    text_len = my_len(text)
    current_word = []

    while i < text_len:
        if ('a' <= text[i] <= 'z') or ('A' <= text[i] <= 'Z'):
            current_word.append(text[i])
        else:
            if current_word:
                word = ''.join(current_word)
                if my_len(word) == target_len and my_len(word) >= 3:
                    result.append(word[:-3] + '$$$')
                else:
                    result.append(word)
                current_word = []
            result.append(text[i])
        i += 1

    if current_word:
        word = ''.join(current_word)
        if my_len(word) == target_len and my_len(word) >= 3:
            result.append(word[:-3] + '$$$')
        else:
            result.append(word)

    return ''.join(result)

def find_time_with_regex(text: str) -> List[str]:
    pattern = r'\b\d{2}:\d{2}\b'
    matches = re.findall(pattern, text)

    valid_times = []
    for match in matches:
        hours = int(match[:2])
        minutes = int(match[3:])
        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            valid_times.append(match)

    return valid_times

def count_words_with_max_length(text: str) -> int:
    words = []
    i = 0
    text_len = my_len(text)
    current_word = []
    while i < text_len:
        if ('a' <= text[i] <= 'z') or ('A' <= text[i] <= 'Z'):
            current_word.append(text[i])
        else:
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        i += 1
    if current_word:
        words.append(''.join(current_word))

    if not words:
        return 0

    max_len = 0
    for w in words:
        w_len = my_len(w)
        if w_len > max_len:
            max_len = w_len

    count = 0
    for w in words:
        if my_len(w) == max_len:
            count += 1
    return count

def find_words_followed_by_punct(text: str) -> List[str]:
    words = []
    i = 0
    text_len = my_len(text)
    current_word = []

    while i < text_len:
        if ('a' <= text[i] <= 'z') or ('A' <= text[i] <= 'Z'):
            current_word.append(text[i])
        else:
            if current_word:
                if i < text_len and (text[i] == ',' or text[i] == '.'):
                    words.append(''.join(current_word))
            current_word = []
        i += 1

    return words

def find_longest_word_ending_e(text: str) -> str:
    longest_word = ""
    i = 0
    text_len = my_len(text)
    current_word = []

    while i < text_len:
        if ('a' <= text[i] <= 'z') or ('A' <= text[i] <= 'Z'):
            current_word.append(text[i])
        else:
            if current_word:
                word = ''.join(current_word)
                last_char = word[my_len(word) - 1] if my_len(word) > 0 else ''
                if last_char == 'e' or last_char == 'E':
                    if my_len(word) > my_len(longest_word):
                        longest_word = word
            current_word = []
        i += 1

    if current_word:
        word = ''.join(current_word)
        last_char = word[my_len(word) - 1] if my_len(word) > 0 else ''
        if last_char == 'e' or last_char == 'E':
            if my_len(word) > my_len(longest_word):
                longest_word = word

    return longest_word

def task2():
    print("\n" + "=" * 60)
    print("=== Task 2: Text Analysis ===")
    print("=" * 60)

    os.makedirs("data", exist_ok=True)

    test_text = """Hello world! How are you? I'm fine, thanks. The time is 14:30 and 23:45.
    The longest word ending with e is apple or maybe orange. 
    Some words: abcdef, test. Another example: hello, world.
    Short words: a, b, c. Longest word example: extraordinary.
    """

    input_file = "data/input_text.txt"
    output_file = "data/result_text.txt"
    zip_file = "data/result_text.zip"

    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(test_text)

    print(f"\nInput file saved: {input_file}")
    print("\n--- Original Text ---")
    print(test_text)

    target_length = 5
    replaced_text = replace_last_three_with_dollar(test_text, target_length)
    times = find_time_with_regex(test_text)
    max_len_count = count_words_with_max_length(test_text)
    words_with_punct = find_words_followed_by_punct(test_text)
    longest_e_word = find_longest_word_ending_e(test_text)

    print("\n" + "=" * 40)
    print("TASK 2 RESULTS")
    print("=" * 40)

    print(f"\n1. Text with words of length {target_length} (last 3 chars replaced by '$$$'):")
    print(f"{replaced_text}")
    print(f"\n2. Times in HH:MM format: {times}")
    print(f"\n3. Number of words with maximum length: {max_len_count}")
    print(f"\n4. Words followed by comma or period: {words_with_punct}")
    print(f"\n5. Longest word ending with 'e': '{longest_e_word}'")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("TASK 2 RESULTS\n\n")
        f.write(f"1. Text with words of length {target_length} (last 3 chars replaced by '$$$'):\n")
        f.write(f"{replaced_text}\n\n")
        f.write(f"2. Times in HH:MM format: {times}\n\n")
        f.write(f"3. Number of words with maximum length: {max_len_count}\n\n")
        f.write(f"4. Words followed by comma or period: {words_with_punct}\n\n")
        f.write(f"5. Longest word ending with 'e': {longest_e_word}\n")

    with zipfile.ZipFile(zip_file, 'w') as zf:
        zf.write(output_file, arcname="result_text.txt")
        info = zf.getinfo("result_text.txt")
        print(f"\nZip file created: {zip_file}")
        print(f"Compressed: {info.compress_size} bytes, Original: {info.file_size} bytes")