import tkinter as tk

def calcular():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        operacao = operacoes.get()
        
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        else:
            resultado = "Operação Inválida"
        
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.config(text="Entradas Inválidas")

janela = tk.Tk()
janela.title("Calculadora Simples")

entrada1 = tk.Entry(janela)
entrada1.grid(row=0, column=0, padx=10, pady=10)

entrada2 = tk.Entry(janela)
entrada2.grid(row=0, column=1, padx=10, pady=10)

operacoes = tk.StringVar()
operacoes.set("+")  

menu_operacoes = tk.OptionMenu(janela, operacoes, "+", "-", "*", "/")
menu_operacoes.grid(row=0, column=2, padx=10, pady=10)

calcular_button = tk.Button(janela, text="Calcular", command=calcular)
calcular_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

resultado_label = tk.Label(janela, text="Resultado: ")
resultado_label.grid(row=2, column=0, columnspan=3)

janela.mainloop()
