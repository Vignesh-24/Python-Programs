from collections import defaultdict
class Node:
    def __init__(self):
        self.node=[None]*26
        self.end=False

class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,word):
        temp=self.root
        for each in word:
            index=ord(each)-97
            if temp.node[index]==None:
                temp.node[index]=Node()
            temp=temp.node[index]
        temp.end=True

    def search(self,word):
        temp=self.root
        for each in word:
            temp = temp.node[ord(each) - 97]
            if temp == None:
                print("Not Found")
                return
        if temp.end==True:
            print("Found String")

arr=['hello','hi','abc','hell']
trie=Trie()
for i in arr:
    trie.insert(i)
trie.search('abcd')
trie.search('bcd')
trie.search('hello')
trie.search('ludo')
trie.search('hie')










            
