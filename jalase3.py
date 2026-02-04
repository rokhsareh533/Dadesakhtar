class C_Queue () :
    def__init__(self,max = 100):
         self.list[] * max
         self.rear = -1
         self.front = -1
    def insert (self,x):
         if (self.rear+1) % len(self.list) == self.front :
              print ('Queue is full')
              return
         if self.front == -1
            self.front = 0
            self.rear = 0
            self.list[0] = x
            return
         self.rear = (self.rear +1) % len(self.list)
         self.list [self.rear] = x
    def del(self) :
        if self.front == -1 :
          print('Queue is empty') 
        if self.front   == self.rear :
           k = self.list [self.front]
           self.front = -1
           self.rear = -1
           return k
        k = self.list[self.front]
        self.front = (self.front +1) % len(self.list)
    
    def is_full(self) :
        return(self.rear+1) % len(self.list) == self.front
    def is_empty(self):
        return self.front == -1
    def show_valid(self):
        if self rear >= self.front :
           for i in range (self front , self.rear)
               print(self.list[i])
        else:
            for i in range(self front . len(self.list)):
                print (self.list[i])
            for i in range (self.rear +1) :
                print(self.list[i])   
                