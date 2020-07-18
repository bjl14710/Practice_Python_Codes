
#find if two hexadecimal numbers are successive in gray code or in binary

#need to convert from hex to binary

In1 = 0x88
In2 = 0x8C
def Count(hx, hx2):
    diff = 0
    list1 = list(bin(hx))
    list2 = list(bin(hx2))
    for i in range (2, len(list1)):
        if list1[i] != list2[i]:
            diff = diff + 1
        else:
            diff = diff

    if diff == 1:
        return 1
    else:
        return -1



    
def main():
    Count(In1, In2)
    print(Count(In1, In2))
#    print('test')


if __name__ == '__main__':
    main()
