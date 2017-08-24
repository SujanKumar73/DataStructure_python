import SlinkedList

s1=SlinkedList.Slist()
s1.add_first(10)
s1.add_first(20)
s1.add_first(30)

def display(head):
    temp=s1.head
    while temp!=None:
        print temp.data
        temp=temp.next

display(s1.head)

