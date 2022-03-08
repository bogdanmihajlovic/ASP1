def menu():
    print("      MENU  \n"
          "1. unos kvadrata\n"
          "2. karakteristicna suma\n"
          "3. magicni kvadrati\n"
          "4. savrseni kvadrati\n"
          "5. prikaz stabla (postorder)\n"
          "6. prikaz stabla po nivoima\n"
          "7. izlaz\n")
    try:
        n = int(input("Unesite opciju: "))
        return n
    except ValueError:

        return False

def printMatrix(matrix):
    for row in matrix:
        for elem in row:
            print('{:2d}'.format(elem),end = ' ')
        print()
    print()

def inMatrix():
    n = int(input("Uneti dimenzije kvadrata: "))
    print("Unesite pocetno stanje magicnog kvadrata: ")

    return [[int(elem) for elem in input().split()] for i in range(n)]

def checkCentar(matrix):
    if matrix[1][1] != 0:
        return True
    else:
        return False

def magicSum(array,n):
    return int(sum(array)/n)

def calCentar(array,n):
    #n = 3
    return int(magicSum(array,n)/n)

def makeArray(matrix,array):
    #formita listu brojeva
    new = []
    for row in matrix:
        for temp in row:
            if temp != 0:
                new.append(temp)
    for el in array:
        new.append(el)
    new.sort()
    return new

def devil(matrix):

    magicS = magicSum(makeArray(matrix,[]),len(matrix))
    n = len(matrix)

    for i in range(n):
        temp = 0
        k = i
        l = 0
        while(k >= 0 and l < n):
            temp += matrix[k][l]
            k -= 1
            l += 1
        k = n - 1
        l = i+1
        while(k >= 0 and l < n):
            temp += matrix[k][l]
            k -= 1
            l += 1
        if temp != magicS:
            return False

    for i in range(n-1,-1,-1):
        temp = 0
        k = 0
        l = i
        while(k < n and l < n):
            temp += matrix[k][l]
            k += 1
            l += 1
        k = n - i
        l = 0
        while(k < n and l < n):
            temp += matrix[k][l]
            k += 1
            l += 1
        if temp != magicS:
            return False

    return True

def checkIfMagic(matrix):
    #provera da li je kvadrat magican
    if len(matrix) == 2:
        return False
    temp = makeArray(matrix,[])
    s = magicSum(temp,len(matrix))
    for row in matrix:
        if 0 in row:
            return False
    for row in matrix:
        if sum(row) != s:
            return False
    for i in range(len(matrix)):
        if sum([matrix[i][j] for j in range(len(matrix))]) != s:
            return False
    if sum([matrix[i][i] for i in range(len(matrix))]) != s:
        return False

    if sum([matrix[i][len(matrix) - i -1] for i in range(len(matrix))]) != s:
        return False

    return True

def chechSum(matrix,arr):
    temp = magicSum(makeArray(matrix,arr),len(matrix))
    array = []
    #provera da li je neka suma nedozvoljena

    #provera kolone
    for row in matrix:
        if sum(row) > temp:
            return True
    #provera vrste
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            array.append(matrix[j][i])
        if sum(array) > temp:
            return True
        array.clear()

    #provera glavne dijagonale
    for i in range(len(matrix)):
        array.append(matrix[i][i])
    if sum(array) > temp:
        return True
    array.clear()
    for i in range((len(matrix)-1),-1):
        array.append(matrix[i][len(matrix) - 1 - i])
    if sum(array) > temp:
        return True

    return False

def findFirstFree(matrix):
    #pronalazak prvog praznog polja
    x = -1
    y = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                x = i
                y = j
                return x,y
    return x,y

def checkIsFull(matrix):
    #provera da li je u nekoj
    #vrsti koloni ili dijagonali n-1 elemenata

    temp = []
    for i in range(len(matrix)):
        temp = [el for el in matrix[i] if el != 0]
        if len(temp) + 1 == len(matrix):
            for j in range(len(matrix)):
                if matrix[i][j] == 0:
                    return i,j,sum(temp)
    temp.clear()
    for i in range(len(matrix)):
        temp = [matrix[j][i] for j in range(len(matrix)) if matrix[j][i] != 0]
        if len(temp) + 1 == len(matrix):
            for j in range(len(matrix)):
                if matrix[j][i] == 0:
                    return j,i,sum(temp)
    temp.clear()
    for i in range(len(matrix)):
        if matrix[i][i] != 0:temp.append(matrix[i][i])
    if len(temp) + 1 == len(matrix):
        for i in range(len(matrix)):
               if matrix[i][i] == 0:
                   return i,i,sum(temp)
    temp.clear()
    for i in range(len(matrix)):
        if matrix[i][len(matrix) - 1 - i] != 0:
            temp.append(matrix[i][len(matrix) - 1 - i])
    if len(temp) + 1 == len(matrix):
        for i in range(len(matrix)):
            if matrix[i][len(matrix) - 1 - i] == 0:
                return i, len(matrix) - 1 - i,sum(temp)
    return False

def checkProgres(matrix,arr):
    if matrix == None:
        print("Nije unet kvadrat")
        return None

    if chechSum(matrix,arr) or len(matrix) == 2:
        print("Nije moguce napraviti magican kvadrat")
        return False
    temp = makeArray(matrix,arr)
    dif = temp[1] - temp[0]
    for i in range(3,len(temp)):
        if temp[i] - temp[i-1] != dif:
            print("Nije moguce napraviti magican kvadrat")
            return False
    if magicSum(temp,len(matrix)) * len(matrix) != sum(temp):
        print("Nije moguce napraviti magican kvadrat")
        return False

    return True

class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self,bottom = None,top = None):
        self.bottom = bottom
        self.top = top

    def push(self,data):
        new = Node(data)
        if self.bottom is None:
            self.bottom = new
            self.top = self.bottom
            return
        elif self.bottom == self.top:
            self.bottom.next = self.top
            self.top.next = new
            self.top = new
            return
        self.top.next = new
        self.top  = new
        return

    def isEmpty(self):
        if self.bottom is None:
            return True
        else:
            return False

    def pop(self):
        temp = self.bottom
        q = self.top

        if self.bottom == self.top:
            self.bottom = None
            self.top = None
            return q
        while temp.next is not self.top:
            temp = temp.next
        self.top = temp
        self.top.next = None
        return q

class Queue:
    def __init__(self,rear= None):
        self.rear = rear

    def is_empty(self):
        return self.rear is None

    def push(self,node):
        if self.is_empty():
            self.rear = Node(node)
            self.rear.next = None
            return
        q = self.rear
        while q.next is not None:
            q = q.next
        q.next = Node(node)
        return

    def pop(self):
        if not self.is_empty():
            q = self.rear
            self.rear = self.rear.next
            return q.data

class NodeTree:
    def __init__(self,state = None):
        self.state = state
        self.parent = None
        self.children = []
        self.numbers = []

    def makeChild(self,newNum,x,y):
        new = NodeTree() #novi cvor za stablo
        new.state = [[el for el in row] for row in self.state] #uzme stanje od svog oca
        new.numbers = [el for el in self.numbers] #uzme odgovaraju brojeve od svog oca
        new.state[x][y] = newNum #stavlja odgovarajuci broj na odgovarajuce mesto
        if newNum in new.numbers :
            new.numbers.remove(newNum)
        else:
            print("Greska pri unosu")
            return False
        if chechSum(new.state,new.numbers):
           return False
        new.parent = self
        self.children.append(new)

class Tree:
    def __init__(self,root = None):
        self.root = root

    def setRoot(self):
        root = NodeTree() #pravi koren stabla
        self.root = root
        self.root.state = inMatrix()
        print("Unesite skup brojeva")
        self.root.numbers = [int(i) for i in input().split()]
        self.root.numbers.sort()

    def makeChildrenRoot(self):
        if not checkCentar(self.root.state) and len(self.root.state) == 3:
            centar = calCentar(makeArray(self.root.state,self.root.numbers),len(self.root.state))
            self.root.makeChild(centar,1,1)
            return
        #provera jel moze da se dopuni
        t = checkIsFull(self.root.state)
        if t:
            x,y,num= t[0],t[1],magicSum(makeArray(self.root.state,self.root.numbers),len(self.root.state))-t[2]
            self.root.makeChild(num,x,y)
        else:
            x,y = findFirstFree(self.root.state)
            for num in self.root.numbers:
                self.root.makeChild(num,x,y)

    def treeMake(self):
        q = Queue()
        if self.root is None:
            self.setRoot()

        #provere da li je moguce napraviti magican kvadrat
        if checkProgres(self.root.state,self.root.numbers) is False:
            self.root = None
            return False
        nums = makeArray(self.root.state,self.root.numbers)

        if len(self.root.state) == 3 and self.root.state[1][1] != 0 and calCentar(nums, 3) != tree.root.state[1][1]:
                print("Nije moguce napraviti magican kvadrat")
                return False

        self.makeChildrenRoot()
        for child in self.root.children:
            q.push(child)

        while not q.is_empty():
            node = q.pop()
            # provera jel moze da se dopuni
            t = checkIsFull(node.state)
            if t:
                x, y, num = t[0], t[1], magicSum(nums, len(node.state)) - t[2]
                if num <= max(nums) and num != 0 and (num in node.numbers):
                    node.makeChild(num, x, y)
            else:
                x,y = findFirstFree(node.state)
                for num in node.numbers:
                    node.makeChild(num,x,y)

            for child in node.children:
                q.push(child)

    def printMagic(self):
        print("Magicni su: ")
        print()
        q = Queue()
        q.push(self.root)
        while not q.is_empty():
            node = q.pop()
            if checkIfMagic(node.state):
                printMatrix(node.state)
                if devil(node.state):
                    print("Savrsen je")
            for child in node.children:
                q.push(child)

    def printDevil(self):
        if len(self.root.state) < 4:
            print("Nema savrsenih kvadrata")
            return
        print("Savrseni su: ")
        print()
        q = Queue()
        q.push(self.root)
        pr = False
        while not q.is_empty():
            node = q.pop()
            if devil(node.state):
                printMatrix(node.state)
                pr = True
            for child in node.children:
                q.push(child)
        if pr is False:
            print("Nema savrsenih kvadrata")

    def _makeLevels(self):
        levels = []
        q = [self.root]
        while q:
            temp1 = []
            temp2 = []
            for nodeTree in q:
                temp1.append(nodeTree.state)
                for child in nodeTree.children:
                    temp2.append(child)
            levels.append(temp1)
            q = [nodeTree for nodeTree in temp2]
        return levels

    def levelsPrint(self):
        levels = self._makeLevels()
        for l,level in enumerate(levels):
            print('Nivo {}, broj cvorova {}'.format(l,len(level)) )
            for i in range(len(level[0])):
                for j in range(len(level)):
                    for el in level[j][i]:
                        print("{:2d}".format(el),end = ' ')
                    print("   ",end = ' ')
                print()
            print()

    def postorder(self):
        temp = Stack()
        nodes = Stack()
        temp.push(self.root)
        while not temp.isEmpty():
            node = temp.pop()
            nodes.push(node.data.state)
            for child in node.data.children:
                temp.push(child)
        while not nodes.isEmpty():
            matrix = nodes.pop()
            matrix = matrix.data
            printMatrix(matrix)

tree = Tree()
while True:

    n = menu()
    try:
        if n == 1:
            tree = Tree()
            tree.treeMake()
        elif n == 2:
            if tree.root is None:
                print("Nije unet kvadrat")
                print()
                continue
            print('Karakteristicna suma je:',magicSum(makeArray(tree.root.state,tree.root.numbers),len(tree.root.state)))
        elif n == 3:
            if tree.root is None:
                print("Nije unet kvadrat")
                continue
            tree.printMagic()
        elif n == 4:
            if tree.root is None:
                print("Nije unet kvadrat")
                continue
            tree.printDevil()
        elif n == 5:
            if tree.root is None:
                print("Nije unet kvadrat")
                continue
            tree.postorder()
        elif n == 6:
            if tree.root is None:
                print("Nije unet kvadrat")
                continue
            tree.levelsPrint()
        elif n == 7:
            break
        else:
            print("Pogresno uneta opcija")
            continue
    except ValueError:
        print("Pogresan unos")
        continue
    except IndexError:
        print("Pogresan unos")
        continue


    '''
0 0 0
0 5 0
0 0 0

1 2 3 4 6 7 8 9

0 0 0
0 0 0
0 0 1

0 0 1
0 5 0
7 0 0

1 2 3
0 0 0
7 8 9

2 0 0
0 5 0
0 0 0

1 3 4 6 7 8 9

1 9 0 
7 5 0 
6 1 8 

1 14 4 15
0 0 0 0
0 0 0 0
0 0 0 0

2 3 5 6 7 8 9 10 11 12 13 16


15 0 0 24 0
16 0 0 5 23
0 20 13 0 0
0 0 19 0 10
0 0 0 0 0

1 2 3 4 6 7 8 9 11 12 14 17 18 21 22 25
    '''