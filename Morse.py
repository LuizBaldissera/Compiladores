MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

def text_to_morse(text):
    morse = ''
    try:
        for char in text.upper():
            if char in MORSE_CODE_DICT:
                morse += MORSE_CODE_DICT[char] + ' '
            else:
                raise ValueError(f"Character '{char}' not found in Morse code dictionary")
        return morse.strip()
    except Exception as e:
        return str(e)

def morse_to_text(morse):
    text = ''
    try:
        morse_chars = morse.split(' ')
        reverse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
        for code in morse_chars:
            if code in reverse_dict:
                text += reverse_dict[code]
            elif code == '':
                text += ' '
            else:
                raise ValueError(f"Invalid Morse code sequence: '{code}'")
        return text
    except Exception as e:
        return str(e)

def main():
    while True:
        print("\n1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            text = input("Enter text to convert: ")
            print("Morse code:", text_to_morse(text))
        elif choice == '2':
            morse = input("Enter Morse code (use spaces between characters): ")
            print("Text:", morse_to_text(morse))
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()