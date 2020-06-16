def main(n,disk,d,sum):
    #n = int(input("Enter number of locations: "))
    #disk = int(input("Enter position of head: "))
    #d = list(map(int, input().split()))
    print("----------CSCAN----------")
    d = list(d.split())
    d.append(int(disk))
    d.append(0)
    d.append(199)
    for i in range(len(d)):
        d[i] = int(d[i])
    print(d)
    d.sort()
    j = d.index(int(disk))

    low = 0
    high = 199

    for i in range(len(d)):
        if int(disk) == int(d[i]):
            dloc = i
            break

    for i in range(dloc,len(d)):
        print("{} -->".format(d[i]),end = '')

    for i in range(dloc):
        print("{} -->".format(d[i]),end = '')
        
        
    sum = int(disk) + d[-1] - d[dloc + 1]
    print()
    print("Movement of total cylinders : {}".format(sum))
    
    
