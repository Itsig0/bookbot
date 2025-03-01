from stats import get_word_cound, get_character_count, sort_character_count
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    count = get_word_cound(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    
    char_count = sort_character_count(get_character_count(book_text))
    
    for key, count in char_count:
        if key.isalpha():
            print(f"{key}: {count}")

    print("============= END ===============")
main()
