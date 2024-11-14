import tkinter as tk
from tkinter import scrolledtext
from analisador_lexico.analisador import analisador_lexico

def exibir_resultado(tokens, contagem_tokens, resultado_tokens, resultado_contagem):
    resultado_tokens.delete(1.0, tk.END)
    for token in tokens:
        resultado_tokens.insert(tk.END, f"{token}\n")

    resultado_contagem.delete(1.0, tk.END)
    for tipo, quantidade in contagem_tokens.items():
        resultado_contagem.insert(tk.END, f"{tipo}: {quantidade}\n")

def analisar_codigo(campo_codigo, resultado_tokens, resultado_contagem):
    codigo = campo_codigo.get("1.0", tk.END)
    tokens, contagem_tokens = analisador_lexico(codigo)
    exibir_resultado(tokens, contagem_tokens, resultado_tokens, resultado_contagem)

def iniciar_interface():
    janela = tk.Tk()
    janela.title("Analisador Léxico")

    label_codigo = tk.Label(janela, text="Digite o código ou expressão:")
    label_codigo.pack(padx=10, pady=5)

    campo_codigo = scrolledtext.ScrolledText(janela, width=50, height=10)
    campo_codigo.pack(padx=10, pady=5)

    label_resultado_tokens = tk.Label(janela, text="Tokens Encontrados:")
    label_resultado_tokens.pack(padx=10, pady=5)

    resultado_tokens = scrolledtext.ScrolledText(janela, width=50, height=10)
    resultado_tokens.pack(padx=10, pady=5)

    label_resultado_contagem = tk.Label(janela, text="Contagem de Tokens:")
    label_resultado_contagem.pack(padx=10, pady=5)

    resultado_contagem = scrolledtext.ScrolledText(janela, width=50, height=5)
    resultado_contagem.pack(padx=10, pady=5)

    botao_analisar = tk.Button(janela, text="Analisar", command=lambda: analisar_codigo(campo_codigo, resultado_tokens, resultado_contagem))
    botao_analisar.pack(pady=10)

    janela.mainloop()
