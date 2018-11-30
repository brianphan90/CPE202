class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items ==[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop(len(self.items)-1)
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def check_prec(op):
    if op == "/"or op =="*":
        return 3
    if op == "+" or op == "-":
        return 2
    if op == ")" or "(":
        return 1
def compute(op, a, b):
    if op == "*":
        return str(float(a) * float(b))
    if op == "/":
        return str(float(a) / float(b))
    if op == "+":
        return str(float(a) + float(b))
    if op == "-":
        return str(float(a) - float(b))
def operate(given_op, operator_s, operand_s, done = False):
    if given_op == "(":
        operator_s.push(given_op)
        return
    op_prec= check_prec(given_op)
    topOp = operator_s.peek()
    top_prec= check_prec(topOp)
    while op_prec <= top_prec:                 #if given_op precedence is less than top operate        
        topOp = operator_s.pop()        
        if topOp == "("and given_op == ")": #done operating
            return        
        if topOp in "+-/*":
            value_one = operand_s.pop()
            value_two = operand_s.pop()
            res = compute(topOp, value_two, value_one)
            operand_s.push(res)             #pop everything from operator stack except "("
            
        topOp = operator_s.peek()
        top_prec= check_prec(topOp)                
    operator_s.push(given_op)       
def eval_infix(express):
    operand_stack = Stack()
    operator_stack = Stack()
    operator_stack.push("(")
    express_lst = express.split()
    express_lst.append(")")
    for token in express_lst:
        if token.isdigit() == True:
            operand_stack.push(token)                               # if token is a number push on the number stack 
        elif token in "+-/*)":
            operate(token, operator_stack, operand_stack)        
        elif token == "(":
            operator_stack.push(token)
    while "+-*/" in operator_stack.items:
        given_0 = operator_stack.pop()
        operate(given_0, operator_stack,operand_stack)
    return float(operand_stack.pop())
    

 

