# braille_conversion.py

# Diccionario de mapeo de caracteres a braille
mapeo_braille = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵', 'á': '⠷', 'é': '⠮', 'í': '⠌', 'ó': '⠬',
    'ú': '⠾', 'ü': '⠿', 'ñ': '⠪',
    '0': '⠚', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙',
    '5': '⠑', '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊',
    '¿': '⠢', '?': '⠢', '¡': '⠖', '!': '⠖',
    ',': '⠂', '.': '⠄', ';': '⠆', ':': '⠒', '-': '⠤',
    '"': '⠶', "'": '⠄', '(': '⠐⠣', ')': '⠐⠜'
}

def texto_a_braille(texto):
    braille = ''
    for caracter in texto:
        char_lower = caracter.lower()
        if caracter.isdigit():
            braille += '⠼' + mapeo_braille[char_lower]
        else:
            numero_encontrado = False
            if caracter.isupper() and char_lower in mapeo_braille:
                braille += '⠨'
            if char_lower in mapeo_braille:
                braille += mapeo_braille[char_lower]
            else:
                braille += ' '
    return braille