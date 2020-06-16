def main(n,disk,d,sum):
    #n = int(input("Enter number of locations: "))
    #disk = int(input("Enter position of head: "))
    #d = list(map(int, input().split()))
    print("-----------CLOOK----------")
    d = list(d.split())
    d.append(int(disk))
    for i in range(len(d)):
        d[i] = int(d[i])
    d.sort()
    print(d)
    j = d.index(int(disk))
    sum = 0

    for i in range(len(d)):
        if int(disk) == int(d[i]):
            dloc = i
            break

    for i in range(dloc, -1,-1):
        print("{} -->".format(d[i]),end = '')
        #sum += abs(int(disk)-d[i])
        disk = d[i]

    for i in range(dloc+1,len(d)):
        print("{} -->".format(d[i]),end = '')
        #sum += abs(int(disk)-d[i])
        disk = d[i]
        
    sum = abs(int(d[dloc])-d[0]) + abs(d[-1]-d[dloc+1])
    print()
    print("Movement of total cylinders : {}".format(sum))
