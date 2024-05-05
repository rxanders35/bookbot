def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_quantity = word_count(text)
    letter_quantity = letter_count(text)
    list_of_dicts = dict_to_sorted_list(letter_quantity)

    print(f"Report: {book_path}")
    print(f"The document contained {word_quantity} words.")
    print("------------")
    
    for c in list_of_dicts:
        if c['char'].isalpha():
            print(f"{c['char']} was found {c['num']} times")


def word_count(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d['num']


def dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(key=sort_on)
    return sorted_list


def letter_count(text):
    characters = {}
    for char in text:
        lowered = char.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
