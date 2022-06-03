
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insertLeft(self,key):
        if self.left == None:
            self.left = Node(key)
        else:
            node = Node(key)
            node.left = self.left
            self.left = node

    def insertRight(self,key):
        if self.right == None:
            self.right = Node(key)
        else:
            node = Node(key)
            node.right = self.right
            self.right = node
    
if __name__ == '__main__':
    r = Node('A')
    print(r.key)
    print(r.left)
    r.insertLeft('B')
    print(r.left.key)
    r.insertRight('C')
    print(r.right.key)
    r.right.key = 'hello'
    print(r.right.key)
