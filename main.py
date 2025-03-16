import sys

from stats import get_num_words
from stats import count_char
from stats import sort_character_counts

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]



    text = get_book_text(book_path)
    num_words = get_num_words(text.lower())
    # print(f"{len(num_words)} words found in the document")

    chars_dict = count_char(text.lower())
    sorted_chars = sort_character_counts(chars_dict)

    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at books/frankenstein.txt...\n")
    print(f"----------- Word Count ----------\nFound {len(num_words)} total words\n")
    print(f"--------- Character Count -------\n")

    # for k, v in chars_dict.items():
    #     print(f"'{k}': {v}")

    for char_info in sorted_chars:
        print(f"{char_info['char']}: {char_info['count']}")

    print("\n============= END ===============\n")





main()
