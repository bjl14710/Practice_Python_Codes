
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
    "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

def cnter(word):
    lists = list(word)
    Rev = list(reviews)
    wrdCnt = 0
    for i  in range (0,len(Rev)): #each review
        Revw = list(Rev[i])
        for j  in range (0,len(Revw)): #each review
            if lists[0] == Revw[j]: # need to check that the rest of the word matches
                cnt = 1
                while lists[cnt] == Revw[j+cnt]:
                    tst = 1
                    #print('test')
                    cnt = cnt + 1
                    if cnt == len(lists)-1:
                        wrdCnt = wrdCnt + 1
                        break

    return wrdCnt


    
    
def main():
    #print(cnter("anacell")) # counts the occurances

    ordd = [None]*len(list(keywords))
    words = list(keywords)
    for i in range (0,len(list(keywords))):
        ordd[i] = cnter(words[i]) #ordd[0] corresponds to anacell
    hld = 0
    cnt = 0
    
        
    ordd.sort()
    cnt = 0
    order = [None] * k
    for j in range (len(ordd) - k, len(ordd)):
        order[cnt] = ordd[j]
        cnt = cnt + 1
    
    print(order)
    
    
    

if __name__ == '__main__':
    main()
