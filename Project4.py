#Caeser Cipher secret encoding decoding project:-
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
text=input("Type your message: \n").lower()
shift=int(input("Type the shift number: \n"))

def encrypt(plain_text,shift_amount):
    cipher_text=" "
    for letter in plain_text:
        position=alphabet.index(letter)   # in hello,position of h is 7
        new_position=position+shift_amount # eg shift position is 5 so 7+5=12
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text,shift_amount):
    plain_text=" "
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position-shift_amount
        plain_text+=alphabet[new_position]
    print(f"The decoded text is {plain_text}")

if direction=="encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction=="decode":
    decrypt(cipher_text=text,shift_amount=shift)
'''
# reorganizing our data in a single function

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


from art_cipher import logo
print(logo)
 

def caeser(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
            shift_amount*= -1    # eg 5* -1= -5
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position+shift_amount  # 12-5=7
            end_text+=alphabet[new_position]
        else:
             end_text += char
    print(f"The {cipher_direction} text is {end_text}")


should_continue=True
while should_continue:
    direction=input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
    text=input("Type your message: \n").lower()
    shift=int(input("Type the shift number: \n"))
    shift=shift%26

    caeser(start_text=text,shift_amount=shift,cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")