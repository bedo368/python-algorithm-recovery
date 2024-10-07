class CircularQueue:


    def __init__(self , size :int, ):
        self.size = size
        self.front = self.rear = 0
        self.queue = [None] * self.size


    def enqueue(self, element ):

        if self.is_full() :
            print('Queue is full')
            return
        self.queue[self.rear] = element
        self.rear = (self.rear + 1) % self.size





    def dequeue(self):
        if self.is_empty() :
            print('Queue is empty')
            return
        val =  self.queue[self.front]
        self.queue[self.front] = None

        self.front = (self.front + 1) % self.size
        return  val

        pass

    def is_empty(self):
        if self.front == self.rear:
            self.front = self.rear = 0
            return True
        pass

    def is_full(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        return False

    def peek(self):
        """
        Get the front element without removing it.

        :return: The front element of the queue.
        """
        if self.is_empty():
            print("Queue is empty! Nothing to peek.")
            return None
        return self.queue[self.front]

    def display(self):
        """
        Display the current state of the queue.
        """
        if self.is_empty():
            print("Queue is empty!")
            return
        print("Queue state:")
        index = self.front

        print(self.queue)




q = CircularQueue(10)
q.enqueue(3)
q.display()

q.enqueue(5)
q.display()

q.enqueue(7)
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.enqueue(6)
q.display()
