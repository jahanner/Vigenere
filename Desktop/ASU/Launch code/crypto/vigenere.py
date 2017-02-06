from helpers import alphabet_position, rotate_character

def main():
    print(encrypt())

def encrypt():
    text = input("Type a message: ")
    key = input("Enter a key: ")
    string = ""
    i = 0
    while i <= len(key):
        for char in text:
            if i >= len(key):
                i = 0
            rotate = rotate_character(char, alphabet_position(key[i]))
            if char == " ":
                string += char
            elif char.isalpha() == False:
                string += char
            else:
                i += 1
                string += rotate
        if len(string) == len(text):
            break
    return "Your cipher is: " + string

if __name__ == '__main__':
    main()
