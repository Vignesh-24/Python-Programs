class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkList:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root==None:
            self.root=node(data)
        else:
            temp=self.root
            while temp.next!=None:
                temp=temp.next
            temp.next=node(data)
    def show(self):
        temp=self.root
        while temp!=None:
            print(temp.data)
            temp=temp.next
    def delete(self,data):
        temp=self.root
        while temp.next.data!=data:
            temp=temp.next
        temp.next=temp.next.next

if __name__ == '__main__':
    llist=LinkList()
    llist.insert(5)
    llist.insert(12)
    llist.insert(2)
    llist.insert(25)
    llist.show()
    llist.delete(12)
    llist.show()




