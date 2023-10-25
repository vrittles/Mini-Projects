class Queue:
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.a = 0 #checjs the current size
        self.l = size - 1 #the first element
    
    def enqueue(self, x):
        if self.a == self.capacity:
            print("Queue Overflow!! Calling exit()...")
            exit(1)
        print(self.arr)
        print("Inserting", x,"into the queue...")
        self.a += 1
        self.arr[self.l] = x
        print(self.arr)
        self.l -= 1
    
    def dequeue(self):
        if self.a == 0:
            print("Queue Underflow!! Calling exit()...")
            exit(1)
        print("Removing",self.arr.pop(),"from the queue...")
        self.a -= 1

    def size(self):
        return self.a

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity


if __name__ == '__main__':
    print("Queue Operations")
    n = int(input("Enter the queue size: "))
    queue = Queue(n)
    while True:
        print("Select the queue operations: ")
        print(f'''1- for enqueue operations
              2- for dequeue operations
              3- to check ISFULL queue
              4- to check ISEMPTY queue
              5- to display queue size''')
        
        user_inp = int(input("Enter the valid option: "))
        if user_inp == 1:
            u_i = input("enter element to insert into queue: ")
            queue.enqueue(u_i)
        elif user_inp == 2:
            queue.dequeue()
        elif user_inp == 3:
            if queue.isFull():
                print("The queue is full")
            else:
                print("The queue is not full")
        elif user_inp == 4:
            if queue.isEmpty():
                print("The queue is empty")
            else:
                print("The queue is not empty")
        elif user_inp == 5:
            print("The stack size is",queue.size())
        else:
            print("Invalid Input")

        user_option = input("Do you want to continue: ").lower()
        if user_option in ('yes','y'):
            pass
        else:
            break