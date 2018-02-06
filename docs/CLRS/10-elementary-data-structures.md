# 10 Elementary Data Structures

## 10.1 Stacks and Queues

### Stacks
Stack-Empty(S)
```
if S.top == 0
    return True
else
    return False
```

Push(S, x)
```
S.top = s.top + 1
S[S.top] = x
```

Pop(S, x)
```
if STACK-EMPTY(S):
    error "underflow"
else S.top = S.top - 1
    return S[S.top +1]
```

### Queues

Enqueue(Q, x)
```
Q[Q.tail] = x
if Q.tail == Q.length
    Q.tail = 1
else Q.tail = Q.tail + 1
```

Dequeue(Q)
```
x = Q[Q.head]
if Q.head == Q.length
    Q.head = 1
else Q.head == Q.head + 1
return x
```

### Exercises

#### 10.1-1

Using Figure 10.1 as a model, illustrate the result of each operation in the squence PUSH(S, 4), PUSH(S, 1), PUSH(S, 3), POP(S), PUSH(S, 8), and POP(S) on an initially empty stack S stored in array S[1..6].

#### 10.1-2

Explain how to implement two stacks in one array A[1..n] in such a way that neither stack overflows unlses the total number of elements in both stacks together is n. The PUSH and POP operations should run in O(1) time.

#### 10.1-3

Using Figure 10.2 as a model, illustrate the result of each operation in the sequence ENQUEUE(Q, 4), ENQUEUE(Q, 1), ENQUEUE(Q, 3), DEQUEUE(Q), ENQUEUE(Q, 4), ENQUEUE(Q, 1), ENQUEUE(Q, 3), DEQUEUE(Q), ENQUEUE(Q, 8), and DEQUEUE(Q) on an initially empty queue Q stored in array Q[1..6].

#### 10.1-4

Rewrite ENQUEUE and DEQUEUE to detect underflow and overflow of a queue.

#### 10.1-5

Whereas a stack allows insertion and deletion of elements at only one end, and a queue allows insertion at one end and deletion at the other end, a DEQUE(double-ended queue) allows inseration and deletion at both ends. Write four O(1)-time procedures to insert elements into and delete elemtns from both ends of a deque implemented by an array.

#### 10.1-5

Show how to implement a queue using two stacks. Analyze the running time of the queue operations.

#### 10.1-5

Show how to implement a stack using two queues. Analyze the running time fo the stack operations.

## 10.2 Linked List

### Common Operations

* List-Search(L, k) - Find first node in list L the holds the value.
* List-Insert(L, node) - Splice node (with set value) into head of list L.
* List-Delete(L, node) - Delete node from list L.
* List-Sort
* List-Reverse

List-Search(L, k)
```
x = L.head
while x != NIL and x.key != k
    x = x.next
return x
```

List-Insert(L, x)
```
x.next = L.head
if L.head != NIL
    L.head.prev = x
L.head = x
x.prev = NIL

```

List-Delete(L, x)
```
if x.prev != NIL
    x.prev.next = x.next
else L.head = x.next
if x.next != NIL
    x.next.prev = x.prev
```

List-Delete'(L, x)
```
x.prev.next = x.next
x.next.prev = x.prev
```

List-Search'(L, x)
```
x = L.nil.next
while x != L.nil and x.key != k
    x = x.next
return x
```

List-Insert'(L, x)
```
x.next = L.nil.next
L.nil.next.prev = x
L.nil.next = x
x.prev = L.nil
```

### Exercises

#### 10.2-1

Q: Can you implement the dynamic-set operation INSERT on a singly linked list in O(1) time? How about DELETE?

A: Yes, by inserting at the L.head. No, DELETE takes O(n) time.

#### 10.2-2

Q: Implement a stack by using a singly linked list L. The operations PUSH and POP should still take O(1) time.

A: See Stack in singly.py

#### 10.2-3

Q: Implement a queue by a singly linked list L. The operations ENQUEUE and DEQUEUE should sill take O(1) time

A: See Queue in singly.py

#### 10.2-4

Q: As written, each loop iteration in the LIST-SEARCH' procedure requries two tests: one for _x != L.nil_ and one for _x.key != k_. Show how to elminate the test for _x != L.nil_ in each iteration.

A: 

LIST-SEARCH''(L, k)
```
L.nil.key = k
x = L.nil.next
while x.key != k
    x = x.next
return x
```

#### 10.2-5

Q: Implement the dictionary operations INSERT, DELETE, and SEARCH using singly linked circular lists. What are the running times of your procedures?

#### 10.2-6

Q: The dynamic-set operation Union takes two disjoint sets S_1 and S_2 as input, and it returns a set S = S_1 U S_2, consisting of all the elements of S_1 and S_2. The sets S_1 and S_2 are usually destroyed by the operation. Show how to support UNION in O(1) time using a suitable list data structure.

#### 10.2-7

Q: Give a O(n)-time nonrecursive procedure that reverse a singly linked list of _n_ elements. The procedure should use no more than constant storage beyond that needed for the list itself.

A: See reversed method in SinglyListNode in singly.py

#### 10.2-8

Q: Explain how to implement doubly linked list s using only one pointer value _x.np_ per item instead o the usualy two (_next_ and _prev_). Assume that all pointer values can be interpreted as k-bit integers, and define _x_, _np_ to be _x.np = x.next XOR x.prev_, the k-bit "exclusive-or" of _x.next_ and _x.prev_. (The value NIL is represented by 0). Be sure to describe  what information you need to access the head of the list. Show how to implement the SEARCH, INSERT, and DELETE operations on such a list. Also show how to reverse such a list in O(1) time.
