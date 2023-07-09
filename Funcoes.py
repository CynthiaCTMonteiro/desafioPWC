def verificar_string_nula_vazia(objeto):
    if objeto is None or not isinstance(objeto, str) or len(objeto) == 0:
        return True
    else:
        return False


def inverter_palavras(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])



