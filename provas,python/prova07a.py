lista = []
nomes = []
def notas():
    while True:
        nome = input('Qual o nome do aluno: ')
        nomes.append(nome)
        n1 = float(input('Digite a nota da primeira unidade: '))
        lista.append(n1)
        n2 = float(input('Digite a nota da segunda unidade: '))
        lista.append(n2)
        n3 = float(input('Digite a nota da terceira unidade: '))
        lista.append(n3)
        media()
        outro_aluno = input('Quer calcular a media de outro aluno S/N: ').upper()
        if outro_aluno == 'N':
            break
        

def media():
    media = sum(lista)/len(lista)
    media_formatada = "{:.2f}".format(media)
    print(f'Media:{media_formatada}')
    
notas()