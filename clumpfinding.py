def NumberToPattern(num, k):
    g_dict = { 0:"A",1:"C",2:"G",3:"T"}
    #"g_dict[1]={}".format(g_dict[1])
    #print('NumberToPattern: number={}'.format(num))
    pattern = ""
    for j in range (k-1,-1,-1):
        #print('NumberToPattern: j={}'.format(j))
        w = int(num / pow(4,j))
        num = num - w*pow(4, j)
        pattern = pattern + g_dict[w]
    return pattern

def ComputingFrequencies(Text, k):

    #print ('Text is ' + Text)
    # initialize frequencyArray
    FrequencyArray = [0]*pow(4,k)
    # compile patterns
    #print("ComputingFrequencies: Text={}".format(Text))
    #stop = len(Text)-k + 1
    for i in range(0, len(Text)-k):
        p = Text[i:i+k]
        #print(len(p))
    #    print("ComputingFrequencies: length of p is {} .p is {}".format(len(p), p))
    # transform pattern to index num
        n = PatternToNumber(p)
    #    print("ComputingFrequencies: length of p is {} .p is {}, index number is {}".format(len(p), p, n))
    # add count in frequencyArray
        FrequencyArray[n] = FrequencyArray[n]+1
    #print("ComputingFrequencies:   FrequencyArray={}".format(FrequencyArray))
    
    return FrequencyArray

def PatternToNumber(pattern):
    num = 0
    #gene_dict={"a":0, "c":1, "g":2, "t":3,"A":0,"C":1,"G":2, "T":3}
    gene_dict={"A":0,"C":1,"G":2, "T":3}

    #print("PatternToNumber: pattern={}".format(pattern))
    k = len(pattern)-1
    for i in pattern:
        num = num + gene_dict[i]*pow(4,k)
        k = k - 1
    #print(num)
    return num



def ClumpFinding(Genome, k, L, t):
    
    # initialize clump and frequent pattern
    FrequentPattern = set()
    #print("total_length={}".format(total_length))
    #FrequentArray=[0]*pow(4,k)
    
    Clump = [0]*pow(4,k)
    text=""
    count = 0
    # build the frequency array in sliding window in lengh L
    for i in range(0, len(Genome)-L):
        text = Genome[i:i+L]
        #print("type of text is {} text={}".format(type(text),text))
        #print('FrequentArray={}'.format(ComputingFrequency.ComputingFrequencies(text,k)))
        #FrequentArray.append(ComputingFrequency.ComputingFrequencies(text,k))
        #temp = ComputingFrequencies(text,k)
        #if i == 0:
        #print("i is {}, temp={}".format(i, temp))
        FrequentArray=[0]*pow(4,k)
        #print("ClumpFinding: count={}".format(count))
        #FrequentArray.append(ComputingFrequencies(text,k))
        FrequentArray = ComputingFrequencies(text,k)
        #print("{}: FrequentArray={}".format(count, FrequentArray))
        count = count + 1
        #FrequentArray.append(temp)
    # find out the frequently k-mers over t times and label it in clump
        for index in range(0,pow(4,k)):
            #if index == 0:
            #print("FreqentArray[{}]={}".format(index, FrequentArray[index]))
            if FrequentArray[index] >= t:
                Clump[index] = 1
                #print("Yes1")
    for i in range(0, pow(4,k)):
        if Clump[i] == 1:
            #print("Yes2")
            FrequentPattern.add(NumberToPattern(i,k))
    
    return FrequentPattern
    # pick up the pattern marked in clump and add in the frequent pattern set


fd = open('./datasets/Vibrio_cholerae.txt')
data = fd.readlines()
fd.close()
#print(data)
Text=str(data[0])
Text=Text[0:-1]

result = ClumpFinding(Text, 5, 50, 4)

print(result)

