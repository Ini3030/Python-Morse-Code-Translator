morse_dictionary = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                    "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                    "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                    "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
                    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", " ": " "}

phrase = input("Input the text you want to translate to morse code:\n")
translation = []

warning = False
for letter in phrase:
    if letter.lower() not in morse_dictionary:
        if warning is False:
            print("\nWARNING: The inputted text contains characters that cannot be translated. "
                  "The translation may have been affected.")
        warning = True
    else:
        translation.append(morse_dictionary[letter.lower()])
print(f'\nYour text has been translated:\n{"".join(translation)}')
