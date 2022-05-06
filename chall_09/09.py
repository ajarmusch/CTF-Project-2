from pwn import *

binary = context.binary = ELF('./chall_09')

p = process('./chall_09')
p.recv()

p.send(binary.string(binary.sym.key))
p.interactive()
# NOT FINISHED
