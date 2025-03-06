def get_book_text(filepath):
    try:
        with open(filepath, 'r') as file:
            book_text = file.read()
        return book_text
    except FileNotFoundError:
        return f"Error: The file at {filepath} was not found."
    except Exception as e:
        return f"An error ocurred: {e}"

def count_words(book_text):
    words = book_text.split()
    return len(words)

def main():
    file_path = 'books/frankenstein.txt'
    book_text = get_book_text(file_path)

    if "Error" not in book_text:
        num_words = count_words(book_text)
        print(f"{num_words} words found in the document")
    else:
        print(book_text)

if __name__ == "__main__":
    main()



