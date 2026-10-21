MORSE_CODE_DICT = {
  "A": "._",
  "B": "-...",
  "C": "-.-.",
  "D": "-..",
  "E": ".",
  "F": "..-.",
  "G": "--.",
  "H": "....",
  "I": "..",
  "J": ".---",
  "K": "-.-",
  "L": ".-..",
  "M": "--",
  "N": "-.",
  "O": "---",
  "P": ".--.",
  "Q": "--.-",
  "R": ".-.",
  "S": "...",
  "T": "-",
  "U": "..-",
  "V": "...-",
  "W": ".--",
  "X": "-..-",
  "Y": "-.--",
  "Z": "--..",
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  " ": "/"
}
def Start_Menu():
    """Gets option for the main menu"""
    while True:
        print("A. Encode text to morse code")
        print("B. Decode Morse code to text")
        print("C. QUIT")
        Action = input("Action: ").upper()
        if Action == "A":
            return Action
        elif Action == "B":
            return Action
        elif Action == "C":
            return Action
        else:
            print("Invalid Option")
def encode_into_morse_code():
    Word_Encoding = input("Input: ").upper()
    Encoding_Letters = list(Word_Encoding)
    for letters in Encoding_Letters:
        if letters in MORSE_CODE_DICT:
            Morse_Code_list.append(MORSE_CODE_DICT[letters])
        else:
            print(f"[Skipping {letters}]")
    
    Morse_Code = "  ".join(Morse_Code_list)
    print(Morse_Code)

def decode_more_code():
    REVERSED_MORSE = {value: key for key, value in MORSE_CODE_DICT.items()}
    Morse_Code = input("Enter your Morse Code (Use Double Spaces and / for Spaces: ")
    Letters = Morse_Code.split("  ")
    for letters in Letters:
        if letters in REVERSED_MORSE:
            word_list.append(REVERSED_MORSE[letters])
        else:
            print(f"[Skipping {letters}]")
    text = "".join(word_list)
    print(text)  




#Variables/ List
Morse_Code_list = []
word_list = []

def main():
    Action = Start_Menu()
    while True:
        if Action == "A":
            encode_into_morse_code()
            break
        elif Action == "B":
            decode_more_code()
            break
        elif Action == "C":
            print("Goodbye")
            break
        else:
            print("Invalid Entry")

if __name__ == "__main__":
    main()