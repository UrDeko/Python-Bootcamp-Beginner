alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift, direction):
    end_text = ""
    alphabet_length = len(alphabet)

    if shift > 26:
        shift %= 26

    if direction == "decode":
        shift *= -1

    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter) + shift
            if position >= alphabet_length and direction == "encode":
                position -= alphabet_length
            end_text += alphabet[position]
        else:
            end_text += letter

    return end_text

stop_game = False

while not stop_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(caesar(text, shift, direction))
    if input("Would you like to try again? Yes/No\n") == "No":
        stop_game = True
        print("Goodbye!")