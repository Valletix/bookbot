def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_char = count_characters(text)
    dict_converted = convert_list(num_char)
    num_sorted = sort_converted(dict_converted)



    print (f"--- Begin report of {book_path} ---")
    print(f"{len(num_words)} words found in the document\n")
 
    for entry in num_sorted:
        if entry["character"].isalpha() == True:

            print(f'The \'{entry["character"]}\' character was found {entry["num"]} times')
    print (f"--- End report ---")




def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return text.split()
    

def count_characters(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def convert_list(dict):
    converted_list = []
    for e in dict:
        converted_list.append({"character":e,"num":dict[e]})
    return converted_list

def sort_on(dict):
    return dict["num"]

def sort_converted(list):
    list.sort(reverse=True, key=sort_on)
    return list



main()