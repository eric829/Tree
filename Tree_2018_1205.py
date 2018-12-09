class Node:
    def __init__(self,val):
    	self.val= val
    	self.leftnode= None
    	self.rightnode =None

class Tree:
    def __init__(self):
        self.root = None  
    
    def insert(self,node,data):
        if self.root is None:
            self.root = Node(data)     
        else:
            current_node = node
            if data < current_node.val:
                if current_node.leftnode ==None:
                    current_node.leftnode= Node(data)
                        
                else:
                    current_node= current_node.leftnode
                    self.insert(current_node,data)
           
            elif data > current_node.val:
                if current_node.rightnode ==None:
                    current_node.rightnode= Node(data)
                        
                else:
                    current_node= current_node.rightnode
                    self.insert(current_node,data)
            else:
                return False              
            
            
    def find(self, current_node, parent_node ,data):

        if current_node is None:
            return False, current_node , parent_node        
        if data == current_node.val:
            return True, current_node , parent_node
        
        elif data < current_node.val:
            return self.find(current_node.leftnode, current_node, data)
        elif data > current_node.val:
            return self.find(current_node.rightnode, current_node , data)
                
    def printTree(self, current_node):
        if current_node.leftnode != None :
            self.printTree(current_node.leftnode)
        print current_node.val,
        if current_node.rightnode:
            self.printTree(current_node.rightnode)
    
    def find_min(self, tree):
    	current_node = tree
    	while True :
    		if current_node.leftnode is None:
    			return current_node
    		current_node = current_node.leftnode

            
    def delete(self,root,data):
        found, target_node, parent_node = self.find(root, root ,data)
        
        if found is True:   
            #有找到
            
            if target_node.leftnode is None and target_node.rightnode is None:
                #目標兩子樹空
                
                if parent_node.leftnode == data:
                    parent_node.leftnode = None
                else:
                    parent_node.rightnode = None
                    
            elif target_node.leftnode is None :       
                #目標左子樹空
                
                if parent_node.leftnode == data:
                    parent_node.leftnode= target_node.rightnode
                    
                else:
                    parent_node.rightnode= target_node.rightnode
                   
            elif target_node.rightnode is None :
                #目標右子樹空
                
                if parent_node.leftnode == data:
                    parent_node.leftnode= target_node.leftnode
                else:
                    parent_node.rightnode= target_node.leftnode
            
            else: 
                #目標雙子樹
                Rtree = target_node.rightnode
                min_node = self.find_min(Rtree)
                target_node.val = min_node.val
                self.delete(min_node)

        else:
            return "Not found "
            

            
atree = [150,30,75,85,160,170,190,210,300,320,350,700]
n = Tree()

for i in atree:
    n.insert(n.root,i)


n.printTree(n.root)
#print n.find(n.root,n.root,170)
n.delete(n.root,170)
print 
n.printTree(n.root)

#print n.find(n.root,33)
#print n.find(n.root,n.root,170)