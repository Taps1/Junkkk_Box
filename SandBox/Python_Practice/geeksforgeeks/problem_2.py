"""Given an integer "K" and a binary tree in string format. Every node of a tree has value in range from 0 to 9. We need to find product of elements at K-th level from root. The root is at level 0.
Tree is given in the form: (node value(left subtree)(right subtree))

Examples:

Input : tree = "(0(5(6()())(4()(9()())))(7(1()())(3()())))" 
        k = 2
        Output : 72"""

def get_product(node_string, k):
    product = 1
    level = -1
    iter_ss = iter(node_string)
    for ch in iter_ss:
        if ch == '(':
            level += 1
        elif ch == ')':
            level -= 1
        else:
            if level == int(k):
                product = product*int(ch)
    print product

if __name__ == "__main__":
    node_string = raw_input("Provide me the string: ")
    k = raw_input("Provide me the level: ")
    get_product(node_string, k)
