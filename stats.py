from collections import Counter

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

def word_count(path_to_book):
    book_text = get_book_text(path_to_book)
    num_words = len(str.split(book_text))
    return num_words

def character_count(path_to_book):
    book_text = get_book_text(path_to_book)
    num_characters = Counter(str.lower(book_text))
    return num_characters

def characters_sorted(path_to_book):
    """
    Reads a book file, counts only alphabetical characters (case-insensitive),
    and returns a sorted list of dictionaries:
    [
        {"char": "e", "num": 44538},
        {"char": "t", "num": 29493},
        ...
    ]
    Sorted by count in descending order.
    """
    # Read and lowercase the book text
    book_text = get_book_text(path_to_book).lower()

    # Count alphabetical characters
    char_counts = {}
    for char in book_text:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1

    # Create list of {"char": ..., "num": ...}
    sorted_char_list = [{"char": char, "num": count}
                        for char, count in char_counts.items()]

    # Sort the list by count in descending order
    sorted_char_list.sort(key=lambda x: x["num"], reverse=True)

    return sorted_char_list

def Bookbot_report(path_to_book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(path_to_book)} total words")
    print("--------- Character Count -------")
    for item in characters_sorted(path_to_book):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")