class Livro:
    def __init__(self, titulo, autor, editora):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora

    def exibir_detalhes(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nEditora: {self.editora}"

class Romance(Livro):
    def __init__(self, titulo, autor, editora, genero):
        super().__init__(titulo, autor, editora)
        self.genero = genero

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nGênero: {self.genero}"

class Biografia(Livro):
    def __init__(self, titulo, autor, editora, pessoa_biografada):
        super().__init__(titulo, autor, editora)
        self.pessoa_biografada = pessoa_biografada

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nPessoa Biografada: {self.pessoa_biografada}"

# Exemplos de uso
livro1 = Romance("Amor Eterno", "Maria Silva", "Editora A", "Romance Histórico")
livro2 = Biografia("Steve Jobs: A Biografia", "Walter Isaacson", "Editora B", "Steve Jobs")

print("Detalhes do Romance:")
print(livro1.exibir_detalhes())
print()
print("Detalhes da Biografia:")
print(livro2.exibir_detalhes())
