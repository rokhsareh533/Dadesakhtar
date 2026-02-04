class node:
    def__init__(self,d):
      self.data = d 
      self.next = node
    
class node :
   def__init__(self,x):
      self.data = x
      self.next = None 
      self.back = None
   
   class dinked_list():
      def__init__(self):
         self.head = None 
      def Del_first(self):
         if self.head is None :
            print("errore")
         else :
            c = self.head
             self.head = c.next
            del c
            if self.head :
               self.head.back = None
    def dell_last(self) :
      if self.head is None :
         print("error D") 
         return
      if self.head.next is None :
         self_Del_first()
         return
      c = self.head
      while c.next.next :
            c = c.next
      Del c.next
      c.next = None

    def Dell_after(self,x) :
       if self.head is None :
          print("errore") 
          return
       c = self.head
       while c :
          if c.Data == x :
             if c.next :
                a = c.next
                c.next = a.next 
                if c.next :
                   c.next.back = c
                   del a
                   return
                print("x is last")
                return
             c = c.next
             print("not found")
                      
    def Dell_befor(self,x) :
      if self.head is None :
         print('errore')
         return
      if self.head.Data == x:
         print("errore1")
         return
      c = self.head
      while c :
         if c.data == x :
            a = c.back
            c.back = a.back
            if c.back :
               a.back.next = c
            else :
               self.head = c 
             dell a 
            return
        c = c.next
      print('not found')     
      

    def del_x(self,x) :
      if self.head is None :
         print('errore')
         return
      if self.head.data == x :
         self.Dell.first()
         return
      c = self.head
      while c :
         if c.Data == x :
            if c.next is None :
               self.del.last()
                 return
            c.back.next = c.next
            c.next.back = c.back
            del c
            return
         c = c.next
         print('not found')

    def Del_all(self) :
      while.self.head :
         self.del.first()

    def ins_fist(self,x):
      if self.head is None :
         self.head = dnode(x)
         return
      a = dnode(x)
      a.next = self.head
      self.head back = a
      self.head = a

def inst_last(self,x) ;
   if self.head is None :
      self.head = dnode(x)
      return
   c = self.head
   while c.next :
      c = c.next
    a = dnode(x)
    c.next = a
    a.back = c 

def ins_after(self,x,y):
   if self.head is None :
      print('errore')
      return
   c = self.head
   while c :
      if c.data == x :
         if c.next is None :
            self ins-inst_last(y)
            return
         a = dnode(y)
         a.next = c.next
         c.next = aa.next.back = a
         a.back = c 
         return
      c = c.next 
    print('not found')
   
def ins_before(self,x,y):
   if self.head is None :
      print('errore') 
      return
    c = self.head
    while c :
       if c.data == x :
          if c.back is None :
             self.ins_first(y)
             return
          a = dnode(y) 
          a.next = c
          a.back.next = a
          c.back = a 
          return
       c = c.next
       print('not found')
       


   

    