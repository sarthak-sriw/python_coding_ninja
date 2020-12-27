#Stack Using LL

class Stack :
    #Define data members and __init__()
    '''----------------- Public Functions of Stack -----------------'''
    def __init__(self):
        self.head = None
        self.count = 0
    
    def getSize(self) :
        return self.count
    #Implement the getSize() function

    def isEmpty(self) :
        if self.head == None:
            return True
        else:
            return False
        #Implement the isEmpty() function

    def push(self, data) :
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
        self.count +=1
        #Implement the push(element) function
		
    def pop(self) :
        if self.head == None:
            return None
        else:
            nodedelete = self.head
            self.head = self.head.next
            nodedelete.next = None
            self.count -= 1
            return nodedelete.data
        
        #Implement the pop() function

    def top(self) :
        if self.head == None:
            return None
        else:
            return self.head.data        
	#Implement the top() function

# Stack using array

arr = []

######push
arr.insert(0,data)

##### pop
arr.pop(0)

####top
arr[0]
	
	
##########################Balanced Paranthesis


def isBalanced(expr):
    s=[]
    for char in expr:
        if char in '({[':
            s.append(char)
        elif char is ')':
            if (not s or s[-1]!="("):
                return False
            s.pop()
        elif char is '}':
            if (not s or s[-1]!="{"):
                return False
            s.pop()
        elif char is ']':
            if (not s or s[-1]!="["):
                return False
            s.pop()
    if not s:
        return True
    return False


######################Check redundant brackets

# Input: 
# ((a+b))
# (a+(b)/c)
# (a+b*(c-d))
# Output: 
# Yes
# Yes
# No

# Explanation:
# 1. ((a+b)) can reduced to (a+b), this Redundant
# 2. (a+(b)/c) can reduced to (a+b/c) because b is
# surrounded by () which is redundant.
# 3. (a+b*(c-d)) doesn't have any redundant or multiple
# brackets.

def checkRedundantBrackets(expression) :
    
    l1 = []
    
    for i in expression:
        if i != ')':
            l1.append(i)
        else:
            count = 0
	
	###while loop is to check this condition () and  (a)
            while l1[-1] != '(':
                count += 1
                l1.pop()
            if count == 0 or count == 1:
                return True
            if count != 0 or count !=1:
                l1.pop()
		
    return False   
    
    ################# Reverse Stack
    arr = [1,2,3,4,5,6]
    #1. arr[::-1]

#2   i = 0
# while i!=len(arr):
#     arr.insert(i,arr.pop())
#     i+=1    
    
#### 3 

arr = []
s is string
###push in stack
for i in range(len(s)):
	arr.append(s[i])
	
rev = ""
while len(arr)!= 0:
	rev += arr.pop()
	
	


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ################  Stock Span
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ###################  Minimum bracket Reversal
    
    
                

