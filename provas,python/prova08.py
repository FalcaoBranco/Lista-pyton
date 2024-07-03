from tkinter import *
from tkinter import messagebox
def exibir_mensagem():
    nome = entrada.get()
    mensagem = f"Olá, {nome}! Bem-vindo ao Sistema de Cadastro."
    messagebox.showinfo("Mensagem de Boas-Vindas", mensagem)

# Criação da janela principal
janela = Tk()
janela.title("Sistema de Cadastro")

# Campo de entrada de texto
entrada = Entry(janela)
entrada.pack()

# Botão para enviar
botao_enviar = Button(janela, text="Enviar", command=exibir_mensagem)
botao_enviar.pack()

# Loop principal da interface gráfica
janela.mainloop()
