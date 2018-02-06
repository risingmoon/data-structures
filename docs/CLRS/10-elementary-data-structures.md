# 10 Elementary Data Structures

## 10.1 Stacks and Queues

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

Can you implement the dynamic-set operation INSERT on a singly linked list in O(1) time? How about delete?

#### 10.2-2

Implement a stack by using a singly linked list L. The operations PUSH and POP should still take O(1) time.

#### 10.2-3

Implement a queue by singly linked list L. The operations ENQUEUE and DEQUEUE should sill take O(1) time

#### 10.2-4

As written, each loop iteration in the LIST-Search' procedure requries two tests: one for x != L.nil and one for x.key != k. Show how to elminate the test for x != L.nil in each iteration.

#### 10.2-5

Implement the dictionary operations INSERT, DELETE, and SEARCH using singly linked circular lists. What are the running times of your procedures?

#### 10.2-6

The dynamic-set operation Union takes two disjoint sets S_1 and S_2 as input, and it returns a set S = S_1 U S_2, consisting of all the elements of S_1 and S_2. The sets S_1 and S_2 are usually destroyed by the operation. Show how to support UNION in O(1) time using a suitable list data structure.

#### 10.2-7

Give a O(n)-time nonrecursive procedure that reverse a singly linked list of n elements. The procedure should use no more than constant storage beyond that needed for the list itself.

#### 10.2-8

Explain how to implement doubly linked list s using only one pointer value x, np per item instead o the usualy two (next and prev). Assume that all pointer values can be interpreted as k-bit integers, and define x, np to be x.np = x.next XOR x.prev, the k-bit "exclusive-or" of x.next and x.prev. (The value NIL is represented by 0). Be sure to describe  what information you need to acess the head of hte list. Show how to implement the SEARCH INSERT, and DELTE operations on such a list. Also show how to reverse such a list in O(1) time.
