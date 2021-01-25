alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def decode(plain_text, shift_amount):
    new_string = ""
    for letter in plain_text:
       index_value = alphabet.index(letter) + 26
       shifted_index = index_value - shift_amount
       new_string += alphabet[shifted_index]
    print(new_string)



def encrypt(plain_text, shift_amount):
    new_string = ""
    for letter in plain_text:
       index_value = alphabet.index(letter)
       shifted_index = index_value + shift_amount
       new_string += alphabet[shifted_index]
    print(new_string)

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decode(plain_text=text, shift_amount=shift)
    
    



