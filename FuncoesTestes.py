import unittest

from Funcoes import inverter_palavras, remover_duplicados, maior_palindrome, formatar_frase, anagrama_palindrome

# Exercicio 1. Reverta a ordem das palavras nas frases, mantendo a ordem das palavras:
Input1 = "Hello, World! OpenAI is amazing."
Output1 = "amazing. is OpenAI World! Hello,"

# Exercicio 2. Remova todos os caracteres duplicados da string abaixo:
Input2 = "Hello, World!"
Output2 = "Helo, Wrd!"

# Exercicio 3. Encontre a substring palindroma mais longa na string abaixo:
Input3 = "babad"
Output3 = "bab"

# Exercicio 4. Coloque em maiúscula a primeira letra de cada frase na string:
Input4 = "hello. how are you? i'm fine, thank you."
Output4 = "Hello. How are you? I'm fine, thank you."

# Exercicio 5. Verifique se a string é um anagrama de um palindromo:
Input5 = "racecar"
Output5 = "true"


class MyTestCase(unittest.TestCase):
    def test_inverter_palavras(self):
        self.assertEqual(inverter_palavras(Input1), Output1)

    def test_remover_duplicados(self):
        self.assertEqual(remover_duplicados(Input2), Output2)

    def test_maior_palindrome(self):
        self.assertEqual(maior_palindrome(Input3), Output3)

    def test_formatar_frase(self):
        self.assertEqual(formatar_frase(Input4), Output4)

    def test_anagrama_palindrome(self):
        self.assertEqual(anagrama_palindrome(Input5), Output5)


if __name__ == '__main__':
    unittest.main()
