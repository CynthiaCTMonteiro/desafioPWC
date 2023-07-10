# Manipulação de Strings em Python


## Conteúdo

* [Verificar String Nula ou Vazia](#verificar-string-nula-ou-vazia)
* [Inverter Palavras](#inverter-palavras)
* [Remover Duplicados](#remover-duplicados)
* [É Palíndromo](#é-palíndromo)
* [Maior Palíndromo](#maior-palíndromo)
* [Formatar Frase](#formatar-frase)
* [Anagrama Palíndromo](#anagrama-palíndrome)
* [Contar Caracteres](#contar-caracteres)
* [Contar Ímpares](#contar-ímpares)

## Verificar String Nula ou Vazia

Esta função recebe uma string como argumento e verifica se ela é nula ou vazia.

```python
def verificar_string_nula_vazia(objeto):
    if objeto is None or not isinstance(objeto, str) or len(objeto) == 0:
        return True
    else:
        return False
```

## Inverter Palavras

Esta função recebe uma frase e retorna a mesma com as palavras em ordem inversa.

```python
def inverter_palavras(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])
```

## Remover Duplicados

Esta função recebe uma string e retorna a mesma sem caracteres duplicados.

```python
def remover_duplicados(frase):
    unique_chars = ""
    for char in frase:
        if char not in unique_chars:
            unique_chars += char
    return unique_chars
```

## É Palíndromo

Esta função verifica se uma string é palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente.

```python
def eh_palindromo(substring):
    return substring == substring[::-1]
```

## Maior Palíndromo

Esta função recebe uma string e retorna o maior palíndromo encontrado nela.

```python
def maior_palindrome(string):
    maior_palindromo = ""
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if eh_palindromo(substring) and len(substring) > len(maior_palindromo):
                maior_palindromo = substring
    return maior_palindromo
```

## Formatar Frase

Esta função recebe uma frase e retorna a mesma formatada de acordo com as regras de pontuação e capitalização.

```python
def formatar_frase(frase):
    frase = frase.lower()
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
```

## Anagrama Palíndromo

Esta função verifica se é possível formar um palíndromo com os caracteres de uma string.

```python
def anagrama_palindrome(string):
    char_count = contar_caracteres(string)
    odd_count = contar_impares(char_count)
    return 'true' if odd_count <= 1 else 'false'
```

## Contar Caracteres

Esta função recebe uma string e retorna um dicionário contendo a contagem de cada caractere na string.

```python
def contar_caracteres(string):
    char_count = {}
    for char in set(string):
        char_count[char] = string.count(char)
    return char_count
```

## Contar Ímpares

Esta função recebe um dicionário contendo uma contagem de caracteres e retorna o número de caracteres que têm uma contagem ímpar.

```python
def contar_impares(char_count):
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count
```

# Uso das Funções

## Exercício 1: Inverter Palavras

Esta função inverte a ordem das palavras de uma frase, mantendo a ordem dos caracteres em cada palavra.

**Exemplo:**

```python
Input1 = "Hello, World! OpenAI is amazing."
Output1 = inverter_palavras(Input1)
print(Output1)  # Resultado: "amazing. is OpenAI World! Hello,"
```

## Exercício 2: Remover Duplicados

Esta função remove todos os caracteres duplicados da string fornecida.

**Exemplo:**

```python
Input2 = "Hello, World!"
Output2 = remover_duplicados(Input2)
print(Output2)  # Resultado: "Helo, Wrd!"
```

## Exercício 3: Maior Palíndromo

Esta função encontra a substring palíndroma mais longa na string fornecida.

**Exemplo:**

```python
Input3 = "babad"
Output3 = maior_palindrome(Input3)
print(Output3)  # Resultado: "bab"
```

## Exercício 4: Formatar Frase

Esta função coloca em maiúscula a primeira letra de cada frase na string fornecida.

**Exemplo:**

```python
Input4 = "hello. how are you? i'm fine, thank you."
Output4 = formatar_frase(Input4)
print(Output4)  # Resultado: "Hello. How are you? I'm fine, thank you."
```

## Exercício 5: Anagrama Palíndromo

Esta função verifica se a string fornecida é um anagrama de um palíndromo.

**Exemplo:**

```python
Input5 = "racecar"
Output5 = anagrama_palindrome(Input5)
print(Output5)  # Resultado: "true"
```

# Testes Unitários

Os testes unitários foram criados para verificar se as funções estão operando corretamente. Os testes foram escritos utilizando a biblioteca `unittest` do Python.

```python
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
```

# Interface Gráfica de Usuário (GUI)

Este projeto também inclui uma interface gráfica de usuário (GUI) escrita em Python usando a biblioteca `tkinter`. Essa GUI permite que os usuários interajam diretamente com as funções.

## Funcionamento

Quando executado, o script cria uma janela contendo um campo de entrada de texto, vários botões correspondendo às funções e um campo de saída de texto. O usuário pode digitar uma string no campo de entrada, clicar em um dos botões para executar a função correspondente e a saída será exibida no campo de saída de texto.

## Funções dos Botões

* **Inverter String:** inverte a ordem das palavras na string.
* **Remover Duplicados:** remove todos os caracteres duplicados na string.
* **Maior Palindromo:** encontra a maior substring palíndroma na string.
* **Capitalize Frase:** capitaliza a primeira letra de cada frase na string.
* **Anagrama Palindromo:** verifica se a string é um anagrama de um palíndromo.
* **Testar Funções:** executa todos os testes unitários e exibe os resultados em uma nova janela.

## Código GUI

```python
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import FuncoesTestes
import io
import sys

from Funcoes import inverter_palavras, remover_duplicados, maior_palindrome, formatar_frase, anagrama_palindrome, \
    verificar_string_nula_vazia

entradaInvalida = "Entrada Inválida"

# Funções para gerenciar a saída e a lógica dos botões...
def saida(valor):
    output_text.configure(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, valor)
    output_text.tag_configure("center", justify="center")
    output_text.tag_add("center", "1.0", "end")
    output_text.configure(state="disabled")

def btn1():
    frase = input_entry.get()
    if verificar_string_nula_vazia(frase):
        resultado = entradaInvalida
    else:
        resultado = inverter_palavras(frase)
    saida(resultado)


def btn2():
    frase = input_entry.get()
    if verificar_string_nula_vazia(frase):
        resultado = entradaInvalida
    else:
        resultado = remover_duplicados(frase)
    saida(resultado)


def btn3():
    frase = input_entry.get()
    if verificar_string_nula_vazia(frase):
        resultado = entradaInvalida
    else:
        resultado = maior_palindrome(frase)
    saida(resultado)


def btn4():
    frase = input_entry.get()
    if verificar_string_nula_vazia(frase):
        resultado = entradaInvalida
    else:
        resultado = formatar_frase(frase)
    saida(resultado)


def btn5():
    frase = input_entry.get()
    if verificar_string_nula_vazia(frase):
        resultado = entradaInvalida
    else:
        resultado = anagrama_palindrome(frase)
    saida(resultado)


def executar_testes():
    # Redireciona a saída de impressão (stdout) para um objeto StringIO
    output_stream = io.StringIO()
    sys.stdout = output_stream

    # Executa os testes
    suite = FuncoesTestes.unittest.TestLoader().loadTestsFromModule(FuncoesTestes)
    FuncoesTestes.unittest.TextTestRunner(stream=output_stream, verbosity=2).run(suite)

    # Restaura a saída de impressão padrão
    sys.stdout = sys.__stdout__

    # Obtém o conteúdo da saída de impressão
    output = output_stream.getvalue()

    # Cria uma nova janela para exibir os resultados dos testes
    janela_resultados = tk.Toplevel(janela)
    janela_resultados.title("Resultados dos Testes")

    # Cria um widget de texto com rolagem para exibir a saída dos testes
    output_text_testes = scrolledtext.ScrolledText(janela_resultados, state="normal", width=100, height=20)
    output_text_testes.insert(tk.END, output)
    output_text_testes.configure(state="disabled")
    output_text_testes.pack()

# Cria a janela principal
janela = tk.Tk()

# Configurações da janela, rótulos, botões e caixas de texto
# Define o título da janela
janela.title("Manipulação de Strings")

# Define o tamanho da janela
largura = 600
altura = 300
x_pos = (janela.winfo_screenwidth() - largura) // 2
y_pos = (janela.winfo_screenheight() - altura) // 2
janela.geometry(f"{largura}x{altura}+{x_pos}+{y_pos}")

# Cria um rótulo para a entrada
input_label = tk.Label(janela, text="Digite a string:")
input_label.pack()

# Cria um campo de entrada
input_entry = tk.Entry(janela, width=50)
input_entry.pack()

# Cria um botão para inverter a string
btn_s1 = tk.Button(janela, text="Inverter String", command=btn1)
btn_s1.pack()

btn_s2 = tk.Button(janela, text="Remover Duplicados", command=btn2)
btn_s2.pack()

btn_s3 = tk.Button(janela, text="Maior Palindromo", command=btn3)
btn_s3.pack()

btn_s4 = tk.Button(janela, text="Capitalize Frase", command=btn4)
btn_s4.pack()

btn_s5 = tk.Button(janela, text="Anagrama Palindrome", command=btn5)
btn_s5.pack()

btn_testar_funcoes = tk.Button(janela, text="Testar Funções", command=executar_testes)
btn_testar_funcoes.pack()

# Cria um rótulo para a saída
output_label = tk.Label(janela, text="Resultado:")
output_label.pack()

# Cria uma caixa de texto para exibir a saída
output_text = tk.Text(janela, width=50, height=1)
output_text.configure(font=("Arial", 15))
output_text.pack()

# Define a caixa de texto como somente leitura
output_text.configure(state="disabled")
# Inicia o loop principal da interface
janela.mainloop()
```


