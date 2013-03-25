import random

class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE / 3
    
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        
        for i in range(numVowels, self.HAND_SIZE):    
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            
    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = self.hand.keys()
        hand_keys.sort()
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        stillPossible = True

        mWord = list(str(self))

        for l in word:
            if l in mWord:
                mWord.remove(l)
            else:
                stillPossible = False
                break
        if stillPossible:
            self.hand = {}
            for char in mWord:
                self.hand[char] = self.hand.get(char, 0) + 1

        return stillPossible


'''
myHand = Hand(7)
print myHand
print myHand.calculateLen()

print(myHand.update('za'))
print myHand
print myHand.calculateLen()

myHand.setDummyHand('aazzmsp')
print myHand
print myHand.calculateLen()

print(myHand.update('za'))
print myHand
print myHand.calculateLen()

myHand.setDummyHand('juhysca')
print myHand
print myHand.calculateLen()

print(myHand.update('yycsa'))
print myHand
print myHand.calculateLen()

print(myHand.update('ycsa'))
print myHand
print myHand.calculateLen()


myHand = Hand(7)
print myHand.hand
print myHand.calculateLen()
myHand.hand = {'b': 0, 'i': 1, 'm': 1, 'o': 1, 'q': 2, 'w': 1}
print myHand.hand
print myHand.calculateLen()
'''


def getPrimes():
    for p in genPrimes():
        print p


def genPrimes():
    import itertools

    def isPrime(number):
        if number == 1: return False
        if number % 2 == 0 and number != 2:
            return False
        else:
            for div in range(2, int(number**0.5)+1):
                if number % div == 0:
                    return False
        return True

    for num in itertools.count():
        if isPrime(num):
            yield num

"""
g = genPrimes()
print(g.next())
print(g.next())
print(g.next())
print(g.next())
print(g.next())
print(g.next())
print(g.next())
print(g.next())
print(g.next())
#getPrimes()
"""

class hashSet(object):
    def __init__(self, numBuckets):
        # numBuckets: int. The number of buckets this hash set will have.
        # Raises ValueError if this value is not an integer, or if it is not greater than zero.
        # Sets up an empty hash set with numBuckets number of buckets.
        if type(numBuckets) != int or numBuckets < 1: raise ValueError
        self.BUCKETS = numBuckets

        # create empty hashSet with numBuckets number of buckets
        self.createHashSet()

    def createHashSet(self):
        # initiates empty set
        self.hSet = {}

        for i in range(self.BUCKETS):
            self.hSet[i] = []

    def hashValue(self, e):
        # INPUT as e: an integer; else Raises ValueError.
        if type(e) != int: raise ValueError
        # RETURN hValue; key of hashSet.
        hValue = e % self.BUCKETS
        if hValue < 0:
            hValue = self.BUCKETS + e
        return hValue

    def getValueList(self):
        # (re-)creates empty list
        self.ValueList = []

        # gets all lists in Set
        for lsts in self.hSet.values():
            # gets all elements in each list
            for elem in lsts:
                self.ValueList.append(elem)

    def member(self, e):
        # INPUT as e: an integer; else Raises ValueError
        # RETURN bool: True if e is in hashSet; else False
        if type(e) != int: raise ValueError
        self.getValueList()

        if e in self.ValueList:
            return True
        else:
            return False

    def insert(self, e):
        # INPUT as e: an integer; else Raises ValueError
        # puts e into appropriate bucket
        if type(e) != int: raise ValueError

        hV = self.hashValue(e)
        bucketContents = self.hSet[hV]
        bucketContents.append(e)
        self.hSet[hV] = bucketContents

    def remove(self, e):
        # INPUT as e: an integer; else Raises ValueError
        # Removes e from self
        self.getValueList()
        if type(e) != int or e not in self.ValueList:
            raise ValueError
        hV = self.hashValue(e)
        self.hSet[hV].remove(e)

    def getNumBuckets(self):
        return self.BUCKETS

    def __str__(self):
        return str(self.hSet)


"""
#mySet = hashSet(5)
#mySet = hashSet('a') # ValueError
#mySet = hashSet(0) # ValueError
#print(mySet.hSet)
#hs1 = hashSet(30)
#hs2 = hashSet(1)
""""""
#print(hs1.getNumBuckets())
#print(hs2.getNumBuckets())
#print(hs3.getNumBuckets())
""""""
print hs1.hashValue(14)
#print hs2.hashValue(14)
print hs1.hashValue(30)
#print hs2.hashValue(30)
print hs1.hashValue(-48)
#print hs2.hashValue(-48)
print hs1.hashValue(-63)
#print hs2.hashValue(-63)
""""""
hs1 = hashSet(11)
hs2 = hashSet(108)
hs1.insert(2)
hs2.insert(2)
print hs1.member(2)
print hs2.member(2)
print hs1.member(85)
print hs2.member(85)
hs1.remove(2)
hs2.remove(2)
print hs1.member(2)
print hs2.member(2)
#hs1.remove(85) # ValueError
#hs2.remove(85) # ValueError
hs1.insert(-41)
hs2.insert(-41)
print hs1.member(-41)
print hs2.member(-41)
print hs1.member(-96)
print hs2.member(-96)
hs1.remove(-41)
hs2.remove(-41)
print hs1.member(-41)
print hs2.member(-41)
#hs1.remove(-96) # ValueError
print hs1.hSet
print hs1
"""

