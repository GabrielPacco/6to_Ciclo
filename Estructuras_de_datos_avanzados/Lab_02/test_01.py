import plotly.express as px
import random as rd 
import numpy as np
import pandas as pd
import csv
#df = px.data.tips()
#fig = px.box(df, x="day", y="total_bill", color="smoker", notched=True)
#fig.show()


# Red-BLACK TREE Implementation	

class Node:
    def __init__(self, key, color):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
    
    def __str__(self):
        return str(self.key)

class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, 'black')
        self.root = self.nil

    def insert(self, key):
        node = Node(key, 'red')
        node.left = self.nil
        node.right = self.nil
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == self.nil:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        if node.parent == self.nil:
            node.color = 'black'
            return
        if node.parent.parent == self.nil:
            return
        self.fix_insert(node)

    def fix_insert(self, node):
        while node.parent.color == 'red':
            if node.parent == node.parent.parent.right:
                y = node.parent.parent.left
                if y.color == 'red':
                    y.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
            else:
                y = node.parent.parent.right
                if y.color == 'red':
                    y.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 'black'

    def left_rotate(self, node):
        y = node.right
        node.right = y.left
        if y.left != self.nil:
            y.left.parent = node
        y.parent = node.parent
        if node.parent == self.nil:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.left = node
        node.parent = y

    def right_rotate(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.nil:
            y.right.parent = node
        y.parent = node.parent
        if node.parent == self.nil:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def print_tree(self):
        self.print_helper(self.root, "", True)

    def print_helper(self, node, indent, last):
        if node != self.nil:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "
            s_color = "R" if node.color == "red" else "B"
            print(str(node.key) + "(" + s_color + ")")
            self.print_helper(node.left, indent, False)
            self.print_helper(node.right, indent, True)

    def search(self, key):
        return self.search_helper(self.root, key)
    
    def search_helper(self, node, key):
        if node == self.nil or key == node.key:
            return node
        if key < node.key:
            return self.search_helper(node.left, key)
        return self.search_helper(node.right, key)

    def minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.nil:
            node = node.right
        return node

    def successor(self, node):
        if node.right != self.nil:
            return self.minimum(node.right)
        y = node.parent
        while y != self.nil and node == y.right:
            node = y
            y = y.parent
        return y

    def predecessor(self, node):
        if node.left != self.nil:
            return self.maximum(node.left)
        y = node.parent
        while y != self.nil and node == y.left:
            node = y
            y = y.parent
        return y

    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, key):
        z = self.search(key)
        if z == self.nil:
            return
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left

            self.transplant(z, z.left)

        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'black':
            self.fix_delete(x)

    def fix_delete(self, node):
        while node != self.root and node.color == 'black':
            if node == node.parent.left:
                w = node.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    node.parent.color = 'red'
                    self.left_rotate(node.parent)
                    w = node.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    node = node.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = node.parent.right
                    w.color = node.parent.color
                    node.parent.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                w = node.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    node.parent.color = 'red'
                    self.right_rotate(node.parent)
                    w = node.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    node = node.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.left_rotate(w)
                        w = node.parent.left
                    w.color = node.parent.color
                    node.parent.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = 'black'

    def height(self, node):
        if node == self.nil:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def print_level_order(self):
        h = self.height(self.root)
        for i in range(1, h + 1):
            self.print_given_level(self.root, i)

    def print_given_level(self, node, level):
        if node == self.nil:
            return
        if level == 1:
            print(node.key, end=" ")
        elif level > 1:
            self.print_given_level(node.left, level - 1)
            self.print_given_level(node.right, level - 1)
            
    def print_level_order(self):
        h = self.height(self.root)
        for i in range(1, h + 1):
            self.print_given_level(self.root, i)

    def print_given_level(self, node, level):
        if node == self.nil:
            return
        if level == 1:
            print(node.key, end=" ")
        elif level > 1:
            self.print_given_level(node.left, level - 1)
            self.print_given_level(node.right, level - 1)



     # Root path to a random node
    def root_path(self, node):
        path = []
        while node != self.nil:
            path.append(node.key)
            node = node.parent
        return path
    

if __name__ == '__main__':

    nodos_rbt = []
    indice = []
    recorrido = []
    recorrido_aux = []
    for i in range(100):

        tree = RedBlackTree()
        array = []
        # insert
        for j in range(100):
            random = rd.randint(0, 10000)
            array.append(random)
            tree.insert(random)
        
        nodos_rbt.append(array)
        indice.append(i)
        

        # choise a random node
        random_node = rd.choice(array)
        print("Random node: ", random_node)

        
        for i in tree.root_path(tree.search(random_node)):
            recorrido.append(tree.root_path(tree.search(random_node)))
            
        recorrido_aux.append(recorrido)

    # Plotly visualization

    print (recorrido)

    # Exportar los 3 arrays en un solo archivo
    
    def exportar_csv():
        with open('exportar.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["indice", "nodos_rbt", "recorrido"])
            for i in range(100):
                writer.writerow([indice[i], nodos_rbt[i], recorrido_aux[i]])
    
    exportar_csv()


    
    # Graficas los datos del archivo exportar.csv con plotly boxplot

    df = pd.read_csv('exportar.csv')
    fig = px.box(df, x="nodos_rbt", y="recorrido", points="all")
    fig.show()

    

    

    







