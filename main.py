from stats import count_words, get_char_count

def get_book_text(filepath):
    try:
        with open(filepath, 'r') as file:
            book_text = file.read()
        return book_text
    except FileNotFoundError:
        return f"Error: The file at {filepath} was not found."
    except Exception as e:
        return f"An error ocurred: {e}"

def main():
    file_path = 'books/frankenstein.txt'
    book_text = get_book_text(file_path)
    char_count = get_char_count(book_text)
    if "Error" not in book_text:
        num_words = count_words(book_text)
        print(f"{num_words} words found in the document")
        for char, count in sorted(char_count.items()):
            print(f"'{char}': {count}")
    else:
        print(book_text)

if __name__ == "__main__":
    main()



