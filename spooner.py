import sys


with open('/usr/share/dict/words') as fp:
    words = set(line.strip() for line in fp.readlines() if line.islower() and len(line.strip()) > 3)


def splitter(word):
    if word[:2] == 'qu': return 2
    vowelpos = [char in "aeiouy" for char in word].index(True)
    if not vowelpos:
        if not any(char in "aeiouy" for char in word[1:]): return 0
        vowelpos = [char in "aeiouy" for char in word[1:]].index(True)

    return vowelpos


def generate(word):
    if not any(char in "aeiou" for char in word): return []

    wordsplit = splitter(word)
    if not wordsplit: return []

    if word[wordsplit:] == inputword[inputwordsplit:]: return []
    if word[:wordsplit] == inputword[:inputwordsplit]: return []

    spoon_1 = '%s%s' % (word[:wordsplit], inputword[inputwordsplit:])
    spoon_2 = '%s%s' % (inputword[:inputwordsplit], word[wordsplit:])

    return [spoon_1, spoon_2]


def spoonit(word):
    spoonset = generate(word)

    if not spoonset: return False
    if spoonset[0] not in words: return False
    if spoonset[1] not in words: return False

    return '%s %s' % (spoonset[0], spoonset[1])


if len(sys.argv) < 2:
    print 'Spooner what?'
    sys.exit()

inputword = sys.argv[1]
inputwordsplit = splitter(inputword) 

spoons = [spoonit(w) for w in words]

view = [x for x in spoons if x]

print '\n'.join(view)
