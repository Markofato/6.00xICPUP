__author__ = 'God'


def thisRaisesAZeroDivisionError():
    x = 1/0


def thisRaisesAValueError():
    y = int('Five')


def thisDoesNotRaiseAnyErrors():
    z = 'just a string'


def tryExercise():
    print 'A',
    try:
        return
        print 'B',
    except ZeroDivisionError as e:
        print 'C',
    else:
        print 'D',
    finally:
        print 'E',
    print 'F'


'''
test
'''

#tryExercise()

PATH_TO_FILE = None


def loadWords():
    inFile = open(PATH_TO_FILE, 'r', 0)
    line = inFile.readline()
    wordlist = line.split(' ')
    print "  ", len(wordlist), "words loaded."
    return wordlist


def isPrime(n):
    if type(n) != int:
        raise TypeError
    if n < 1:
        raise ValueError
    else:
        for div in range(2, int(n**0.5)+1):
            if n % div == 0:
                return False
        return True


'''
print(isPrime('hello'))
print(isPrime(0))
print(isPrime(2))
print(isPrime(8))
print(isPrime(-5))
print(isPrime(1231))
'''


class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print self.time


'''
clock = Clock('5:30')
clock.print_time()
'''


class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print time


'''
clock = Clock('5:30')
clock.print_time('10:30')
'''


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<{},{}>'.format(self.x,self.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __repr__(self):
        return 'Coordinate({}, {})'.format(self.x,self.y)


'''
#x.__repr__() <==> repr(x)

#a = Coordinate(2,2)
#b = Coordinate(2,2)
c = Coordinate(2,4)
#coords = [a,b,c]
print(c)
print(c.__repr__())
print(repr(c))
print(eval(repr(c)) == c)
'''


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        """Creates a new intSet of integers that appear in both
           self and other"""
        interSet = intSet()
        for e1 in self.vals:
            for e2 in other.vals:
                if e1 == e2:
                    interSet.insert(e1)
        return interSet

    def __len__(self):
        """Returns length of self"""
        return len(self.vals)


'''
#list1 = [1,3,8,7,6,3,4,5,7,6,4,2,1,2,4,5,3]
#list2 = [8,6,5,4,7,1,2,5,6,9,8,4,2,3,5,6,5,7]
s1 = intSet()
s2 = intSet()
s3 = intSet()
list1 = {1,3,8,7,6,3,4,5,7,6,4,2,1,2,4,5,3}
list2 = {8,6,5,4,7,1,2,5,6,9,8,4,2,3,5,6,5,7}
[s1.insert(e) for e in list1]
[s2.insert(e) for e in list2]
#s1 = list1
#s2 = list2
print(s1.vals)
print(s2.vals)
print(s1.intersect(s2))
print(s1.intersect(s3))
print(len(s1), len(s2), len(s3))
'''


class Queue(object):
    def __init__(self):
        self.vals = []

    def insert(self, elem):
        self.vals.append(elem)

    def remove(self):
        endElem = len(self.vals)
        print(endElem)
        if endElem == 0:
            raise ValueError
        else:
            return self.vals.pop(endElem-1)


'''
queue = Queue()
queue.insert(5)
queue.insert(6)
print(queue.remove())
queue.insert(7)
print(queue.remove())
print(queue.remove())
print(queue.remove())
'''


class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print self.incantation


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print spell


'''
spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())
'''


class A(object):
    def __init__(self):
        self.a = 1

    def x(self):
        print "A.x"

    def y(self):
        print "A.y"

    def z(self):
        print "A.z"


class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3

    def y(self):
        print "B.y"

    def z(self):
        print "B.z"


class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5

    def y(self):
        print "C.y"

    def z(self):
        print "C.z"


class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6

    def z(self):
        print "D.z"


'''
obj = D()
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)
obj.x()
obj.y()
obj.z()


#2
#3
#5
#6
#A.x
#C.y
#D.z

print(D.__mro__)
print(C.__mro__)
print(B.__mro__)
print(A.__mro__)

'''