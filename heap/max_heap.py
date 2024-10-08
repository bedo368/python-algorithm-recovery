

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)

        if len(self.heap) == 1 :
            return
        self._heapify_up(len(self.heap) - 1)



    def delete(self):
        val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return  val

    def _heapify_up(self , i ) :
        current_node = i
        parent = int(current_node / 2)
        while current_node > 0:
            if self.heap[parent] >= self.heap[current_node]:
                break
            if self.heap[parent] < self.heap[current_node]:
                self.heap[parent], self.heap[current_node] = self.heap[current_node], self.heap[parent]
                current_node = parent
                parent = (current_node - 1) // 2

    def _heapify_down(self , i ):
        current_node = i
        n=len(self.heap)

        while True:
            left_child = 2 * current_node + 1
            right_child = 2 * current_node + 2
            largest = current_node

            if left_child < n and self.heap[left_child] > self.heap[right_child] and self.heap[current_node] < \
                    self.heap[left_child]:
                largest = left_child
            if right_child < n and self.heap[right_child] > self.heap[left_child] and self.heap[current_node] < \
                    self.heap[right_child]:
                largest = right_child

            if largest != current_node:

                self.heap[current_node], self.heap[largest] = self.heap[largest], self.heap[current_node]
                current_node = largest
            else:
                break



    def get_route (self):

        return self.heap[0]
    def __str__(self):
        return str(self.heap)













h = MaxHeap()

h.insert(1)
h.insert(5)
h.insert(4)
h.insert(3)
h.insert(2)
h.insert(7)
h.insert(9)
h.insert(49)
h.insert(10)
h.insert(18)
h.insert(55)
h.insert(90)
h.insert(43)
h.insert(47)
h.insert(66)

print(h.get_route())
print(h.delete())
print(h.delete())
print(h.delete())
print(h.delete())
print(h.delete())
print(h.delete())
print(h.delete())
print(h.delete())
print(h)
