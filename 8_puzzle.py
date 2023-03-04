from random import shuffle
from time import sleep
import os

def check_solvable(arr):
    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1

    return inv_count % 2 == 0

def generate_random_config():
    arr = [0,1,2,3,4,5,6,7,8]
    shuffle(arr)
    return arr

def min_heapify(heap, root, size):
    lower = root
    left = 2 * root + 1
    if left < size and heap[left] < heap[lower]:
        lower = left

    right = 2 * root + 2

    if right < size and heap[right] < heap[lower]:
        lower = right

    if lower != root:
        [heap[root], heap[lower]] = [heap[lower], heap[root]]
        min_heapify(heap, lower, size)


def remove_element(heap):
    last_element = len(heap) - 1

    heap[0], heap[last_element] = heap[last_element], heap[0]
    
    heap.pop()
 
    min_heapify(heap, 0, len(heap))


def parent(position):
    return int((position - 1) / 2)


def swap(heap, position, parent_position):
    heap[position], heap[parent_position] = heap[parent_position], heap[position]


def update_heap(heap, position, new):
    heap.append(new)

    pai_pos = parent(position)

    while heap[position] < heap[pai_pos]:
        swap(heap, position, pai_pos)
        position = pai_pos
        pai_pos = parent(position)


class Puzzle:
    rows = "rows"
    columns = "columns"
    index = "i"
    left = "l"
    right = "r"
    up = "u"
    down = "d"

    position = {rows: 0, columns: 0, index: None}
    possibilities = []

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

    def calc_h(self, c, i):
        rows_diff = abs((c // 3) - (i // 3))
        columns_diff = abs((c % 3) - (i % 3))
        return columns_diff + rows_diff
    
    def calc_cost(self):
        i = 0
        cost = 0
        for x in range(len(self.config)):
            if self.config[x] != i:
                cost += self.calc_h(self.config[x], i)
            i += 1  
        return cost

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

    def print_f(self):
        for index in range(len(self.config))[::3]:
            print(self.config[index], self.config[index + 1], self.config[index + 2])
        print("")

    def __init__(self, config=None, solution=None, steps=None):
        
        self.config = [0, 1, 2, 3, 4, 5, 6, 7, 8] if(config == None) else config
        
        self.solution = "" if(solution == None) else solution

        self.steps = 0 if(steps == None) else steps
        
        self.f = self.calc_cost() + self.steps

        for x in range(len(self.config)):
            if self.config[x] == 0:
                self.empty = x
        
    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return str(self.config)

movement = None

puzzle = Puzzle()

# os.system('cls')

while movement != "":

    puzzle.print_f()

    print("movimentos possíveis:", puzzle.movements())

    movement = input("R para gerar uma configuração, S para resolver\nsua opção: ")

    print("")

    if movement in puzzle.movements():
        puzzle.move(movement)

    elif(movement == "R"):
        puzzle = Puzzle(generate_random_config())
    
    # os.system('cls')

    if movement == "S":
        if(check_solvable(puzzle.config) == False):
            puzzle.print_f()
            print("não é solucionável")
            exit()
        first_config = Puzzle(puzzle.config.copy(),)

        heap = []

        memory = []

        if puzzle.calc_cost() == 0:
            print("configuração já resolvida!")
            exit()
        update_heap(heap, len(heap), puzzle)
        while(len(heap) != 0):
            puzzle = heap[0]

            remove_element(heap)

            for movement in puzzle.movements().replace(" ", ""):
                new_puzzle = Puzzle(puzzle.config.copy(), puzzle.solution + movement, puzzle.steps + 1)
                new_puzzle.move(movement)
                puzzle.possibilities.append(new_puzzle)

            for p in puzzle.possibilities:
                if p.calc_cost() == 0:
                    first_config.print_f()
                    print("passos para resolver:", ' '.join(list(p.solution)))
                    if(input("Resolver?\nS(sim) N(não): ") == "S"):
                        # os.system('cls')
                        for m in list(p.solution):
                            first_config.move(m)
                            print(m)
                            first_config.print_f()
                            sleep(1)
                            # os.system('cls')
                    first_config.print_f()
                    input()
                    exit()
                
                if str(p.config) not in memory:
                    memory.append(str(p.config))
                    update_heap(heap, len(heap), p)
        break