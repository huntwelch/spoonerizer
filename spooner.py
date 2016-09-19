import sys

if len(sys.argv) < 2:
    print 'Spooner what?'
    sys.exit()

with open('/usr/share/dict/words') as fp:
    words = set(line.strip() for line in fp.readlines() if line.islower())

def isvowel(char):
    return True if "aeiouy".count(char) >= 1 else False

inputword = sys.argv[1]
inputwordsplit = [isvowel(char) for char in inputword].index(True)
if inputword[:2] == 'qu':
    inputwordsplit = 2

def generate(word):

    if len(word) < 3: return False

    wordsplit = [isvowel(char) for char in word]

    if True not in wordsplit: return False

    wordsplit = wordsplit.index(True)

    if word[:2] == 'qu':
        wordsplit = 2

    if word[wordsplit:] == inputword[inputwordsplit:]: return False
    if word[:wordsplit] == inputword[:inputwordsplit]: return False

    spoon_1 = ''.join([word[:wordsplit], inputword[inputwordsplit:]])
    spoon_2 = ''.join([inputword[:inputwordsplit], word[wordsplit:]])
    return [spoon_1, spoon_2]

def spoonit(word):
    spoonset = generate(word)
    if not spoonset: return False
    if spoonset[0] not in words: return False
    if spoonset[1] not in words: return False
    return ' '.join([spoonset[0], spoonset[1]])

spoons = [spoonit(w) for w in words]

view = [x for x in spoons if x]

print '\n'.join(view)
