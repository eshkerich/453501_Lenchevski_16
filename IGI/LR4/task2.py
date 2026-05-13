"""
Lab 4 - Task 2
Author: Lenchevski Vladimir
Date: 15.04.2026
Version: 1.0
"""
import zipfile
import os
import re
from typing import List, Tuple, Dict


def my_len(s: str) -> int:
    count = 0
    for _ in s:
        count += 1
    return count


def replace_last_three_with_dollar(text: str, target_len: int) -> str:
    """
    Replace last 3 characters of words with a given length with a single '$' symbol
    """
    result = []
    i = 0
    text_len = my_len(text)
    current_word = []

    while i < text_len:
        char = text[i]
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            current_word.append(char)
        else:
            if current_word:
                word = ''.join(current_word)
                if my_len(word) == target_len and my_len(word) >= 3:
                    result.append(word[:-3] + '$')
                else:
                    result.append(word)
                current_word = []
            result.append(char)
        i += 1

    if current_word:
        word = ''.join(current_word)
        if my_len(word) == target_len and my_len(word) >= 3:
            result.append(word[:-3] + '$')
        else:
            result.append(word)

    return ''.join(result)


def find_time_with_regex(text: str) -> List[str]:
    """
    Find all valid time strings in HH:MM format using regular expressions
    """
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
    """
    Count words that have the maximum length in the text
    """
    words = re.findall(r"[A-Za-zА-Яа-я]+", text)
    
    if not words:
        return 0
    
    max_len = max(my_len(w) for w in words)
    count = sum(1 for w in words if my_len(w) == max_len)
    
    return count


def find_words_followed_by_punct(text: str) -> List[str]:
    """
    Find all words that are immediately followed by a comma or period
    """
    pattern = r'([A-Za-zА-Яа-я]+)[,.]'
    matches = re.findall(pattern, text)
    return matches


def find_longest_word_ending_e(text: str) -> str:
    """
    Find the longest word that ends with the letter 'e'
    """
    words = re.findall(r"[A-Za-zА-Яа-я]+", text)
    
    words_ending_e = [w for w in words if w and w[-1].lower() == 'e']
    
    if not words_ending_e:
        return ""
    
    longest = max(words_ending_e, key=lambda w: my_len(w))
    return longest


def count_sentences(text: str) -> int:
    """
    Count total number of sentences in the text
    """
    sentences = re.split(r'[.!?]+[\s\n]*', text)
    sentences = [s for s in sentences if s.strip()]
    return my_len(sentences)


def count_sentences_by_type(text: str) -> Dict[str, int]:
    """
    Count declarative, interrogative, and imperative sentences
    """
    declarative = len(re.findall(r'[^.!?]*\.\s*', text))

    interrogative = len(re.findall(r'[^.!?]*\?\s*', text))

    imperative = len(re.findall(r'[^.!?]*!\s*', text))
    
    return {
        "declarative": declarative,
        "interrogative": interrogative,
        "imperative": imperative
    }


def average_sentence_length(text: str) -> float:
    """
    Calculate average sentence length in characters
    """
    sentences = re.split(r'[.!?]+[\s\n]*', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if not sentences:
        return 0.0
    
    total_word_chars = 0
    
    for sentence in sentences:
        words = re.findall(r'[A-Za-zА-Яа-я]+', sentence)
        for word in words:
            total_word_chars += my_len(word)
    
    avg = total_word_chars / my_len(sentences)
    return round(avg, 2)


def average_word_length(text: str) -> float:
    """
    Calculate average word length in characters
    """
    words = re.findall(r'[A-Za-zА-Яа-я]+', text)
    
    if not words:
        return 0.0
    
    total_length = sum(my_len(w) for w in words)
    avg = total_length / my_len(words)
    return round(avg, 2)


def count_smileys(text: str) -> int:
    """
    Count smileys in the text
    """
    pattern = r'[:;]-*([\(\)\[\]])\1*'
    matches = re.findall(pattern, text)
    return my_len(matches)


def task2():
    print("\n" + "=" * 70)
    print("=== Task 2: Text Analysis ===")
    print("=" * 70)

    os.makedirs("data", exist_ok=True)

    input_file = "data/input_text.txt"
    output_file = "data/result_text.txt"
    zip_file = "data/result_text.zip"

    with open(input_file, "r", encoding='utf-8') as f:
        input_text = f.read()

    while True:
        try:
            target_len = int(input("\nEnter word length to replace last 3 characters (minimum 3): "))
            if target_len >= 3:
                break
            else:
                print("Error: Length must be at least 3 characters!")
        except ValueError:
            print("Error: Please enter a valid integer!")

    print("\n" + "=" * 50)
    print("VARIANT 16 RESULTS")
    print("=" * 50)

    replaced_text = replace_last_three_with_dollar(input_text, target_len)
    times = find_time_with_regex(input_text)
    max_len_count = count_words_with_max_length(input_text)
    words_with_punct = find_words_followed_by_punct(input_text)
    longest_e_word = find_longest_word_ending_e(input_text)

    print(f"\n1. Text with words of length {target_len} (last 3 chars replaced by '$'):")
    print(f"{replaced_text}")
    print(f"\n2. Valid times in HH:MM format: {times}")
    print(f"\n3. Number of words with maximum length: {max_len_count}")
    print(f"\n4. Words followed by comma or period: {words_with_punct}")
    print(f"\n5. Longest word ending with 'e': '{longest_e_word}'")

    print("\n" + "=" * 50)
    print("COMMON TASKS RESULTS")
    print("=" * 50)

    total_sentences = count_sentences(input_text)
    sentences_by_type = count_sentences_by_type(input_text)
    avg_sentence_len = average_sentence_length(input_text)
    avg_word_len = average_word_length(input_text)
    smiley_count = count_smileys(input_text)

    print(f"\n1. Total number of sentences: {total_sentences}")
    print(f"\n2. Sentences by type:")
    print(f"   - Declarative: {sentences_by_type['declarative']}")
    print(f"   - Interrogative: {sentences_by_type['interrogative']}")
    print(f"   - Imperative: {sentences_by_type['imperative']}")
    print(f"\n3. Average sentence length (characters, words only): {avg_sentence_len}")
    print(f"\n4. Average word length (characters): {avg_word_len}")
    print(f"\n5. Number of smileys in the text: {smiley_count}")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 50 + "\n")
        f.write("TASK 2 RESULTS - VARIANT 16\n")
        f.write("=" * 50 + "\n\n")
        
        f.write("INDIVIDUAL TASK RESULTS:\n")
        f.write("-" * 30 + "\n")
        f.write(f"1. Text with words of length {target_len} (last 3 chars replaced by '$'):\n")
        f.write(f"{replaced_text}\n\n")
        f.write(f"2. Valid times in HH:MM format: {times}\n\n")
        f.write(f"3. Number of words with maximum length: {max_len_count}\n\n")
        f.write(f"4. Words followed by comma or period: {words_with_punct}\n\n")
        f.write(f"5. Longest word ending with 'e': {longest_e_word}\n\n")
        
        f.write("=" * 50 + "\n")
        f.write("COMMON TASKS RESULTS\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"1. Total number of sentences: {total_sentences}\n\n")
        f.write(f"2. Sentences by type:\n")
        f.write(f"   - Declarative: {sentences_by_type['declarative']}\n")
        f.write(f"   - Interrogative: {sentences_by_type['interrogative']}\n")
        f.write(f"   - Imperative: {sentences_by_type['imperative']}\n\n")
        f.write(f"3. Average sentence length (characters, words only): {avg_sentence_len}\n\n")
        f.write(f"4. Average word length (characters): {avg_word_len}\n\n")
        f.write(f"5. Number of smileys in the text: {smiley_count}\n")

    print(f"\nResults saved to: {output_file}")

    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(output_file, arcname=os.path.basename(output_file))

        info = zf.getinfo(os.path.basename(output_file))
        
        print("\n" + "=" * 50)
        print("ARCHIVE INFORMATION")
        print("=" * 50)
        print(f"Zip file created: {zip_file}")
        print(f"Original file size: {info.file_size} bytes")
        print(f"Compressed size: {info.compress_size} bytes")
        print(f"Compression ratio: {(1 - info.compress_size/info.file_size) * 100:.1f}%")
        print(f"File in archive: {info.filename}")

    print("\n" + "=" * 50)
    print("TASK 2 COMPLETED SUCCESSFULLY!")
    print("=" * 50)


if __name__ == "__main__":
    task2()