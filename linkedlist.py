class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next: Node = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        iterator = self.head
        linkedListString = ''
        while iterator:
            linkedListString += str(iterator.data) + '->'
            iterator = iterator.next
        print(linkedListString)

    def length(self):
        len = 0
        iterator = self.head
        while iterator:
            len += 1
            iterator = iterator.next
        return len

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(data)

    def insert_values(self, values):
        for value in values:
            self.insert_at_end(value)


    def remove_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                iterator.next = iterator.next.next
            iterator = iterator.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                iterator.next = Node(data, iterator.next)
            iterator = iterator.next
            count += 1

    def index_by_value(self, value):
        count = 0
        iterator = self.head
        while iterator:
            if iterator.data == value:
                return count
            iterator = iterator.next
            count += 1
        return -1

    
    def insert_after_value(self, value, data):
        # reusing index_by_value doubles time complexity...
        index = self.index_by_value(value)
        if index < 0:
            raise Exception("Value not found")
        self.insert_at(index + 1, data)

    def remove_by_value(self, value):
        index = self.index_by_value(value)
        if index < 0:
            raise Exception("Value not found")
        self.remove_at(index)
        


if __name__ == '__main__':
    # ll = LinkedList()
    # ll.insert_at_end(12)
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    # ll.insert_at_beginning(1)
    # ll.insert_at_end(15)
    # ll.print()
    # print(ll.length())

    # print(LinkedList().length())

    ll2 = LinkedList()
    ll2.insert_values(["banana", "mango", "grapes", "orange"])
    ll2.print()
    ll2.insert_at(0, "figs")
    ll2.insert_at(3, "strawberries")
    ll2.print()

    print(ll2.index_by_value("mango"))

    ll2.insert_after_value("mango", "blackberries")
    ll2.print()

    ll2.remove_by_value("grapes")
    ll2.print()

