def morse(phrase):
    morse_code = {'A': '._',
    'B': '_...',
    'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.', 'G': '__.', 'H': '....', 'I': '.___','J': '.___','K': '_._','L': '._..', 'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.', 'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._', 'Y': '_.__', 'Z': '__..' }
    cipher = ''
    for x in phrase:
        if x != '':
            cipher+= morse_code[x]+ ' '
        else:
            cipher+= ' '
    return cipher
