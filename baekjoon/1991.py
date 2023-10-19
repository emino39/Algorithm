def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

N = int(input())
tree = dict()

for n in range(N):
    parent, left, right = map(str, input().split())
    tree[parent] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')