import string
def count_words(book_text):
    words = book_text.split()
    return len(words)

def get_char_count(words):
    characters = {letter: 0 for letter in string.ascii_lowercase}
    characters.update({char: 0 for char in string.punctuation})
    characters[" "] = 0
    num = {char: 0 for char in string.digits}
    for char in words.lower():
        if char in characters:
            characters[char] += 1
    return characters        
        

