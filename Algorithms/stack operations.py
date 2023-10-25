class Stack:
    def __init__(self,size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1

    def push(self,x):
        if self.isFull():
            print("Stack Overflow!! Calling exit()...")
            exit(1)
        print("Inserting", x,"into the stack...")
        self.top = self.top + 1
        self.arr[self.top] = x

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow!! Calling exit()...")
            exit(1)
        print("Removing",self.peek(),"from the stack...")

        top = self.arr[self.top]
        self.top = self.top - 1
        return top

    def peek(self):
        if self.isEmpty():
            exit(1)
        return self.arr[self.top]

    def size(self):
        return self.top + 1

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity

if __name__ == '__main__':
    print("Stack Operations")
    n = int(input("Enter the stack size: "))
    stack = Stack(n)
    while True:
        print("Select the stack operations: ")
        print(f'''1- for Push operations
              2- for POP operations
              3- to check stack ISEMPTY
              4- to display top element
              5- to display stack size''')
        
        user_inp = int(input("Enter the valid option: "))
        if user_inp == 1:
            u_i = input("enter element to Push into stack: ")
            stack.push(u_i)
        elif user_inp == 2:
            stack.pop()
        elif user_inp == 3:
            if stack.isEmpty():
                print("The stack is empty")
            else:
                print("The stack is not empty")
        elif user_inp == 4:
            print("Top element is",stack.peek())
        elif user_inp == 5:
            print("The stack size is",stack.size())
        else:
            print("Invalid Input")

        user_option = input("Do you want to continue: ").lower()
        if user_option in ('yes','y'):
            pass
        else:
            break