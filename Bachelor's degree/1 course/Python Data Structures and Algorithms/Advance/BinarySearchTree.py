from binarytree import Node


class DrawBinaryTree:
    # Клас, який буде додавати вершини до дерева, яке буде виведено за допомогою псевдографіки
    root = None

    def Add_For_Drawing(self, vertex):
        if self.root is not None:
            temp = self.root
            while True:
                if vertex > temp.value:
                    if temp.right is not None:
                        temp = temp.right
                    else:
                        temp.right = Node(vertex)
                        break
                else:
                    if temp.left is not None:
                        temp = temp.left
                    else:
                        temp.left = Node(vertex)
                        break
        else:
            self.root = Node(vertex)


class Vertex:
    # Допоміжний клас - вершина бінарного дерева пошуку """

    def __init__(self, item):
        """ Конструктор вершини

        :param item: Елемент бінарного дерева
        """
        self.key = item
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    # Бінарне дерево пошуку

    def __init__(self):
        """ Конструктор бінарного дерева пошуку – створює порожнє дерево """
        self.root = None
        self.vertex_set = []

    def Inorder_Tree_Walk(self, vertex) -> None:
        if vertex is not None:
            self.Inorder_Tree_Walk(vertex.left)
            print(vertex.key, end="  ")
            self.Inorder_Tree_Walk(vertex.right)
        return None

    def Add_For_Drawing(self, vertex):
        if self.root is not None:
            temp = self.root
            while True:
                if vertex > temp.value:
                    temp = temp.right
                    if temp.right is not None:
                        temp = temp.right
                    else:
                        temp.right = Node(vertex)
                        break
                else:
                    if temp.left is not None:
                        temp = temp.left
                    else:
                        temp.left = Node(vertex)
                        break
        else:
            self.root = Node(vertex)

    def Tree_Search(self, vertex, key) -> "Vertex object":
        while (vertex is not None) and (key != vertex.key):
            if key < vertex.key:
                vertex = vertex.left
            else:
                vertex = vertex.right
        return vertex

    def Tree_Minimum(self, vertex) -> "Vertex object":
        while vertex.left is not None:
            vertex = vertex.left
        return vertex

    def Tree_Maximum(self, vertex) -> "Vertex object":
        while vertex.right is not None:
            vertex = vertex.right
        return vertex

    def Tree_Successor(self, x_vertex) -> "Vertex object":
        if x_vertex.right is not None:
            return self.Tree_Minimum(x_vertex.right)
        y_vertex = x_vertex.parent
        while (y_vertex is not None) and (x_vertex == y_vertex.right):
            x_vertex = y_vertex
            y_vertex = y_vertex.parent
        return y_vertex

    def Tree_Predecessor(self, x_vertex) -> "Vertex object":
        if x_vertex.left is not None:
            return self.Tree_Maximum(x_vertex.left)
        y_vertex = x_vertex.parent
        while (y_vertex is not None) and (x_vertex == y_vertex.left):
            x_vertex = y_vertex
            y_vertex = y_vertex.parent
        return y_vertex

    def Tree_Insert(self, new_item) -> None:
        y_vertex = None
        x_vertex = self.root
        new_vertex = Vertex(new_item)
        while x_vertex is not None:
            y_vertex = x_vertex
            if new_vertex.key < x_vertex.key:
                x_vertex = x_vertex.left
            else:
                x_vertex = x_vertex.right
        new_vertex.parent = y_vertex
        if y_vertex is None:
            self.root = new_vertex
        elif new_vertex.key < y_vertex.key:
            y_vertex.left = new_vertex
        else:
            y_vertex.right = new_vertex
        return None

    def Tree_Delete(self, del_vertex) -> "Vertex object":
        if (del_vertex.left is None) or (del_vertex.right is None):
            y_vertex = del_vertex
        else:
            y_vertex = self.Tree_Successor(del_vertex)

        if y_vertex.left is not None:
            x_vertex = y_vertex.left
        else:
            x_vertex = y_vertex.right

        if x_vertex is not None:
            x_vertex.parent = y_vertex.parent

        if y_vertex.parent is None:
            self.root = x_vertex
        elif y_vertex == y_vertex.parent.left:
            y_vertex.parent.left = x_vertex
        else:
            y_vertex.parent.right = x_vertex

        if y_vertex != del_vertex:
            del_vertex.key = y_vertex.key
        return y_vertex
