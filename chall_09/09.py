from pwn import *
binary = context.binary = ELF('./chall_09')
p = process(binary.path)
p.send(binary.string(binary.sym.key))
p.interactive()
# NOT FINISHED
