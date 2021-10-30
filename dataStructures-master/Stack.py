class Stack:
    dataList = list()
    maxSize = 0 #0 = Infinity

    def __init__(self,maxSize=0):
        self.dataList = list()
        self.maxSize = maxSize

    # Stores an element on the stack
    def push(self,element):
        success = False
        if self.isFull() == False:
            self.dataList.append(element)
            success = True
        else:
            print "Stack is full. Cannot push last item to stack."
        return success

    # Removes the last element of the stack
    def pop(self):
        element = ''
        if isEmpty == False:
            element = self.peek()
            self.dataList.pop()
            return element
        else:
            print "Stack is empty. Cannot pop last item off."
            return False

    # Looks at the last element of the stack without removing it
    def peek(self):
        if isEmpty == False:
            index = len(self.dataList)
            element = self.dataList[index-1]
            return element
        else:
            print "Stack is empty. Cannot peek at the last item."
            return False

    # Check if stack is empty
    def isEmpty(self):
        retval = False
        size = len(self.dataList)
        if size <= 0:
            retval = True
        return retval

    # Checks if stack is full
    def isFull(self):
        retval = False
        size = len(self.dataList)
        if size >= self.maxSize and self.maxSize != 0:
            retval = True
        return retval

# Procedure
stack = Stack(10)
index = 1
continueAdding = True
while (continueAdding):
    continueAdding = stack.push(index)
    index+=1
isEmpty = stack.isEmpty()
if isEmpty == True:
    print "The Stack is Empty"
else:
    print "The Stack is not Empty"
lastElement = stack.peek()
print "Last item on stack is " + str(lastElement)
stack.pop()
print "Popped off last item on stack"
print "Now latest item is " + str(stack.peek())