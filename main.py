
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    #print("test")
    #print(f"{count_words(file_contents)} is the word count")
    print(f"the results are:") 
    char_count = character_count(file_contents)
    for character in sorted(char_count):
        print(f"'{character}': {char_count[character]}")    
    
    '''for character, count in char_count.items():
        print(f"'{character}': {count}")
'''


        

def count_words(book):
    words = book.split()
    return len(words)

def character_count(text):
    char_count = {}
    text_low = text.lower()
    for character in text_low:
        if character not in char_count:
            char_count[character] = 1
        else:
            char_count[character] += 1
    return char_count
    

      
    ''' 
        if character == (for key in character_count):
            key.value += 1
        else 
    '''     





main()

