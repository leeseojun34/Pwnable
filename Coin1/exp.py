from pwn import *

p = remote("pwnable.kr", 9007)

print(p.recv())

for i in range(0, 100, 1):
    print(p.recvuntil("N="))
    upper = int(p.recvuntil(" "))
    lower = 0
    print(p.recvuntil("C="))
    c = int(p.recvuntil(" "))

    count = 0

    while count != c:
        count += 1
        send_data = ""
        middle = (lower+upper)/2
        for i in range(lower, upper):
            send_data += str(middle)
            send_data += " "
        send_data += str(middle)
        print(send_data)
        p.sendline(send_data)
        upper = int(p.recv())
        print(upper)
        if upper % 10 == 9:
            upper = middle
        else:
            lower = middle + 1

        middle = (lower+upper)/2
        p.sendline(str(middle))
        print(str(middle))
        print(p.recv())
print(p.recv())
