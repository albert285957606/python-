from timeit import Timer

def test1():#1.889487
    l = []
    for i in range(1000):
        l = l + [i]
    return l

def test2():#0.091561
    l = []
    for i in range(1000):
        l.append(i)
    return l

def test3():#0.038418
    l = [i for i in range(1000)]
    return l

def test4():#0.009710
    l = list(range(1000))
    return l

t1 = Timer("test1()","from __main__ import test1")
print("concat %f seconds\n"%t1.timeit(number=1000))
print(test1())
print(test2())
print(test3())
print(test4())

#test1()
#test2()
#test3()
#test4()
list().append()
list().sort()
list().clear()
list().copy()
list().count()
list().extend()
list().index()
list().insert()
list().pop()#o(n)
list().remove()
list().reverse()

#pop() 0.0007
#pop(0)  0.8

