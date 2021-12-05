"""Program pro překlad do morseovy abecedy a zpět."""

# Slovníky pro překlad
DIR_DoMorseovky = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                   'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..',
                   '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                   '.': '.-.-.-', ', ': '--..--', '-': '-....-'}

DIR_ZMorseovky = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                  '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                  '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                  '--': 'M', '-.': 'N', '---': 'N', '.--.': 'P',
                  '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                  '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                  '-.--': 'Y', '--..': 'Z',
                  '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                  '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
                  '.-.-.-': '.', '--..--': ', ', '-....-': '-'}


# Překlad do morseovky
def to_morse(retezec):

    """Funkce to_morse vrací vstupní řetězec převedený do morseovky.
        Argumenty:
            - retezec - Vstup funkce
        Vrací:
            - string - Výstup funkce
        """

    morse = []
    # přeložené znaky se ukládají do pole morse

    for i in retezec:
        if i in DIR_DoMorseovky:
            morse.append(DIR_DoMorseovky[i])

            # vložený znak je nalezen ve slovníku a vložen na konec pole morse

    return " ".join(morse)
    # přidání mezery na konec přeloženého znaku


def from_morse(retezec):

    """Funkce from_morse vrací vstupní řetězec převedený z morseovky.
            Argumenty:
                - retezec - Vstup funkce
            Vrací:
                - string - Výstup funkce
            """

    morse = retezec.split()
    # vstup se rozdělí na jednotlivé znaky které následně hledá ve slovníku
    preklad = []
    # přeložené znaky se ukládají do pole preklad

    for i in morse:
        if i in DIR_ZMorseovky:
            preklad.append(DIR_ZMorseovky[i])

            # vložený znak je nalezen ve slovníku a vložen na konec pole morse

    return "".join(preklad)


# Hlavní funkce
def main():
    operace = int(input("Vyberte si překlad:\n"
                        "1 - Do morseovky\n"
                        "2 - Z morseovky\n"))

    # Dle vybrané operace se následně provede překlad

    if operace == 1:
        vstup = input("Zadejte text k překladu do morseovky: ")
        preklad = to_morse(vstup.upper())
        print(preklad)

    elif operace == 2:
        vstup = input("Zadejte text k překladu z morseovky: ")
        preklad = from_morse(vstup)
        print(preklad)

    elif operace != 1 & operace != 2:
        print("Špatně zadaná operace")

    # V případě špatného výběru operace program končí


if __name__ == "__main__":
    main()
