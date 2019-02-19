class Stack:
    def __init__(self):
        self.stack=[]
    def isempty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.isempty():
            print("the stack is under flow")
        else:
            return (self.stack.pop())
    def size(self):
        print(len(self.stack))
    def peek(self):
        return (self.stack[-1])
a=Stack()
prec={}
prec['/']=3
prec['*']=3
prec['+']=2
prec['-']=2
prec['(']=1
dup=''
while True:
    expre = input("enter the expretion:")
    for i in expre:
        if i.isalpha():
            dup += i
        elif i is '(':
            a.push(i)
        elif i in '+ - / *' and a.isempty():
            a.push(i)

        elif i is ')':
            if a.isempty():
                print("the stack is under flow")
            else:
                while a.peek() != '(':
                    dup += a.peek()
                    a.pop()
                a.pop()
        else:
            while (not a.isempty()) and prec[a.peek()] >= prec[i]:
                dup += a.pop()
            a.push(i)

    while not a.isempty():
        dup += a.pop()
    print(dup)
