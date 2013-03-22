# -*- coding: utf-8 -*-
#recursivePower
def rp(base, exp):
    if exp == 0: return 1
    if exp > 0:
        return base * recursivePower(base, exp-1)

#recursivePowerNew
def rpn(base, exp):
    if exp == 0: return 1
    if exp > 0:
        if exp % 2 == 0:
            return  rpn(base, exp/2)* rpn(base, exp/2)
        return base * rpn(base, exp-1)
    
#Greatest common divisor
def gcd(a, b):
    gcd = 0
    for x in range(1, a):
        for y in range(1, b):
            if a % x == 0 and b % x == 0:
                ngcd = x
                if ngcd > gcd: gcd = ngcd
            if a % y == 0 and b % y == 0:
                ngcd = y
                if ngcd > gcd: gcd = ngcd
    return gcd

#rgcd
def rgcd(a, b):
    if a == b:
        return a
    if a > b:
        return rgcd(a - b, b)
    return rgcd(a, b - a)

#recur fibbi
def fib(t1, t2):
    t3 = t1 + t2
    if t2 < 1000000000:
        return fib(t2, t3)
    return t2

#Itercount
def lenIter(aStr):
    x = 0
    for c in aStr:
        x += 1
    return x
a = '#Greatest common divisor'

#recur count
def lenRecur(aStr):
    if aStr == '': return 0
    return lenRecur(aStr[1:]) + 1

#recur char finder:
def isIn(char, aStr):
    midChar = len(aStr)/2
    #print(char, aStr, midChar)
    if char == aStr: return True
    if midChar != 0:
        if char == aStr[midChar]:return True
    #if len(aStr) == 0: return False
    #if len(aStr) == 1 and char == aStr:
    #    return True
    #checks first half of aStr
    #when char < aStr[midChar] string = true:
    #           it is before the index of midChar
    #           return aStr up until midChar
    #               aStr[:midChar]
        if char < aStr[midChar]:
    #        print(char, aStr[:midChar])
            return isIn(char, aStr[:midChar])
        else: #returns false
    #        print(char, aStr[midChar:])
            return isIn(char, aStr[midChar:])
    #if char < aStr[x]:return isIn(char, aStr[:x])
    return False

#recur not-palin checker
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    #testing to see if semordnilap; Not palindromic.
    if str1 == '' and str2 == '': return True
    if str1 == '' or str2 == '': return False
    if str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    if str1[0] != str2[-1]:
        return False


def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)


def testFib(n):
    global numCalls
    numCalls = 0
    for i in range(n+1):
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')


#x = (1, 2, (3, 'John', 4), 'Hi')

#print(3 in x)
#print(x[0:1])
#print(x[0:-1])

#aTup = ('I', 'am', 'a', 'test', 'tuple')
def oddTuples(aTup):
    oTup = ()
    for i,t in enumerate(aTup):
        if (i + 1) % 2 != 0:
            oTup += (aTup[i],)
    return oTup



#x = [1, 2, [3, 'John', 4], 'Hi']
#print(3 in x)
#print(range(3))
#print(range(10,3))

#aList = range(1, 6)
#bList = aList
#aList[2] = 'hello'

#print(aList == bList)
#print(aList)

#cList = range(6, 1, -1)
#dList = []
#for num in cList:
#    dList.append(num)
#print(cList == dList)
#print(cList is dList)
#print(cList)
#listA = [100, 0, 1, 4]
#print(listA.append(7))

#listA = [100, 0, 1, 4, 7]
#listB = ['x', 'z', 't', 'q']
#listA.sort()

#print(listA)
#print(listA.insert(0, 100))
#print(listA)
#print(listA + listB)
#print(listB.sort())
#print(listB.pop())
#print(listB)
#print(listB.count('a'))
#   returns 0
#listB.remove('a') #before of no 0
#listA.extend([4, 1, 6, 3, 4])
#print(listA)
#print(listA.sort)
#print(listA.pop(4))
#print(listA)
#print(abs(-5))
testList = [1, -4, 8, -9]


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


def absOf(n):
    return abs(n)


#f = absOf
#applyToEach(testList, f)
#print(testList)
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

#print(applyEachTo([inc, square, halve, abs], -3))
#print(applyEachTo([inc, square, halve, abs], 3.0))
#print(applyEachTo([inc, max, int], -3))

#print(int(-3))

#animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
#animals['d'] = 'donkey'

#print(animals)
#print(animals['c'])
#print(animals['donkey'])
#print(animals.keys())
#del animals['b']
#print(len(animals))

#animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

#animals['d'] = ['donkey']
#animals['d'].append('dog')
#animals['d'].append('dingo')


def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    n = 0
    for l in aDict.values():
        print(l)
        for t in l:
            print(t)
            n+=1
    return n


#print(animals)
#print(howMany(animals))
#from collections import Iterable

#animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#eDict = {}
#animals['d'] = ['donkey']
#animals['d'].append('dog')
#animals['d'].append('dingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    bKeyValue = [0, 0]
    if len(aDict.keys()) == 1:
        return aDict.keys()[0]
    for key,value in aDict.iteritems():
        keyValue = 0
        for i in value:
            keyValue += 1
        if keyValue > bKeyValue[0]:
            bKeyValue = [keyValue, key]
    if bKeyValue[1] == 0:
        return None
    return bKeyValue[1]


#print(biggest({'X': []}))
#print(biggest({'X': [], 'Y': []}))
#print(biggest(animals))
#print(biggest(eDict))

