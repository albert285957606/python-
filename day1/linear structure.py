#线性结构
#栈
#栈的简单应用之括号匹配


class Stack_zuo:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.insert(0,item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)

class Stack_you:
    def __init__(self):
        self.items = []
        #self.a = a
        #self.name =name
        print("列表创建")
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
"""
def perChecker(symbolString):
    s = Stack_you("init")
    balanced =True
    index =0
    while index <len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:return False
"""
def perChecker(symbolString):
    s = Stack_you()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):#False
                    balanced = False
        index = index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False
def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

#print(perChecker('{{([][])}()}'))

#十进制转换为二进制
def divideBy(decNumber):
    remstack = Stack_you()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2 #2
    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
    return binString
#print(divideBy(42))

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack_you()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base #2
    binString = ""
    while not remstack.isEmpty():
        binString = binString + digits[remstack.pop()]
    return binString
#print(baseConverter(25,16))

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack_you()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLNMOPQRSTUVWSYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token ==')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while(not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

