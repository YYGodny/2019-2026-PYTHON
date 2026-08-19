def shiftLinkedList(head, k):
    move = len(head) - k
    n = []
    n2 = []
    for index, item in enumerate(head):
        if index <= move - 1:
                n.append(item)
        else:
                n2.append(item)
    for i in n: n2.append(i)
    print(n2)
