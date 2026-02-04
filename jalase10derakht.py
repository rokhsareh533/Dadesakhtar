def Build_Tree(preorder,inorder):
    if not preorder or not inorder:
        return None
    val = preorder[0]
    index = inorder.index[val]
    N = Tree_Node(val)
    N.left = Build_Tree(preorder[1:index], inorder[:index])
    N.right = Build_Tree(preorder[:1+index], inorde[1+index:])




def inv_Tree(root):
    if not root:
        return None
    root.left , root.right = root.right , root.left
    inv_Tree(root.left)
    inv_Tree(root.right)


class Tree_Node:
    def__init__(self,D):
       self.value = D 
       self.Lchild = None
       self.Rchild = None
      


def search (root, target) :
   if root is None:
       return False
    if root. value == target :
       return True
    return search (root.left, target)
           OR
        Search (root-rights target)
   



def Sum_ Nodes (root) :
    If root is none:
       return 0
    return Sum_Nodes (root. left )
           + sum_Nodes (root right)
            + root-value