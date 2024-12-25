
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    #print("test")
    print("--- Begin report of books/frankenstein.txt ---") 
    print(f"{count_words(file_contents)} words in the document")
    
    char_count = character_count(file_contents)
    
    char_list = []
    for char, count in char_count.items():   #iterates over each key, value in dictionary "char_count" using items() function
        new_dict = {"char": char, "num": count}   #creates new dictionary with key char and key num 
        char_list.append(new_dict)  #adds new dictionaries to a list

    #sort using lamba short function to identify char key as the comparison variable  and putting them in reverse order just to try it out
    char_list.sort(key=lambda x: x['char'], reverse=True)
     
    for char_dict in char_list:
        print(f"The letter '{char_dict['char']}' appears {char_dict['num']} times in the document") 

    # working version sans list below
    '''
    for character in sorted(char_count):
        if character.isalpha():
            print(f"The character '{character}' was found {char_count[character]} times") 
    '''        
    


    print("--- End report ---")
    '''for character, count in char_count.items():
        print(f"'{character}': {count}")
'''


        

def count_words(book):
    words = book.split()
    return len(words)

# old function before adding isalpha 
'''
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
def character_count(text):
    char_count = {}
    text_low = text.lower()
    for character in text_low:
        if character.isalpha():  # only count alphabet characters
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

