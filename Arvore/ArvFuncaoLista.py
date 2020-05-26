
class No():
    def __init__(self, valor):
        self.valor = valor
        self.direita = None
        self.esquerda = None

    def __str__(self):
        return f'NO: {self.valor}'

class ArvLista():
    def __init__(self):
        self.raiz = None
        self.quantidadeFolhas = 0

    def __addNo(self, no, perc):
        if no.valor > perc.valor:
            if perc.direita == None:
                perc.direita = no
            else:
                self.__addNo(no, perc.direita)
        elif no.valor < perc.valor:
            if perc.esquerda == None:
                perc.esquerda = no
            else:
                self.__addNo(no, perc.esquerda)

        else:
            raise ("numero já existe")

    def add(self, valor):
        no = No(valor)
        if self.raiz == None:
            self.raiz = no
        else:
            self.__addNo(no, self.raiz)
        self.quantidadeFolhas += 1

    # Dividir ou não a função em, buscarNo e BuscarPaiNo

    def __buscarNo(self, valor, percorredor):
        perc = percorredor
        if perc == None:
            return None
        if perc.valor == valor:
            return perc
        else:
            if valor > perc.valor:
                return self.__buscarNo(valor, perc.direita)
            else:
                return self.__buscarNo(valor, perc.esquerda)

    def buscar(self, valor):
        if self.quantidadeFolhas == 0:
            return "Valor não existe na árvore"
        busca = self.__buscarNo(valor, self.raiz)
        if busca == None:
            return "Valor não existe árvore"
        return "Valor encontrado"

    def __imprimir(self, perc):
        if perc != None:
            print(perc)
            self.__imprimir(perc.esquerda)
            self.__imprimir(perc.direita)

    def imprimir(self):
        self.__imprimir(self.raiz)

ArvLista= ArvLista()
