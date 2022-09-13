alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_by, input_direction):
  end_text = ""
  if input_direction == "decode":
    shift_by *= -1      
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_by
      end_text += alphabet[new_position]
    else: 
      end_text += char
  print(f"Your {input_direction}d text is:{end_text}")
      
from art import emoji
print(emoji)

  
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
      
  caesar(start_text=text, shift_by=shift,input_direction=direction)

  again = input("Type 'yes' if you want to go again. otherwise type 'no'.").lower()
  if again == "no":
    should_continue = False
    print("Have a great time!")

