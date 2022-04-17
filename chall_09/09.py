from pwn import *

binary = context.binary = ELF('./chall_16')

if not args.REMOTE:
    p = process(binary.path)
else:
    p = remote('chal.2020.sunshinectf.org', 30016)

p.send(binary.string(binary.sym.key))
p.interactive()
