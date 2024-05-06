def morse_to_text(morse_code): 
    text = "" 
    morse_code += " " 
    char = "" 
    for symbol in morse_code:
        if symbol != " ":
            char += symbol
        else:
            if char in morse_dict.values():
                text +=
                list(morse_dict.keys())
                [list(morse_dict.values()).index(char)]
                char = ""
    return text
codigo_morse = input("ingrese el codigo morse a convertir a texto: ")
texto = morse_to_text(codigo_morse)
print("texto:", texto)



