def main(n,disk,d,sum):
    #n = int(input("Enter number of locations: "))
    #disk = int(input("Enter position of head: "))
    #d = list(map(int, input().split()))
    print("-------LOOK-------")
    d = list(d.split())
    for i in range(len(d)):
        d[i] = int(d[i])
    d.append(int(disk))
    d.sort()
    print(d)
    max = d[-1]
    sum = 0

    for i in range(len(d)):
        if int(disk) == int(d[i]):
            dloc = i
            break
        
    for i in range(dloc,-1,-1):
        print("{} -->".format(d[i]),end = '')
        sum += abs(int(disk) - int(d[i]))
        disk = int(d[i])
        
    for i in range(dloc+1,len(d)):
        print("{} -->".format(d[i]),end = '')
        sum += abs(int(disk) - int(d[i]))
        disk = int(d[i])
        
    print()
    print("Movement of total cylinders : {}".format(sum))

