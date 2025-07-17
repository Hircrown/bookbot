from stats import words_counter, char_counter, dict_to_ordered_list

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content


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



def main():
    text = get_book_text("books/frankenstein.txt")
    words_num = words_counter(text)
    char_dict = char_counter(text)
    print_report("books/frankenstein.txt", words_num, char_dict)

main()
