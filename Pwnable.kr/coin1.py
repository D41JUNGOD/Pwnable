from pwn import *
from struct import *
from time import *

p = lambda x: pack("<L", x)

s = remote("pwnable.kr",9007)

print s.recv(2048)

sleep(3)
i = 1
while i<=1:
    tmp = s.recv(1024)
    n = tmp[tmp.find("N=")+2:tmp.find(" ")]
    c = tmp[tmp.find("C=")+2:tmp.find("  ")]
    j=1
    count = int(c)
    low = 0
    high = int(n)-1
    print n,c
    while(j<count):
        mid = (low+high)/2
        print low,high,mid
        for k in range(low,mid):
            s.send(str(k)+" ")
        s.send("\n")
        check = int(s.recv(1024))
        if check % 10 == 0:
            low = mid+1
        elif check % 10 ==9:
            high = mid-1
        j+=1
    s.send(str(mid))
    print(s.recv(1024))

print(s.recv(1024))

