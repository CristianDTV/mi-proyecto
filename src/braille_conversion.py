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
    """ Convierte texto alfabético a braille basado en el mapeo_braille. """
    braille = ''
    for caracter in texto:
        char_lower = caracter.lower()
        if caracter.isupper() and char_lower in mapeo_braille:
            braille += '⠨'  # Prefijo para mayúsculas en braille
        if char_lower in mapeo_braille:
            braille += mapeo_braille[char_lower]
        else:
            braille += ' '  # Añadir espacio para caracteres no mapeados
    return braille

# Puedes añadir más funciones relacionadas con braille si es necesario.
