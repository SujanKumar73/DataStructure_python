class BST:
    class TreeNode:
        def __init__(self, ele):
            self.data=ele
            self.left=None
            self.right=None

    def __init__(self):
        self.root=None
        self.count=0

    def is_empty(self):
        return self.count==0

    def length(self):
        return self.count

    def add_node(self,data):
        parent=current=self.root
        while current is not None and current.data != data:
            parent = current
            if data < current.data:
                current=current.left
            elif data > current.data:
                current=current.right
        if current is None:
            new_node=self.TreeNode(data)
            if parent is None:
                self.root=new_node
            elif data < parent.data:
                parent.left=new_node
            elif data > parent.data:
                parent.right=new_node
            self.count+=1

    def is_member(self,key):
        if not self.is_empty():
            current=self.root
            while current is not None:
                if key < current.data:
                    current=current.left
                elif ke > current.data:
                    current=current.right
                else:
                    break
            return current!=None

    def inorder(self):
            if not self.is_empty():
                print("Root. data is ",self.root.data)
                self._inorder(self.root)

    def _inorder(self,root):
        if root is not None:

            self._inorder(root.left)
            print root.data
            self._inorder(root.right)
