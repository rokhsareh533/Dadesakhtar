def del_first(self) :
    if self.head is None :
        print( 'list is empty')
        return 
    c = self.head
    self.head = c.next
    del c

def del_last(self) :
    if self.head is None :
        print ('list is empty')  
        return
    if self.head.next is None :
        self.Del_first() 
        return
    c = self.head
    while c.next.next :
        c = c.next
    del c.next
    c.next = None

def del_after(self,x) :
    if self.head is None :
        print('error0')
        return
    if self.head.next is None :
        print('error1')
        return
    if self.head.Data == x :
       a = self.head.next = a.next
       del a
       return
       c = c.next
       print('rrror not x')

def Del_befor(self,x) :
    if self.head is None :
        print('error0')
        return
    if self.head.next is None :
        print('error1')
        return
    if self.head.Data == x :
        print('error x1')
        return
    if self.head.next.Data == x :
        self.Del_first()
        return
    if self.head.next.next is None :
        print('error2')
        return
    c = self.head
    while c.next :
        if c.next.next.Data == x :
            a = c.next
            c.next = a.next
            del a
            return
        c = c.next
      print('error not x')  
    
def del_x(self,x) :
    if self.head is None :
        print('error0')
        return
    if self.head Data == x :
       self.Del_first()
       return
    c = self.head
    while c.next :
        if c.next.Data == x :
            a = c.next
            c.next = a next
            del a
            return
            c = c.next
            print('error not found')

def Del_all(self) :
    while self.head :
        self del_first()
        return
    
def Find(self,x) :
def Replace(self,x,y)  
