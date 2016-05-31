def silabas(word, sep='-'):
    """Devuelve la palabra introducida separada en sílabas
    separadas por el caracter 'sep', por defecto '-'.
    No introducir signos de puntuación."""
    word = word.lower()
    l = ['r','l']
    o = ['p','b','f','t','d','c','k','g']
    c = ['b','c','ch','d','f','g','h','j','k','l','ll','m','n','ñ','p','q','r','rr','s','t','v','x','y','z']
    a = ['a','e','o','á','é','ó','í','ú']
    i = ['i','u','ü']
    letras = []
    estructura = ''
    j = 0
    while j < len(word):
        if j == 0:
            if word[j] == 'p' and word[j+1] == 's':
                letras.append('ps')
                estructura += 'C'
                j += 2
                continue
            elif word[j] == 'p' and word[j+1] == 'n':
                letras.append('pn')
                estructura += 'C'
                j += 2
                continue
            elif word[j] == 'p' and word[j+1] == 't':
                letras.append('pt')
                estructura += 'C'
                j += 2
                continue
            elif word[j] == 'g' and word[j+1] == 'n':
                letras.append('gn')
                estructura += 'C'
                j += 2
                continue
        if j < len(word) - 1:
            if word[j] == 'c' and word[j+1] == 'h':
                letras.append('ch')
                estructura += 'C'
                j += 2
                continue
            elif word[j] == 'l' and word[j+1] == 'l':
                letras.append('ll')
                estructura += 'C'
                j += 2
                continue
            elif word[j] == 'r' and word[j+1] == 'r':
                letras.append('rr')
                estructura += 'C'
                j += 2
                continue
            elif word[j] == 'c' and (word[j+1] == 'e' or word[j+1] == 'i'):
                letras.append('c')
                estructura += 'C'
                j += 1
                continue
            elif word[j] == 'g' and (word[j+1] == 'e' or word[j+1] == 'i'):
                letras.append('g')
                estructura += 'C'
                j += 1
                continue
        if word[j] in a:
            letras.append(word[j])
            estructura += 'A'
            j += 1
            continue
        elif word[j] in i:
            letras.append(word[j])
            estructura += 'I'
            j += 1
            continue
        elif word[j] in l:
            letras.append(word[j])
            estructura += 'L'
            j += 1
            continue
        elif word[j] in o:
            letras.append(word[j])
            estructura += 'O'
            j += 1
            continue
        elif word[j] in c:
            letras.append(word[j])
            estructura += 'C'
            j += 1
            continue
        else:
            raise TypeError("No se reconoce el carácter '{0}' como una letra del castellano.".format(word[j]))
    estructura += 'C'
    letras.append('')
    salida = []
    j = 0
    silaba = ''
    while j < len(letras):
        if letras[j] == '':
            break
        silaba += letras[j]
        if estructura[j] == 'A':
            if estructura[j+1] == 'A':
                salida.append(silaba)
                silaba = ''
                j+=1
                continue
            elif estructura[j+1] == 'I':
                j+=1
                continue
            elif estructura[j+1] == 'O':
                if estructura[j+2] in 'AIL':
                    if letras[j+1] == 'd' and letras[j+2] == 'l':
                        salida.append(silaba + letras[j+1])
                        silaba = ''
                        j += 2
                        continue
                    salida.append(silaba)
                    silaba = ''
                    j+=1
                    continue
                else:
                    if letras[j+2] == 's' and estructura[j+3] in 'LCO':
                        salida.append(silaba + letras[j+1] + letras[j+2])
                        silaba = ''
                        j += 3
                        continue
                    salida.append(silaba + letras[j+1])
                    silaba = ''
                    j += 2
                    continue
            else:
                if j+2 < len(letras):
                    if estructura[j+2] in 'AI':
                        salida.append(silaba)
                        silaba = ''
                        j+=1
                        continue
                    else:
                        if letras[j+2] == 's' and estructura[j+3] in 'LCO':
                            salida.append(silaba + letras[j+1] + letras[j+2])
                            silaba = ''
                            j += 3
                            continue
                        salida.append(silaba + letras[j+1])
                        silaba = ''
                        j += 2
                        continue
                else:
                    salida.append(silaba + letras[j+1])
                    silaba = ''
                    j += 2
                    continue
        elif estructura[j] == 'I':
            if estructura[j+1] in 'AI':
                j+=1
                continue
            elif estructura[j+1] == 'O':
                if estructura[j+2] in 'AIL':
                    if letras[j+1] == 'd' and letras[j+2] == 'l':
                        salida.append(silaba + letras[j+1])
                        silaba = ''
                        j += 2
                        continue
                    salida.append(silaba)
                    silaba = ''
                    j+=1
                    continue
                else:
                    if letras[j+2] == 's' and estructura[j+3] in 'LCO':
                        salida.append(silaba + letras[j+1] + letras[j+2])
                        silaba = ''
                        j += 3
                        continue
                    salida.append(silaba + letras[j+1])
                    silaba = ''
                    j += 2
                    continue
            else:
                if j+2 < len(letras):
                    if estructura[j+2] in 'AI':
                        salida.append(silaba)
                        silaba = ''
                        j+=1
                        continue
                    else:
                        if letras[j+2] == 's' and estructura[j+3] in 'LCO':
                            salida.append(silaba + letras[j+1] + letras[j+2])
                            silaba = ''
                            j += 3
                            continue
                        salida.append(silaba + letras[j+1])
                        silaba = ''
                        j += 2
                        continue
                else:
                    salida.append(silaba + letras[j+1])
                    silaba = ''
                    j += 2
                    continue
        elif estructura[j] == 'O':
            if estructura[j+1] in 'AIL':
                j+=1
                continue
            else:
                if letras[j+1] == '':
                    salida.append(silaba)
                    break
                raise TypeError("Estructura de sílaba incorrecta en la palabra {0}".format(word))
        else:
            if estructura[j+1] in 'AI':
                j+=1
                continue
            else:
                if letras[j+1] == '':
                    salida.append(silaba)
                    break
                elif letras[j+1] == 's':
                    salida.append(silaba)
                    silaba = ''
                    j+=1
                    continue
                raise TypeError("Estructura de sílaba incorrecta en la palabra {0}".format(word))
    return sep.join(salida)
