class Qoueue:
    def__init__(self,max=100):
          self.list = []
          self.front = _1
          self.rear = -1
    def insert(self,x):
         if self.rear >= len self.list _1 :
        print("Qoueue is full.")
        return
if self.front == _1 :
     self.front = 0
     self.rear = 0
     self.list[0] = x
     return
    self.rear +=1
    self.list[self.rear] = x
    return
def del (self):
    if self.front == -1 :
      print('Queue is empty')
      return
    if self.front == self.rear :
        k = self list [self.front] 
        self.front = _1
        self.rear = _1
        return K
    k = self.list[self.front]
        self.front += 1
        return k
      
class C_Queue :
     def__init__(self,max):
          self.list[]
          self.front = _1
          self.max = max
    def ins (self,x) :
        if self.front == _1
           self.front = 0
           self.rear = 0
           self.list[0] = x
           return
        if (self.rear +1) % self.max == self.front :
           print ('Queue is full')
           return n
           self.rear = (self.rear +1) % self max 
           self.list [self.rear] = x
    def delete(self):
       if self.front == _1 :
            print('Queue is empty')
            return
       if self.rear == self.front :
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
            k = self.list[self.front]
            self.front += 1
            return k
    def is_emty (self):
      return self.front == -1
    def is_full(self):
       return (self.return +1) % self.max =0 self.front 
    def show_valid (self):
        if self.rear >= front :
             for i in range(self.front , self.rear +1 , 1):
                  print(self.list[i])
        else:
             for i in range (self.front , self.max , 1):
                  print (self.list[i])
            for i in range (0,self.rear+1 , 1):
                  print (self.list[i])               

     def show_valid1(self) :
         i = self.front
         print(self.list[i]) :
         while i != self.rear :
              i = (i + 1) % len (self.list)
              print (self.list[i])


     def show_invalid(self) :
        i = (self.rear +1) % len (self.list) 
        whil i != self.front :
        print (self.list[i]) 
        i = (i +1) % len(self.list)

     def Find (self,x) :
         i = self.front
         if self.list[i] == x :
               return
         while i != self.rear :
               i = (i +1) % len(self.list) 
               if self.lisr.[i] == x :
                     return i
     def i Replace (self,x,y) :
         i = self.front
         if self.list[i] == x :
            self.list[i] = y
          while i != self.reare :
                i = (i +1)  % len(self.list)
                if self.list[i] == x :
                   self.list[i] = y
      
         