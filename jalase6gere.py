class nod :
    def__init__(self,data) :
         self.Data = data 
         self.next = None
    
class liked _list :
    def__init__(self) :
        self.head = None
    def insert (self,x) :
        if self.head is None :
            a = node(x)
            self head = a
        else :
            a = node(x)
            c = self.head
            while c.next :
                c = c.next
            c.next = a

    def insert_first(self,x) :
        if self.head is none :
           self.head == node(x) 
        else :
            a = node (x) 
            a . next = self.head
            self.head = a 

    def insert_last(self,x) :
        if self.head in None :
            self.head = node (x)  
        else :
            a = node (x)         
            c = self.head
            while c.next :
                c = c.next
            c.next = a 

    def insert_after(self,x=y) :
        if self.head is None :
            print('list is empty')    
            return 
        c = self.head
        while c :
            if c.Data == x :
                a = node (y)
                a.next = a
                c = c.next
             print('not found')  



     def insert_after(self,x=y) :
        if self.head is None :
            print('list is empty')    
            return 
        c = self.head
        flog.true
        while c :
            if c.Data == x :
                a = node (y)
                a.next = c.next
                c.next = a 
                flag = False
                c = c.next
               c = c.next
            if flag :
               print('not found')      

    def insert_befor(self,x,y) :
        if self.head is None :
            print('list is empty')
            return
        if self.head Data == x :
           self.insert.first(y)
           return
        c = self.head
        while c.next :
            if c.next data == x :
                a = node (y) 
                a.next = c.next
                c.next = a
                return
            c.next
        print ('not found')                 