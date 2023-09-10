"""
Adam Rodgers,  8/28/2023

This file implements an AVL tree to store the history of the users use of the weather application.
The AVL tree is sorted by the users username.
Three functions have been implmented for this self balancing AVL tree, a insert function, a retrieve function, and a display function.
Along with there supporting functions.

"""


from application import application

"""
Node class for AVL tree
"""
class node:
    def __init__(self): #constructor 
        self.username = None
        self.history = None
        self.right = None
        self.left = None
        self.height = 1

    def print(self): #print function to make code cleaner
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("  Username: ", self.username)
        print("  History:   ", self.history)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^\n")

"""
AVL tree class
sorted by username
data gotten from application class
"""
class AVL:
    def __init__(self): #constructor 
        self.root = None

    def load(self): # load function to set data and make new node, also serves as a wrapper function for insert
        new_node = node()
        app = application()
        new_node.username = input("Please enter username: ")
        new_node.history = app.run()
        new_node.print()
        self.root = self.insert(self.root, new_node)

    """
    Main insert function
    """
    def insert(self, curr, new_node): 
        if not curr:
            return new_node
       
        if new_node.username < curr.username: # Go right or left is new_node username is smaller or larger
            curr.left = self.insert(curr.left, new_node)
        elif new_node.username > curr.username:
            curr.right = self.insert(curr.right, new_node)
        else:
            return curr
        
        #keeps track of height and balance
        curr.height = 1 + max(self.get_height(curr.left), self.get_height(curr.right)) 
        balance = self.get_balance(curr)

        #if left is more
        if balance > 1:
            if new_node.username < curr.left.username:
                return self.rotate_right(curr) #Left left case
            else:
                curr.left = self.rotate_left(curr.left) #left right case
                return self.rotate_right(curr)
            
        #if right is more
        if balance < -1:
            if new_node.username > curr.right.username:
                return self.rotate_left(curr) #Right right case
            else:
                curr.right = self.rotate_right(curr.right) #Right left case
                return self.rotate_left(curr)
            
        return curr
    
    #right rotation function
    def rotate_right(self, curr): 
        new_root = curr.left #holds data
        hold = new_root.right

        new_root.right = curr #rotates
        curr.left = hold

        #updates height
        curr.height = 1 + max(self.get_height(curr.left), self.get_height(curr.right))
        new_root.height = 1 + max(self.get_height(curr.left), self.get_height(curr.right))

        return new_root
    
    def rotate_left(self, curr):
        new_root = curr.right#holds data
        hold = new_root.left

        new_root.left = curr#rotates
        curr.right = hold

        #updates height
        curr.height = 1 + max(self.get_height(curr.left), self.get_height(curr.right))
        new_root.height = 1 + max(self.get_height(curr.left), self.get_height(curr.right))

        return new_root
    
    #get height function, needed to check if right/left exists. If not return 0
    def get_height(self, root): 
        if not root:
            return 0
        return root.height
    
    #get balance function, needed to check if right/left exists. If not return 0
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    

    #retrieve wrapper function
    def retrieve(self, search):
         return self.__retrieve(self.root, search)
    
    #retrieve function  
    def __retrieve(self, curr, search):
        if not curr:
            return
        if curr.username == search: #if its the data searched
            curr.print()
            return curr.username
        elif curr.username > search: #searches by username to make retrieval faster 
            self.__retrieve(curr.left, search)
        else:
            self.__retrieve(curr.right, search)
    
    #display wrapper function
    def display(self):
        self.__display(self.root)
        return

    #display function, inorder
    def __display(self, root):
        if not root:
            return
        self.__display(root.left)
        root.print()
        self.__display(root.right)