#creating a stack 
def create_stack():
    stack = []
    return stack 

#creating an empty stack
def check_empty(stack):
    return len(stack) ==0

#adding items onto  the stack
def push(stack,item):
    stack.append(item)
    print("pushed"  + item)

#removing an element from the stack
def  pop(stack):
    if(check_empty(stack)):
        return "stack is empty"

    return stack.pop()

stack = create_stack()
push(stack,str(1))

push(stack,str(2))
push(stack,str(3))
print("popped: " + pop(stack))
print("After popping: " + str(stack))