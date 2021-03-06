
# -------------------------------------- #
# Classe que representa uma célula do autômato celular
class Cell:
    def __init__(self, position, value):
        self.position = position
        self.value = value

    def __str__(self):
        return "position=" + str(self.position) + "value=" + str(self.value)

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
    
    # retorna todas as células com distancia >= d para a celula de referencia
    def getNeighbors(self, cell):
        neighbors = []
        for cellGrid in self.grid:
            d = self.getCellsDistance(cell, cellGrid)
            if d <= self.distance:
                neighbors.append(cellGrid)
        return neighbors

    # calcula o novo valor da celula com base na
    # soma dos valores dos vizinhos módulo ordem da célula
    def calcValue(self, neighbors):
        sumValue = 0
        for cell in neighbors:
            sumValue += cell.value
        return sumValue % self.limit

    # calcula a distancia entre duas células
    def getCellsDistance(self, cellOne, cellTwo):
        return min(
            abs(cellOne.position - cellTwo.position), 
            self.size - abs(cellOne.position - cellTwo.position)
            )

    # preenche a lista circular de células
    def fillGrid(self, initialValues):
        for i in range(self.start, self.size+self.start):
            cell = Cell(position=i, value=initialValues[i - self.start])
            self.grid.append(cell)

    # executa os calculos de distância entre as célular e atualiza a lista
    def nextStep(self):
        newGrid = []
        for cell in self.grid:
            neighbors = self.getNeighbors(cell)
            value=self.calcValue(neighbors)
            newGrid.append(Cell(position=cell.position, value=value))
        self.grid = newGrid

    def __str__(self):
        strAutomaton = ""
        for cell in self.grid:
            strAutomaton += str(cell.value) + " "
        return strAutomaton

# -------------------------------------- #
# classe que representa o motor que executa as etapas do autômato
class Engine:
    def __init__(self, executions, automaton):
        self.executions = executions
        self.automaton = automaton

    def run(self):
        for i in range(self.executions):
            self.automaton.nextStep()


# -------------------------------------- #
# classe responsável por ler o arquivo de entrada e escrever a saída
class Reader:
    def __init__(self, inFile, outFile):
        self.inFile = inFile
        self.outFile = outFile

    # método responsável por validar a entrada
    def validate(self, args, values):
        n = args[0]
        m = args[1]
        d = args[2]
        k = args[3]
        
        hasError = False
        if n < 1 or n > 500:
            print("n fora do intervalo estabelecido (1 ≤ n ≤ 500)")
            hasError = True

        if m < 1 or m > 1000000:
            print("m fora do intervalo estabelecido (1 ≤ m ≤ 1000000)")
            hasError = True

        if d >= n/2:
            print("d fora do intervalo estabelecido (d < n/2)")
            hasError = True

        if k < 1 or m > 10000000:
            print("k fora do intervalo estabelecido (1 ≤ k ≤ 10000000)")
            hasError = True

        validValues = all(v <= m for v in values)
        if not validValues:
            print("valores iniciais das células do autômato fora do intervalo estabelecido (1 ≤ m ≤ 1000000)")
            hasError = True

        if hasError:
            exit()
    
        return n, m, d, k, values


    # método responsável por fazer a leitura do arquivo de entrada
    def readInput(self):
        try:
            f = open(self.inFile, "r")
            cellIn = f.read()
            cellSplit = cellIn.splitlines()
            args = cellSplit[0].split(sep=" ")
            values = cellSplit[1].split(sep=" ")

            args = [ int(i) for i in args ]
            if len(args) != 4:
                raise Exception()

            values = [ int(i) for i in values ]
            return self.validate(args, values)
        except:
            print("Erro na leitura do arquivo " + self.inFile + ", revise o formato da entrada")
            exit()
        finally:
            f.close()

    # método responsável por escrever o resultado da execução no arquivo de saída
    def writeOutput(self, output):
        f = open(self.outFile, "w")
        f.write(output)
        f.close()


# -------------------------------------- #
def main():
    # instancia o objeto responsavel pela leitura dos arquivos
    reader = Reader(inFile="cell.in", outFile="cell.out")
    # le o arquivo cell.in
    n, m, d, k, i = reader.readInput() 
    # monta o automato celular
    automaton = Automaton(size=n, limit=m, distance=d, initialValues=i)
    # inicia a engine
    engine = Engine(executions=k, automaton=automaton)
    # executa os steps
    engine.run()
    # escreve o retorno em cell.out
    reader.writeOutput(str(automaton))

main()
        


