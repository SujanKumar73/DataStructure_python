class Slist:
    class _Node:
        def __init__(self,element):
            self.data=element
            self.next=None

    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def is_empty(self):
        return self.count==0

    def length(self):
        return self.count

    def first(self):
        if not self.is_empty():
            return self.head.data

    def last(self):
        if not self.is_empty():
            return self.tail.data

    def add_first(self,val):
        new_node=self._Node(val)
        if not self.is_empty():
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=self.tail=new_node
        self.count+=1

    def add_tail(self,val):
        new_node=self.Node(val)
        if not self.is_empty():
            self.tail.next=new_node
            self.tail=new_node
        else:
            self.tail=new_node
        self.count+=1

    def del_first(self):
        if not self.is_empty():
            data=self.head.data
            self.head=head.next
            if self.head is None:
                self.tail=None
            self.count-=1
            return data

    def del_last(self):
        if not self.is_empty():
            data=self.tail.data
            if self.count==1:
                self.head=self.tail=None
            else:
                last=self.tail
                cur=self.head
                while cur.next is not last:
                    cur=cur.next
                self.tail=cur
                self.tail.next=None
            self.count-=1
            return data

    def is_member(self,key):
        if not self.is_empty():
            cur=self.head
            while cur is not None:
                if cur.data==key:
                    break
                else:
                    cur=cur.next
            return cur!=None
        
            
