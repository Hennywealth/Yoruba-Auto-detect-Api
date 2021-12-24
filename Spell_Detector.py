

def readDictionaryfile(dictionaryFilename):
    dictionarywords = []
    inputfile = open(dictionaryFilename,"r", encoding="utf-8") 
    for line in inputfile:
        word = line
        dictionarywords.append(word.strip(".,!\":;?\n").lower())
    inputfile.close()
    return dictionarywords



def readtextfile(textfilename):
    words = []
    inputfile = open(textfilename, "r", encoding="utf-8" )
    for line in inputfile:
        Words_OnLine = line.strip().split()
        for word in Words_OnLine:
            words.append(word.strip(".,!\":;?").lower())
    inputfile.close()
    return words

 
def findErrors(dictionarywords, textwords): 
    misspelled_words = []
    for word in textwords:
        if word not in dictionarywords:
            misspelled_words.append(word) 
    return misspelled_words
 
def printErrors(errorsList):
    print('The misspelled words are:')
    for word in errorsList:
        print(word)
              

    









