from stats import get_book_text, word_count, character_count, characters_sorted, Bookbot_report
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

Bookbot_report(path_to_book)


