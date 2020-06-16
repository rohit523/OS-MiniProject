def main(n,disk,d,sum):
    #n = int(input("Enter number of locations: "))
    #disk = int(input("Enter position of head: "))
    #d = list(map(int, input().split()))
    print("----------SCAN----------")
    d = list(d.split())
    print(d)
    for i in range(len(d)):
        d[i] = int(d[i])
    d.append(int(disk))
    print(d)
    d.sort()
    max = d[-1]
    
    for i in range(len(d)):
        if int(disk) == int(d[i]):
            dloc = i
            break
        
    for i in range(dloc,-1,-1):
        print("{} -->".format(d[i]),end = '')
        
    print("0 -->",end = '')

    for i in range(dloc+1,len(d)):
        print("{} -->".format(d[i]),end = '')
    print()    
    sum = int(disk) + int(max)
    print("Movement of total cylinders : {}".format(sum))

