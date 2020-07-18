

word1 = 'ba'
word2 = 'ab'

def roundRotate(word):
    lists = list(word)
    newWord = [None]*len(lists)  #creates a list the size we need
    newWord[0] = lists[len(lists)-1]
    for i in range (1,len(lists)):
        newWord[i] = lists[i-1]
    return newWord

def check(word, otherWord):
    if word == otherWord:
        return 1
    else:
        return -1
    

def main():
    inputWord = list(word2)
    print(check(roundRotate(word1), inputWord))
    


if __name__ == '__main__':
    main()
