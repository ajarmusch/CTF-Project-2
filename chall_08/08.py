from pwn import *

binary = context.binary = ELF('./chall_09')

if not args.REMOTE:
    p = process(binary.path)
else:
    p = remote('chal.2020.sunshinectf.org', 30009)

p.send(xor(binary.string(binary.sym.key),b'\x30'))
p.interactive()
