def patternToNumber(pattern):
    num = 0
    k = len(pattern) - 1
    gene_dict = {"A":0, "C":1, "G":2, "T":3}
    for i in pattern:
        num += gene_dict[i] * pow(4, k)
        k -= 1
    return num

def numberToPattern(index, k):
    gene_dict_reverse = {0:"A", 1:"C", 2:"G", 3:"T"}
    p = ""
    q = 0
    k = k - 1
    
    while k >=0:
        q = int(index/pow(4, k))
        p = p + gene_dict_reverse[q]
        index = index - q * pow(4, k)
        k = k - 1
    return p

def computeFrequency(text, k):
    indexDB = []
    frequentArray = [0]*pow(4,k)
    for i in range(0, len(text)-k+1):
        pattern = text[i:i+k]
        indexDB.append(patternToNumber(pattern))
    #print("indexDB={}".format(indexDB))
    for i in indexDB:
        frequentArray[i] += 1
   
    
    
    return frequentArray


def betterClumpFinding(genome, k, L, t):
# initialize
    freqDB = [0]*pow(4, k)
    clump = [0]*pow(4, k)
    frequentPattern = set()
    firstPattern = ""
    
    freqDB = computeFrequency(genome[0:L], k)

    #print("freqDB={}".format(freqDB))
# create the clump array for frequency greater than t times
    for i in range(0, pow(4, k)):
        if freqDB[i] >= t:
            clump[i] = 1
            #print("Found {}".format(i))
# update frequencyDB
    # sliding and looping
    for i in range(1, len(genome)-L+1):
        firstPattern = genome[i-1:i-1+k]
        #print("i={} firstPattern[{}:{}]={}".format(i, i-1, i-1+k, genome[i-1:i-1+k]))
    # first Pattern decrease frequency by one
        index = patternToNumber(firstPattern)
        #print("i={} index = {} firstPattern[{}:{}]={}".format(i, index, i-1, i-1+k, genome[i-1:i-1+k]))
        freqDB[index] -= 1
        if freqDB[index] >=t:
            clump[index] = 1
    # last Pattern increase frequency by one
        lastPattern = genome[i+L-k: i+L]
        index = patternToNumber(lastPattern)
        freqDB[index] += 1
    # update the clump array
        if freqDB[index] >= t:
            clump[index] = 1
            #print("Found {}".format(i))
# iterate all pattern frequency greater than t times and add them into frequentPattern set
    for i in range(0, pow(4,k)):
        if clump[i] == 1:
            frequentPattern.add(numberToPattern(i,k))
            #print("clump {} == 1, add {} to frequentPattern".format(i, numberToPattern(i,k)))

    return frequentPattern


import sys
fd = open("./datasets/E_coli.txt")
data = fd.readlines()
fd.close()
genome=""
genome=data[0]
k=9
L=500
t=3
result = set()
result = betterClumpFinding(genome, k, L, t)
print(len(result))

