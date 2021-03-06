from functools import reduce

# Flags para informar se o input é feito via terminal (ICPC) ou via arquivo (CodeForces)
TERMINAL_METHOD = "terminal"
FILE_METHOD = "file"


# -------------------------------------- #
# Classe que representa uma célula do autômato celular
class Cell:
    def __init__(self, position, value, neighbors):
        self.position = position
        self.value = value
        self.neighbors = neighbors


# -------------------------------------- #
# Classe que representa o autômato celular
class Automaton:
    def __init__(self, size, distance, limit, initialValues):
        self.start = 1
        self.size = size
        self.distance = distance
        self.limit = limit
        self.grid = []
        self.fillGrid(initialValues)

    # calcula a distancia entre duas posições de celulas [min(|i−j|, n−|i−j|)]
    def getCellsDistance(self, posOne, posTwo):
        return min(
            abs(posOne - posTwo), 
            self.size - abs(posOne - posTwo)
            )

    # busca todas as células com distancia >= d para a celula de referencia 
    def getNeighbors(self, position):
        neighbors = []
        for c in self.grid:
            d = self.getCellsDistance(position, c.position)
            if d <= self.distance and d != 0:
                neighbors.append(c.position)
        return neighbors

    #calcula o novo valor da celula com base na soma dos valores dos vizinhos módulo ordem da célula
    def calcValue(self, cell):
        sum = reduce(lambda s, n: s + self.grid[n - self.start].value, cell.neighbors, cell.value)
        value = sum % self.limit
        return value

    # preenche a lista circular de células com o valor inicial passado no imput
    def fillGrid(self, initialValues):
        self.grid = [Cell(position=i, value=initialValues[i - self.start], neighbors=[]) for i in range(self.start, self.size+self.start)]
        for c in self.grid:
            c.neighbors = self.getNeighbors(c.position)

    # executa os calculos de distância entre as células e atualiza a lista
    def nextStep(self):
        newGrid = [Cell(position=cell.position, value=self.calcValue(cell), neighbors=cell.neighbors) for cell in self.grid]
        self.grid = newGrid

    # converte os valores das celulas para string
    def __str__(self):
        gridParsed = [str(cell.value) for cell in self.grid]
        return " ".join(gridParsed)


# -------------------------------------- #
# classe que representa o motor que executa as etapas do autômato
class Engine:
    def __init__(self, executions, automaton):
        self.executions = executions
        self.automaton = automaton

    def run(self):
        [self.automaton.nextStep() for i in range(self.executions)]


# -------------------------------------- #
# classe responsável por representar as entradas de testes do projeto
class TestCase:
    def __init__(self, n, m, d, k, i):
        self.n = n
        self.m = m
        self.d = d
        self.k = k
        self.i = i


# -------------------------------------- #
# classe responsável por ler o arquivo de entrada e escrever a saída
class I0Manager:
    def __init__(self, method):
        self.method = method
        self.testCases = []

        if method == FILE_METHOD:
            self.inFile = "cell.in"
            self.outFile = "cell.out"
            self.clearOutput()


    def getTestCases(self, l):
        # limpa as linhas desnecessarias
        lines = []
        for i in l:
            if i != "":
                lines.append(i)

        testCases = []
        #busca o conjunto de 2 linhas que forma o teste e monta o objeto TestCase com 
        # seus respectivos valores de n, m, k, d e i
        for i in range (0, len(lines), 2):
            args = lines[i].split(" ")
            values = lines[i+1].split(" ")
            args = [ int(i) for i in args ]
            values = [ int(i) for i in values ]
            testCases.append(TestCase(n=args[0], m=args[1], d=args[2], k=args[3], i=values))
        return testCases

    # limpa o arquivo de saída antes de imprimir o novo resultado
    def clearOutput(self):
        open(self.outFile, "w").close()      

    # faz a leitura dos dados de entrada
    def readInput(self):
        lines = []
        if self.method == TERMINAL_METHOD:
            while True:
                try:
                    lines.append(input())
                except:
                    break
                    
        elif self.method == FILE_METHOD:
            f = open(self.inFile, "r")
            inputData = f.read()
            lines = inputData.splitlines()
            f.close()

        return self.getTestCases(lines)

    # escrever o resultado da execução
    def writeOutput(self, output):
        output = "%s\n" % output
        if self.method == TERMINAL_METHOD:
            print(output, end='')
        elif self.method == FILE_METHOD:
            f = open(self.outFile, "a")
            f.write(output)
            f.close()
        

# -------------------------------------- #
def main():
    # instancia o objeto responsavel pela leitura dos arquivos
    # tipos de metodos possiveis: (TERMINAL_METHOD, FILE_METHOD)
    io = I0Manager(method=FILE_METHOD)
    # le a entrada de dados e retorna os casos de teste
    testCases = io.readInput() 
    for test in testCases:
        # monta o automato celular
        automaton = Automaton(size=test.n, limit=test.m, distance=test.d, initialValues=test.i)
        # k = k % (n + m)
        execs = test.k % (test.n + test.m)
        # inicia a engine
        engine = Engine(executions=execs, automaton=automaton)
        # executa os steps (k)
        engine.run()
        # escreve o retorno
        io.writeOutput(str(automaton))
    print()

main()
