def verificar_string_nula_vazia(objeto):
    if objeto is None or not isinstance(objeto, str) or len(objeto) == 0:
        return True
    else:
        return False


def inverter_palavras(sentence):
    words = sentence.split()
    reversed_words = ' '.join(words[::-1])
    return reversed_words


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


def formatar_frase(frase):
    pontuacoes_conhecidas = ['.', '!', '?', ':']

    def capitalizar_palavra(palavra):
        return palavra.capitalize()

    def verificar_capitalizacao_anterior(index, palavra):
        if index == 0 or palavra[index - 1][-1] in pontuacoes_conhecidas:
            return True
        return False

    palavras = frase.split()
    nova_frase = [capitalizar_palavra(palavra) if verificar_capitalizacao_anterior(i, palavras) else palavra for
                  i, palavra in enumerate(palavras)]
    return ' '.join(nova_frase)


def anagrama_palindrome(string):
    char_count = contar_caracteres(string)
    odd_count = contar_impares(char_count)
    return 'true' if odd_count <= 1 else 'false'


def contar_caracteres(string):
    char_count = {}
    for char in set(string):
        char_count[char] = string.count(char)
    return char_count


def contar_impares(char_count):
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count
