from tkinter import *
from tkinter import messagebox

def exibir_mensagem():
    nome = entrada.get()
    mensagem = f"Olá, {nome}! Bem-vindo ao Sistema de Cadastro."
    messagebox.showinfo("Mensagem de Boas-Vindas", mensagem)

window = Tk()
window.title("Janela com Título")

txt = Label(text='Sistema de cadastro')
txt.pack()


entrada = Entry(window)
entrada.pack()

botao_enviar = Button(window, text="Enviar", command=exibir_mensagem)
botao_enviar.pack()

window.mainloop()