import sys
from stats import words_counter, char_counter, dict_to_ordered_list


def get_book_text(path):
    try:
        with open(path) as f:
            file_content = f.read()
            return file_content
    except FileNotFoundError:
        print("Can't find that book")
        sys.exit(3)
    except Exception as e:
        print(e)
        sys.exit(4)


def print_report(book_path, total_words, letters_dict):
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    letters_list = dict_to_ordered_list(letters_dict)
    for letter in letters_list:
        print(f"{letter[0]}: {letter[1]}")
    print("============= END ===============")


def sys_input():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        return sys.argv[1]
    else:
        print("Too many arguments! Usage: python3 main.py <path_to_book>")
        sys.exit(2)


def main():
    path = sys_input()
    text = get_book_text(path)
    words_num = words_counter(text)
    char_dict = char_counter(text)
    print_report(path, words_num, char_dict)

main()

