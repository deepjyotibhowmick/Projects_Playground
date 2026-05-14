# All vowels will be translate into x
# demo translator

def translate(phrase):
    translated_value = ""

    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.islower():
                translated_value = translated_value + "x"
            else:
                translated_value = translated_value + "X"

        else:
            translated_value = translated_value + letter
    return translated_value

phrs = input("Enter a Phrase: ")

print("Translated value: ",translate(phrs))