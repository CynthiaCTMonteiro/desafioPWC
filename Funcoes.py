def verificar_string_nula_vazia(objeto):
    if objeto is None or not isinstance(objeto, str) or len(objeto) == 0:
        return True
    else:
        return False


def inverter_palavras(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])



def remover_duplicados(frase):
    unique_chars = ""
    for char in frase:
        if char not in unique_chars:
            unique_chars += char
    return unique_chars

def eh_palindromo(substring):
    return substring == substring[::-1]


def maior_palindrome(string):
    maior_palindromo = ""
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if eh_palindromo(substring) and len(substring) > len(maior_palindromo):
                maior_palindromo = substring
    return maior_palindromo