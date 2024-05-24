alphabet="abcdefghijklmnopqrstuvwxyz"
new_msg=""

user_msg=input("Enter your secret message: ")
key=int(input("Enter a key: "))

for character in user_msg:
    if character in alphabet:
        position=alphabet.find(character)
        new_position=(position+key)%26
        new_char=alphabet[new_position]
        new_msg+=new_char
print("Your new message is "+new_msg)