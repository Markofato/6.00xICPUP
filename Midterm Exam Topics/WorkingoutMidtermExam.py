__author__ = 'God'
#while 1 != 2:
 #   x = 1.0
 #   if x/0 == TypeError:
 #       print('lol')
 #   elif x == 4:
 #       break
 #   elif x == 5:
 #       pass
#x=0
#n = -4
def upAndDown(n):
    #global x
    x+=1
    if n == 0:  return x
    if n == 1:  return x
    if n%2 == 0:
        return upAndDown( (n/2) )
    if n%2 == 1:
        return upAndDown( (n*3 + 1) )
    return "All Done", x

#print(upAndDown(n))

#stuff  = 'iPad'
#for thing in stuff:
#    if thing == 'iPad':
#        print "Found it"


def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x


#print(Square(-12))
def isMyNumber(number):
    secNum = 136
    if number < secNum:
        print('-1')
        return -1
    if number == secNum:
        print('0')
        return 0
    if number > secNum:
        print('1')
        return 1

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number.
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number

    returns: integer, the secret number
    '''
    guess = 1
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == 0:
            foundNumber = True
        elif sign == -1:
            guess *= 2
        else:
            guess -= 1
    return guess

#print(jumpAndBackpedal(isMyNumber))


def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story.
    """
    story = story.split(' ')

    def adj(word):
        if word in listOfAdjs:
            return '[ADJ]'
        return word

    def verb(word):
        if word in listOfVerbs:
            return '[VERB]'
        return word

    def noun(word):
        if word in listOfNouns:
            return '[NOUN]'
        return word

    story = [adj(word) for word in story]
    story = [verb(word) for word in story]
    story = [noun(word) for word in story]
    return ' '.join(story)

'''
story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']
print(generateForm(story, listOfAdjs, listOfNouns, listOfVerbs))
exp = 'At the [ADJ] thrift [NOUN] I [VERB] a pair of [ADJ] [NOUN] that [VERB] like [NOUN] your [NOUN] might wear'
print(generateForm(story, listOfAdjs, listOfNouns, listOfVerbs) == exp)

story = 'The ravenous zombies started attacking yesterday'
listOfAdjs = ['ravenous']
listOfNouns = ['zombies', 'humans', 'yesterday']
listOfVerbs = ['attacking', 'attacks']
print(generateForm(story, listOfAdjs, listOfNouns, listOfVerbs))
exp = 'The [ADJ] [NOUN] started [VERB] [NOUN]'
print(generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)==exp)

story = 'The ravenous zombies started attacking yesterday'
listOfAdjs = []
listOfNouns = []
listOfVerbs = []
print(generateForm(story, listOfAdjs, listOfNouns, listOfVerbs))

story = 'The period test. how does it split it?'
print(story.split())
listOfAdjs = ['ravenous']
listOfNouns = ['zombies', 'humans', 'yesterday']
listOfVerbs = []
print(generateForm(story, listOfAdjs, listOfNouns, listOfVerbs))

story = ''
listOfAdjs = ['ravenous']
listOfNouns = ['zombies', 'humans', 'yesterday']
listOfVerbs = ['attacking', 'attacks']
print(generateForm(story, listOfAdjs, listOfNouns, listOfVerbs))
'''

def generateTemplates(madLibsForm):
    """
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    AVNlist = []
    listOfWords = madLibsForm.split(' ')
    listwAdjVerbNoun = ['[ADJ]', '[VERB]', '[NOUN]']
    for word in listOfWords:
        if word in listwAdjVerbNoun:
            for wordtype in listwAdjVerbNoun:
                if word == wordtype:
                    AVNlist.append(word)

    return AVNlist


'''
one = 'At the [ADJ] thrift [NOUN] I [VERB] a pair of [ADJ] [NOUN] that [VERB] like [NOUN] your [NOUN] might wear'
two = 'The [ADJ] [NOUN] started [VERB] [NOUN]'
three = 'what if there are none of the words they are looking for'
four = ''
print(generateTemplates(one))
print(generateTemplates(two))
print(generateTemplates(three))
print(generateTemplates(four))
'''

def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    madTempList = [('[ADJ]',listOfAdjs), ('[VERB]',listOfVerbs), ('[NOUN]',listOfNouns)]
    for wType in madTempList:
        if madTemplate == wType[0]:
            if userWord in wType[1]:
                return True
            else:
                return False

'''
one = ['[ADJ]', '[NOUN]', '[VERB]', '[ADJ]', '[NOUN]', '[VERB]', '[NOUN]', '[NOUN]']
two = ['[ADJ]', '[NOUN]', '[VERB]', '[NOUN]']

listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']

print(verifyWord('creepy','[ADJ]' ,listOfAdjs, listOfNouns, listOfVerbs))
print(verifyWord('creepy','[NOUN]' ,listOfAdjs, listOfNouns, listOfVerbs))
print(verifyWord('found','[ADJ]',listOfAdjs, listOfNouns, listOfVerbs))
print(verifyWord('store','[NOUN]' ,listOfAdjs, listOfNouns, listOfVerbs))
print(verifyWord('store','[VERB]',listOfAdjs, listOfNouns, listOfVerbs))
print(verifyWord('looked','[NOUN]',listOfAdjs, listOfNouns, listOfVerbs))
print(verifyWord('found','[VERB]',listOfAdjs, listOfNouns, listOfVerbs))
print(verifyWord('found','[NOUN]' ,listOfAdjs, listOfNouns, listOfVerbs))
print(verifyWord('plaid','[VERB]',listOfAdjs, listOfNouns, listOfVerbs))
'''
def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    for c in range(0, (n/24)+1):
        for b in range(0, (n/8)+1):
            for a in range(0, (n/5)+1):
                if 5*a + 8*b + c*24 == n:
                    return True
    return False

for term in [[[numPens(n),n] for n in range(-5000,10000)]]: print(term)
for term in [[n/5, n/8, n/24, n] for n in range(0,100)]: print(term)

