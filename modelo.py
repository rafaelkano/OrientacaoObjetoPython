class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self._likes} Likes' )

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.duracao}min - {self.likes} Likes')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.temporadas} Temporadas - {self._likes} Likes')

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

atlanta.dar_like()
atlanta.dar_like()

#print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}')
#print(f'Nome: {atlanta.nome} - {atlanta.ano}: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    programa.imprime( )
