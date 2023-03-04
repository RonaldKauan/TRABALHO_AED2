# Aplicacao de Heap Minima
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

# Remove elemento
def remove_element(heap):
    last_element = len(heap) - 1
    heap[0], heap[last_element] = heap[last_element], heap[0]
    heap.pop()
    min_heapify(heap, 0, len(heap))

# Retorna pai de um elemento
def parent(position):
    return int((position - 1) / 2)

 # Troca elementos
def swap(heap, position, parent_position):
    heap[position], heap[parent_position] = heap[parent_position], heap[position]

# Atualiza pilha
def update_heap(heap, position, new):
    heap.append(new)

    pai_pos = parent(position)

    while heap[position] < heap[pai_pos]:
        swap(heap, position, pai_pos)
        position = pai_pos
        pai_pos = parent(position)