from __main__ import *
def main(n,disk,d,sum):
    #n = int(input("Enter number of locations: "))
    #disk = int(input("Enter position of head: "))
    #d = list(map(int, input().split()))
    print("----------FCFS----------")
    d = list(d.split())
    print(d)
    sum =0

    print("{} -->".format(disk),end = '')
    for i in d:
        print("{} -->".format(i),end = '')
    print()
    
    for i in range(int(n)):
        x = abs(int(d[i])-int(disk))
        disk = int(d[i])
        sum += x
    print("Movement of total cylinders : {}".format(sum))



