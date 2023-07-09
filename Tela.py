import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import FuncoesTestes
import io
import sys

from Funcoes import inverter_palavras, remover_duplicados, maior_palindrome, formatar_frase, anagrama_palindrome, \
    verificar_string_nula_vazia

entradaInvalida = "Entrada Inválida"


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
