x = input('Choose the Algorithm: 1 -- FIFO; 2 -- SJF ')
class Processos:
    def __init__(self, nome, tempo, prioridade):
        self.nome = nome
        self.tempo = tempo
        self.prioridade = prioridade

    def get_tempo(self):
            return self.tempo
vet = []


i = 1
match x:
    case '1':
        n = int(input('Quantos processos serão? '))

        while(i <= n):
            processo = Processos('Processo ' + str(i),
                                 input('Quanto tempo terá o Processo {} em milisegundos? '.format(i)), i)
            vet.append(processo)

            i = i + 1

        i = 1
        while(i <= n):
            print(vet[i - 1].__dict__)
            i = i + 1

        pass
    case '2':
        n = int(input('Quantos processos serão? '))

        while (i <= n):
            processo = Processos('Processo ' + str(i),
                                 input('Quanto tempo terá o Processo {} em milisegundos? '.format(i)), i)
            vet.append(processo)

            i = i + 1

        i = 1
        j = 1


        vet = sorted(vet, key=lambda processo: processo.get_tempo())

        i = 1
        while (i <= n):
            print(vet[i - 1].__dict__)
            i = i + 1

pass
