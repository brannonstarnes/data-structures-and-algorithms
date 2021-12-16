from stack_and_queue.stack_and_queue import Stack

opening_brackets = ["[", "{", "("]
closing_brackets = ["]", "}", ")"]

rule = {"[":"]", "{":"}", "(":")" }

def validate_brackets(string):
    stack = Stack()
    for char in string:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if rule[stack.peek()] == char:
                stack.pop()
            else:
                return False
    if stack.is_empty():
            return True
    else:
        return False

