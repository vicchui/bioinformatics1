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
    #stop = len(Text)-k + 1
    for i in range(0, len(Text)-k):
        p = Text[i:i+k]
        #print(len(p))
        #print("ComputingFrequencies: length of p is {} .p is {}".format(len(p), p))
    # transform pattern to index num
        n = PatternToNumber(p)
        #print("ComputingFrequencies: length of p is {} .p is {}, index number is {}".format(len(p), p, n))
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