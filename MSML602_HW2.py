import csv
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class HomeWork2:

    # Problem 1: Construct an expression tree (Binary Tree) from a postfix expression
    # input -> list of strings (e.g., [3,4,+,2,*])
    # this is parsed from p1_construct_tree.csv (check it out for clarification)

    # there are no duplicate numeric values in the input
    # support basic operators: +, -, *, /

    # output -> the root node of the expression tree. Here: [*,+,2,3,4,None,None]
    # Tree Node with * as root node, the tree should be as follows
    #         *
    #        / \
    #       +   2
    #      / \
    #     3   4

    def constructBinaryTree(self, input) -> TreeNode:
        stack = []

        # check empty input
        if input is None or len(input) == 0:
            raise ValueError("Empty postfix expression")

        for element in input:
            element = element.strip()

            # check if it is one of the operators
            if element == "+" or element == "-" or element == "*" or element == "/":

                # make sure there are at least two operands
                if len(stack) < 2:
                    raise ValueError("Invalid postfix expression (insufficient operands)")

                rightNode = stack.pop()
                leftNode = stack.pop()

                newNode = TreeNode(element)
                newNode.left = leftNode
                newNode.right = rightNode

                stack.append(newNode)

            else:
                # basic validation that it is a number
                try:
                    int(element)
                except ValueError:
                    raise ValueError("Invalid token in postfix expression")

                valueNode = TreeNode(element)
                stack.append(valueNode)

        # after processing everything, there should be exactly one element
        if len(stack) != 1:
            raise ValueError("Malformed postfix expression (too many operands)")

        return stack[0]
            
    
    # Problem 2.1: Use pre-order traversal (root, left, right) to generate prefix notation
    # return an array of elements of a prefix expression
    # expected output for the tree from problem 1 is [*,+,3,4,2]
    # you can see the examples in p2_traversals.csv

    def prefixNotationPrint(self, head: TreeNode) -> list:
        result = []

        def helper(node):
            if node is None:
                return
            
            # first add the root
            result.append(node.val)
            
            # then go to left subtree
            helper(node.left)
            
            # then go to right subtree
            helper(node.right)

        helper(head)

        return result

    # Problem 2.2: Use in-order traversal (left, root, right) for infix notation with appropriate parentheses.
    # return an array of elements of an infix expression
    # expected output for the tree from problem 1 is [(,(,3,+,4,),*,2,)]
    # you can see the examples in p2_traversals.csv

    # don't forget to add parentheses to maintain correct sequence
    # even the outermost expression should be wrapped
    # treat parentheses as individual elements in the returned list (see output)

    def infixNotationPrint(self, head: TreeNode) -> list:
        result = []

        def helper(node):
            if node is None:
                return
            
            # if this node has children, it is an operator
            if node.left is not None or node.right is not None:
                result.append("(")
            
            # go left
            helper(node.left)
            
            # add current value
            result.append(node.val)
            
            # go right
            helper(node.right)
            
            # close parentheses if it was an operator
            if node.left is not None or node.right is not None:
                result.append(")")

        helper(head)

        return result
        
    # Problem 2.3: Use post-order traversal (left, right, root) to generate postfix notation.
    # return an array of elements of a postfix expression
    # expected output for the tree from problem 1 is [3,4,+,2,*]
    # you can see the examples in p2_traversals.csv

    def postfixNotationPrint(self, head: TreeNode) -> list:
        result = []

        def helper(node):
            if node is None:
                return
            
            # first go left
            helper(node.left)
            
            # then go right
            helper(node.right)
            
            # then add current value
            result.append(node.val)

        helper(root)

        return result
    
class Stack:
    # Implement your stack using either an array or a list
    # (i.e., implement the functions based on the Stack ADT we covered in class)
    # You may use Python's list structure as the underlying storage.
    # While you can use .append() to add elements, please ensure the implementation strictly follows the logic we discussed in class
    # (e.g., manually managing the "top" of the stack
    
    # Use your own stack implementation to solve problem 3

    # initialize a stack
    def __init__(self):
        self.arr = []
        self.top = -1   # start with empty stack

    # add a value to the stack
    def push(self, value):
        self.arr.append(value)
        self.top = self.top + 1

    # delete the top of the stack
    def pop(self):
        if self.top == -1:
            raise IndexError("Stack is empty")
        
        value = self.arr[self.top]
        self.arr.pop()
        self.top = self.top - 1
        return value

    # check to see if the stack is empty
    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    # Problem 3: Write code to evaluate a postfix expression using stack and return the integer value
    # Use stack which you implemented above for this problem

    # input -> a postfix expression string. E.g.: "5 1 2 + 4 * + 3 -"
    # see the examples of test entries in p3_eval_postfix.csv
    # output -> integer value after evaluating the string. Here: 14

    # integers are positive and negative
    # support basic operators: +, -, *, /
    # handle division by zero appropriately

    # DO NOT USE EVAL function for evaluating the expression

    def evaluatePostfix(self, exp: str) -> int:

        # check empty input
        if exp is None or exp.strip() == "":
            raise ValueError("Empty postfix expression")

        stack = Stack()
        elements = exp.split()

        for e in elements:

            if e == "+" or e == "-" or e == "*" or e == "/":

                # check if there are at least two operands
                if stack.top < 1:
                    raise ValueError("Malformed expression: insufficient operands")

                val2 = stack.pop()
                val1 = stack.pop()

                if e == "+":
                    ans = val1 + val2

                elif e == "-":
                    ans = val1 - val2

                elif e == "*":
                    ans = val1 * val2

                else:
                    if val2 == 0:
                        raise ZeroDivisionError("cannot divide by zero")
                    ans = int(val1 / val2)

                stack.push(ans)

            else:
                try:
                    stack.push(int(e))
                except ValueError:
                    raise ValueError("Invalid token in expression")

        # after processing, stack must contain exactly one value
        if stack.top != 0:
            raise ValueError("Malformed expression: too many operands")

        return stack.pop()
    
# Main Function. Do not edit the code below
if __name__ == "__main__":
    homework2 = HomeWork2()

    print("\nRUNNING TEST CASES FOR PROBLEM 1")
    testcases = []
    try:
        with open('p1_construct_tree.csv', 'r') as f:
            testcases = list(csv.reader(f))
    except FileNotFoundError:
        print("p1_construct_tree.csv not found")

    for i, (postfix_input,) in enumerate(testcases, 1):
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)
        output = homework2.postfixNotationPrint(root)

        assert output == postfix, f"P1 Test {i} failed: tree structure incorrect"
        print(f"P1 Test {i} passed")

    
    print("\nRUNNING TEST CASES FOR PROBLEM 2")
    testcases = []
    with open('p2_traversals.csv', 'r') as f:
        testcases = list(csv.reader(f))

    for i, row in enumerate(testcases, 1):
        postfix_input, exp_pre, exp_in, exp_post = row
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)

        assert homework2.prefixNotationPrint(root) == exp_pre.split(","), f"P2-{i} prefix failed"
        assert homework2.infixNotationPrint(root) == exp_in.split(","), f"P2-{i} infix failed"
        assert homework2.postfixNotationPrint(root) == exp_post.split(","), f"P2-{i} postfix failed"

        print(f"P2 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 3")
    testcases = []
    try:
        with open('p3_eval_postfix.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                testcases.append(row)
    except FileNotFoundError:
        print("p3_eval_postfix.csv not found")

    for idx, row in enumerate(testcases, start=1):
        expr, expected = row

        try:
            s = Stack()
            result = s.evaluatePostfix(expr)
            if expected == "DIVZERO":
                print(f"Test {idx} failed (expected division by zero)")
            else:
                if "E" in expected or "e" in expected:
                    expected = int(float(expected))
                else:
                    expected = int(expected)
                assert result == expected, f"Test {idx} failed: {result} != {expected}"
                print(f"Test case {idx} passed")
        

        except ZeroDivisionError:
            assert expected == "DIVZERO", f"Test {idx} unexpected division by zero"
            print(f"Test case {idx} passed (division by zero handled)")
        
        except ValueError:
            assert expected == "VALERROR", f"Test {idx} unexpected value error"
            print(f"Test case {idx} passed (value error handled)")