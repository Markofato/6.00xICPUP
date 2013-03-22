__author__ = 'God'
def union(set1, set2):
    """
    set1 and set2 are collections of objects, each of which might be empty.
    Each set has no duplicates within itself, but there may be objects that
    are in both sets. Objects are assumed to be of the same type.

    This function returns one set containing all elements from
    both input sets, but with no duplicates.
    """
    if len(set1) == 0:
        return set2
    elif set1[0] in set2:
        return union(set1[1:], set2)
    else:
        return set1[0] + union(set1[1:], set2)


#print(union('',''), union('','a'), union('','ab'), union('a',''), union('a','b'),union('c','ab'), union('de',''), union('ab','c'), union('cd','ab'))
#print(union('abc',''), union('abc','a'), union('abc','ab'), union('abc','d'), union('abc', 'abcd'))
#print(union('','abc'), union('a','abc'), union('ab','abc'), union('abc','abc'))
#print(union('','abc'), union('a','abc'), union('ab','abc'), union('d','abc'))


def foo(x, a):

    """
    x: a positive integer argument
    a: a positive integer argument

    returns an integer
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

#print(foo(2, 5), foo(5, 6), foo(9, 7))
#print( foo(10, 3), foo(1, 4), foo(10, 6))
#print( foo(100, 5), foo(96, 5), foo(22, 5))


def rem(x, a):

    """
    x: an integer argument
    a: an integer argument

    returns: integer, the remainder when x is divided by a.
    """
    print(x, a)
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        print(x, a, x - a)
        return rem(x - a, a)

#print(rem(7, 5))


def program1(x):
    total = 0
    n=0
    for i in range(1000):
        total += i
        n+=1

    while x > 0:
        x -= 1
        n+=1
        total += x
        n+=1

    return total,(n + 3)

def program2(x):
    total = 0
    n=0
    for i in range(1000):
        total = i
        n+=1

    while x > 0:
        x /= 2
        n+=1
        total += x
        n+=1

    return total,(n + 3)

#print(program1(0), program1(1000))
#print(program2(0), program2(1000))

def program3(L):
    totalSum = 0
    highestFound = None
    for x in L:
        totalSum += x

    for x in L:
        if highestFound == None:
            highestFound = x
        elif x > highestFound:
            highestFound = x

    return (totalSum, highestFound)


def program1(L):
    multiples = []
    for x in L:
        for y in L:
            multiples.append(x*y)
    return multiples


