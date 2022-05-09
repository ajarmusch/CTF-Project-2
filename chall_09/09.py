from pwn import *
binary = context.binary = ELF('./chall_09')
p = process(binary.path)
p.send(xor(binary.string(binary.sym.key),b'\x69'))
p.interactive()
# NOT FINISHED
