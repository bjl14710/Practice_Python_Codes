
array = [1,1,2,45,46,46]
tar = 47
def twoSum(arr, target):
    cnt = 0
    #k = 0 # to keep track of the number being compared
    k = 0
    arr.sort()
    used = 0 * len(arr)
    while k < len(arr)-1:
        if arr[k] == arr[k-1]:
            k = k + 1 #ignore the next numbers
            #print('true')
            #print(arr[k])
            #print(arr[k-1])
        for i in range (k,len(arr)):
            if arr[k] + arr[i] == target:
                if arr[i] != arr[i-1]:
                    cnt = cnt + 1
                #cnt = cnt + 1
                #print(cnt)
                #print(arr[k])
                #print(arr[i])
            if i == len(arr)-1: # if we went through all the members, change the targeted comparator
                k = k + 1
                
    return cnt

def main():
    #twoSum(array,tar)
    print(twoSum(array, tar))

    
if __name__ == '__main__':
    main()
