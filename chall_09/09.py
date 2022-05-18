from pwn import *
binary = context.binary = ELF('./chall_09')
p = process(binary.path)
p.send(xor(binary.string(binary.sym.key),b'\x69'))
#string needs to be gotten manually you can set a break point at the 
#key. You need to check the stack and get the key value
p.interactive()
#FINISHED
