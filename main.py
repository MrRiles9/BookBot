import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import count_words, get_char_count, get_sorted_char

def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file at {filepath} was not found."
    except Exception as e:
        return f"An error ocurred: {e}"

def main():
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    
    if "Error" in book_text:
        print(book_text)
        sys.exit(1)
    
    num_words = count_words(book_text)
    char_count = get_char_count(book_text)
    sorted_chars = get_sorted_char(char_count)
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")    


if __name__ == "__main__":
    main()



