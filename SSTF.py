from heapq import *
def main(n,disk,d,sum):
    #n = int(input("Enter number of locations: "))
    #disk = int(input("Enter position of head: "))
    #d = list(map(int, input().split()))
    print("----------SSTF----------")
    d = list(d.split())
    print(d)
    sum = 0
    heap=[]
    while len(d)>0:
        for r in d:
            heappush(heap,(abs(int(disk)-int(r)),int(r)))
        try:
            x=heappop(heap)[1]
        except:
            pass
        print("{} -->".format(disk),end='')
        sum+=abs(int(disk)-x)
        
        disk=x
        d.remove(str(x))
        heap=[]

    print()
    print("Movement of total cylinders : {}".format(sum))

