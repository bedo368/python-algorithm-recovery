

class PriorityQueue :
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

        if len(self.queue) == 1 :
            return
        self._heapify_up(len(self.queue) - 1)



    def delete(self):
        val = self.queue[0]
        self.queue[0] = self.queue.pop()
        self._heapify_down(0)

        return  val

    def _heapify_up(self , i ) :
        current_node = i
        parent = int(current_node / 2)
        while current_node > 0:
            if self.queue[parent] >= self.queue[current_node]:
                break
            if self.queue[parent] < self.queue[current_node]:
                self.queue[parent], self.queue[current_node] = self.queue[current_node], self.queue[parent]
                current_node = parent
                parent = (current_node - 1) // 2

    def _heapify_down(self , i ):
        current_node = i
        n=len(self.queue)

        while True:
            left_child = 2 * current_node + 1
            right_child = 2 * current_node + 2
            largest = current_node

            if left_child < n and self.queue[left_child] > self.queue[right_child] and self.queue[current_node] < \
                    self.queue[left_child]:
                largest = left_child
            if right_child < n and self.queue[right_child] > self.queue[left_child] and self.queue[current_node] < \
                    self.queue[right_child]:
                largest = right_child

            if largest != current_node:

                self.queue[current_node], self.queue[largest] = self.queue[largest], self.queue[current_node]
                current_node = largest
            else:
                break



    def get_route (self):

        return self.queue[0]
    def __str__(self):
        return str(self.queue)













h = PrioriyQueue()

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
