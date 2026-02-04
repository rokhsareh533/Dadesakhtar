class stack :
    def__init__(self,limit = 1000)
       self.st = []
       self.lim = limit
    def push(self,x):
        if len(self.st) >= self.limit :
            print ("stack is full")
            return
        self.st.append(x)
    def pop(self):
        if len(self.st) == 0 :
            print ("stack is empty")
            return -1
        return self.st.pop()
    def peek (self):
        if len(self.st) == 0 :
            print ("stack is empty")
            return _1
        return self.st[_1]
    def find(self,x):
        for i in range(len(self.st)):
            if self.st[i] == x :
              print(i)
    def find1(self,x):
        for i in range(len(self.st)):
            if self.st[i] == x :
               print(i)
               return
    def find2(self,x):
        for i in range(len(self.st)_1,_1,_1):
            if self.st[i] == x :
                print(i)  
                return
    def find2_n(self,x):
        for i in range(len(self.st)):
            if self.st[i] == x :
                p = i
                print(p)
    def replace(self,x):
        for i in range(len(self.st)):
            if self.st[i] == x :
                self.st[i] = y 
                return        