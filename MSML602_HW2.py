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
        for element in input:
            element = element.strip()
            
            # check if it is one of the operators
            if element == "+" or element == "-" or element == "*" or element == "/":
                
                # pop twice because operator needs two operands
                rightNode = stack.pop()
                leftNode = stack.pop()
                
                # create a new node for the operator
                newNode = TreeNode(element)
                
                # attach children
                newNode.left = leftNode
                newNode.right = rightNode
                
                # push back to stack
                stack.append(newNode)
            
            else:
                # if it's not an operator, treat it like a value
                valueNode = TreeNode(element)
                stack.append(valueNode)

        # after processing everything, stack should have one element
        if len(stack) > 0:
            return stack[0]
        else:
            return None
        
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