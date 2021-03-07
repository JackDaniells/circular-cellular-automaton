INPUT_TERMINAL_METHOD = "terminal"
INPUT_FILE_METHOD = "file"

class Cell:
    def __init__(self, position, value):
        self.position = position
        self.value = value

class Automaton:
    def __init__(self, size, distance, limit, initialValues):
        self.start = 1
        self.size = size
        self.distance = distance
        self.limit = limit
        self.grid = []
        self.fillGrid(initialValues)
    
    def calcValue(self, cell):
        sumValue = 0
        for cellGrid in self.grid:
            d = self.getCellsDistance(cell, cellGrid)
            if d <= self.distance:
                sumValue += cellGrid.value
        return sumValue % self.limit

    def getCellsDistance(self, cellOne, cellTwo):
        return min(
            abs(cellOne.position - cellTwo.position), 
            self.size - abs(cellOne.position - cellTwo.position)
            )

    def fillGrid(self, initialValues):
        self.grid = [Cell(position=i, value=initialValues[i - self.start]) for i in range(self.start, self.size+self.start)]

    def nextStep(self):
        newGrid = [Cell(position=cell.position, value=self.calcValue(cell)) for cell in self.grid]
        self.grid = newGrid

    def __str__(self):
        gridParsed = [str(cell.value) for cell in self.grid]
        return " ".join(gridParsed)

class Engine:
    def __init__(self, executions, automaton):
        self.executions = executions
        self.automaton = automaton

    def run(self):
        [self.automaton.nextStep() for i in range(self.executions)]

class TestCase:
    def __init__(self, n, m, d, k, i):
        self.n = n
        self.m = m
        self.d = d
        self.k = k
        self.i = i

class Reader:
    def __init__(self, method):
        self.method = method
        self.testCases = []

        if method == INPUT_FILE_METHOD:
            self.inFile = "cell.in"
            self.outFile = "cell.out"
            self.clearOutput()


    def fillTestCases(self, a):
        cellSplit = []
        for i in a:
            if i != "":
                cellSplit.append(i)

        for i in range (0, len(cellSplit), 2):
            args = cellSplit[i].split(" ")
            values = cellSplit[i+1].split(" ")
            args = [ int(i) for i in args ]
            values = [ int(i) for i in values ]
            self.testCases.append(TestCase(n=args[0], m=args[1], d=args[2], k=args[3], i=values))

    def clearOutput(self):
        open(self.outFile, "w").close()      

    def readInput(self):
        cellSplit = []
        if self.method == INPUT_TERMINAL_METHOD:
            while True:
                try:
                    cellSplit.append(input())
                except:
                    break
                    
        elif self.method == INPUT_FILE_METHOD:
            f = open(self.inFile, "r")
            cellIn = f.read()
            cellSplit = cellIn.splitlines()
            f.close()

        self.fillTestCases(cellSplit)

    def writeOutput(self, output):
        output = "%s\n" % output
        if self.method == INPUT_TERMINAL_METHOD:
            print(output, end='')
        elif self.method == INPUT_FILE_METHOD:
            f = open(self.outFile, "a")
            f.write(output)
            f.close()
        
def main():
    # INPUT_TERMINAL_METHOD, INPUT_FILE_METHOD
    reader = Reader(method=INPUT_TERMINAL_METHOD)
    reader.readInput() 
    for test in reader.testCases:
        automaton = Automaton(size=test.n, limit=test.m, distance=test.d, initialValues=test.i)
        engine = Engine(executions=test.k, automaton=automaton)
        engine.run()
        reader.writeOutput(str(automaton))
    print()
main()
