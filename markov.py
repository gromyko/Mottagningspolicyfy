import random

nodelist = dict()
class node:
    
    output = str()

    def __init__(self, word):
        self.links = dict()
        self.word = word
        self.numberOfLinks = 0
        self.forwardLinks = None
        global nodelist
        nodelist[word] = self

    def incrementLink(self, word):
        if word in self.links.keys():
            self.links[word] += 1
        else:
            self.links[word] = 1
    
    def buildLinks(self):
        self.forwardLinks = dict()
        for val in self.links.values():
            self.numberOfLinks += val 
        index = 0
        for word, count in zip(self.links.keys(), self.links.values()):
            self.forwardLinks[count+index] = word
            index += count
            

    def getWord(self):
        if self.forwardLinks is None:
            self.buildLinks()
        if self.numberOfLinks:
            num = random.randrange(0, self.numberOfLinks, 1)
            for count in self.forwardLinks:
                if num <= count:
                    return self.forwardLinks[count]
        else:
            return "" 


f = open("text.txt", "r")

sample = f.read()


words = sample.split(" ")

lastWord = None

for word in words:
    if lastWord is not None:
        if lastWord in nodelist.keys():
            nodelist[lastWord].incrementLink(word)
        else:
            temp = node(lastWord)
            temp.incrementLink(word)
    lastWord = word

currentNode = random.choice(list(nodelist.values()))
res = currentNode.word
for i in range(2000):
    word = currentNode.getWord()
    if word:
        res += " " + word
        currentNode = nodelist[word]
    else:
        currentNode = random.choice(list(nodelist.values()))



f2 = open("out.txt", "w")
f2.write(res)
f2.close()
f.close()
