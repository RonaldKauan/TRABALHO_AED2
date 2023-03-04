from time import sleep
import puzzle as Classe
import helpers as Heap

#Cores Axuliares para Interface
RED   = "\033[1;31m" 
RESET = "\033[0;0m"
GREEN = "\033[0;32m"
CYAN  = "\033[1;36m"

def action(again = False):
    puzzle.print_f()
    # Caso usuario digite um comando invalido
    if (again):
        print(RED + "Comando invalido, Por favor tente novamente" + RESET)
    print("movimentos possíveis:", puzzle.movements())
    comand = input("N para gerar uma nova configuração, R para resolver ou E para sair\nsua opção: ")
    print("")
    return comand


comand = None
again = False
puzzle = Classe.Puzzle()
while comand != "E":
    comand = action(again)
    again = False
    # Caso Movimentos esteja dentro dos permitidos
    if(comand in puzzle.movements()):
        puzzle.move(comand)
    # Gera uma nova configuracao
    elif(comand == "N"):
        puzzle = Classe.Puzzle()
    # Gera sequencia de comandos para resolver o puzzle
    elif(comand == "R"):
        heap = []
        memory = []
        first_config = Classe.Puzzle(puzzle.config.copy())

        # Caso a sequencia não possa ser resolvida
        if not(puzzle.check_solvable()):
            puzzle.print_f()
            print(RED + "Caso não solucionável!" + RESET)
            comand = ""

        # Caso a sequencia ja esteja resolvida
        if puzzle.calc_cost() == 0:
            print(GREEN + "Configuração já resolvida!" + RESET)
            comand = ""

        Heap.update_heap(heap, len(heap), puzzle)
        while(len(heap) != 0 and comand == "R"):
            aux = heap[0]
            Heap.remove_element(heap)

            for movement in aux.movements().replace(" ", ""):
                new_puzzle = Classe.Puzzle(aux.config.copy(), aux.solution + movement, aux.steps + 1)
                new_puzzle.move(movement)

                if new_puzzle.calc_cost() == 0:
                    first_config.print_f()
                    print("Passos para resolver:" + GREEN, ' '.join(list(new_puzzle.solution)))
                    comand = input(RESET + "Resolver?\n" + GREEN + "S(sim) " + RED + "N(não): "+ RESET)

                    #Mostra sequencia para resolver o puzzle
                    if(comand == "S"):
                        qty = 1
                        for m in list(new_puzzle.solution):
                            first_config.move(m)
                            print(GREEN + "Passo {}: ".format(qty) + CYAN + "{}".format(m) + RESET)
                            first_config.print_f()
                            qty += 1
                            sleep(1)
                        print(GREEN + "Puzzle resolvido com sucesso" + RESET)
                        puzzle = first_config  
                    elif(comand == "N"):
                        break

                if str(new_puzzle.config) not in memory:
                    memory.append(str(new_puzzle.config))
                    Heap.update_heap(heap, len(heap), new_puzzle)
    else:
        again = True

print(GREEN + "Fim de jogo. Espero que tenha se divertido :)" +RESET)