from pwn import *

binary = context.binary = ELF('./chall_08')

p = process('./chall_08')
p.recv()

p.send(xor(binary.string(binary.sym.key),b'\x30'))
p.interactive()
#NOT FINISHED
