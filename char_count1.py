
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    #print("test")
    print("--- Begin report of books/frankenstein.txt ---") 
    print(f"{count_words(file_contents)} words in the document")
    
    char_count = character_count(file_contents)
    
    for character in sorted(char_count):
        if character.isalpha():
            print(f"The character '{character}' was found {char_count[character]} times") 
            
    


    print("--- End report ---")
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

