from random import shuffle

class Puzzle:
    # Variaveis
    rows, columns, index = "rows","columns", "i"
    left, right, up, down = "l",  "r", "u", "d"
    position = {rows: 0, columns: 0, index: None}
    possibilities = []
    

    # Override dos metodos de comparacao e representacao ('<','print')
    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return str(self.config)

    # Construtor da classe
    def __init__(self, config = None, solution = None, steps=None):
        
        # Caso nenhuma configuracao seja passada, gera uma nova aletoriamente
        self.config = self.generate_random_config() if(config == None) else config
        
        self.solution = "" if(solution == None) else solution

        self.steps = 0 if(steps == None) else steps
        
        self.f = self.calc_cost() + self.steps

        for x in range(len(self.config)):
            if self.config[x] == 0:
                self.empty = x

    # Gera configuracao aleatoria
    def generate_random_config(self):
        arr = [0,1,2,3,4,5,6,7,8]
        shuffle(arr)
        return arr

    # Verifica se o puzzle possui solucao
    def check_solvable(self):
        inv_count = 0
        empty_value = 0
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if self.config[j] != empty_value and self.config[i] != empty_value and self.config[i] > self.config[j]:
                    inv_count += 1  

        return inv_count % 2 == 0

    # Move espaço vazio conforme comando
    def move(self, m):
        chosen = None
        if m == self.left:
            chosen = self.empty + 1
        elif m == self.right:
            chosen = self.empty - 1
        elif m == self.up:
            chosen = self.empty + 3
        elif m == self.down:
            chosen = self.empty - 3
        self.config[self.empty], self.config[chosen] = self.config[chosen], self.config[self.empty],
        
        for x in range(len(self.config)):
            if self.config[x] == 0:
                self.empty = x

        self.f = self.steps + self.calc_cost()
    
    # Calcula custo de cada peça
    def calc_cost(self):
        i = 0
        cost = 0
        for x in range(len(self.config)):
            if self.config[x] != i:
                cost += self.calc_h(self.config[x], i)
            i += 1  
        return cost

    # Calcula heuristica
    def calc_h(self, c, i):
        rows_diff = abs((c // 3) - (i // 3))
        columns_diff = abs((c % 3) - (i % 3))
        return columns_diff + rows_diff

    # Verifica quais movimentos estão disponiveis
    def movements(self):
        allowed_moves = ""
        for x in range(len(self.config)):
            if self.config[x] == 0:
                self.position[self.rows] = x // 3
                self.position[self.columns] = x % 3
        
        if self.position[self.rows] != 0:
            allowed_moves += self.down

        if self.position[self.rows] != 2:
            allowed_moves += self.up

        if self.position[self.columns] != 0:
            allowed_moves += self.right

        if self.position[self.columns] != 2:
            allowed_moves += self.left

        return ' '.join(list(allowed_moves)) 

    # Imprime a configuracao
    def print_f(self):
        for index in range(len(self.config))[::3]:
            print(self.config[index], self.config[index + 1], self.config[index + 2])
        print("")