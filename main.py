def countSequence(arr):
    acount,gcount=0,0
    for i in arr:
        if i=='A':
            acount+=1
        if i=='G':
            gcount+=acount
    return gcount

arr=input()
print(countSequence(arr))